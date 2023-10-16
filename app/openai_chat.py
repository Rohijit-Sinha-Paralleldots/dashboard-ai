import os
import pprint
import json
import uuid
from typing import Any, Generator

import openai
import tiktoken
from fastapi.exceptions import HTTPException
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from .schema import ChatInput, ChatResult, RequestResult
from .prompt_generators.prompt_gen import PromptGen, MODEL
from .context_stores.context_store import ContextStore

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", None)


class QueryConversation:
    return_message = "Please rephrase your query"

    def __init__(self, project_id) -> None:
        self.project_id = project_id

    def _get_conversation_result(self, chat: ChatInput) -> Generator[Any | list | dict, None, None] | Any | list | dict:
        """Get result object from conversing with chatGpt"""
        if not OPENAI_API_KEY:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Cannot use OpenAI service")
        prompt_gen = PromptGen(self.project_id)
        chat_messages = prompt_gen.generate_prompt_message(chat)
        # pprint.pprint(len(chat_messages))
        res = openai.ChatCompletion.create(
            model=MODEL,
            messages=chat_messages
        )
        return res

    def _get_coversation_message(self, result: Generator[Any | list | dict, None, None] | Any | list | dict) -> str:
        """Get message as a string"""
        message = result["choices"][0]["message"]["content"]
        print(f"Token Used. Token length={result['usage']['total_tokens']}")
        return message

    def _parse_query(self, message: str) -> ChatResult:
        """Parse SQL query from the string message"""
        split_message = message.split(" ")
        if split_message[0] == "500":
            return_message = " ".join(split_message[1:])
            return ChatResult(status=500, message=return_message, response=message)
        elif split_message[0] == "200":
            query = " ".join(split_message[1:])
            return ChatResult(status=200, query=query, response=message)
        else:
            return ChatResult(status=500, message=self.return_message, response=message)

    def _save_context(self, context: str) -> str:
        """Save a context and return its id"""
        con_store = ContextStore()
        con_uid = con_store.save_context(context)
        return con_uid

    def get_sql_query(self, chat: ChatInput) -> ChatResult:
        """Get SQL query from NLP query"""
        res = self._get_conversation_result(chat)
        message = self._get_coversation_message(res)
        return self._parse_query(message)

    async def get_db_data(self, chat: ChatInput, conn: AsyncConnection):
        user_con_uid = self._save_context(chat.user_input)
        chat_res = self.get_sql_query(chat)
        result = None
        context = chat_res.response
        if chat_res.status == 500:
            result = chat_res.message
        elif chat_res.status == 200:
            print("SQL Query =>", chat_res.query)
            query = text(chat_res.query)
            try:
                result = await conn.execute(query)
                result = [res._mapping for res in result]
            except SQLAlchemyError as exc:
                print(exc._message())
                result = self.return_message
        con_uid = self._save_context(context)
        return RequestResult(
            user_context_uid=user_con_uid,
            assistant_context_id=con_uid,
            result=result
        )

    def get_token_count(self, chat: ChatInput):
        prompt_gen = PromptGen(self.project_id)
        chat_messages = prompt_gen.generate_prompt_message(chat)
        try:
            encoding = tiktoken.encoding_for_model(MODEL)
        except KeyError:
            encoding = tiktoken.get_encoding("cl100k_base")
        if MODEL == "gpt-3.5-turbo":  # note: future models may deviate from this
            num_tokens = 0
            for message in chat_messages:
                # every message follows <im_start>{role/name}\n{content}<im_end>\n
                num_tokens += 4
                for key, value in message.items():
                    num_tokens += len(encoding.encode(value))
                    if key == "name":  # if there's a name, the role is omitted
                        num_tokens += -1  # role is always required and always 1 token
            num_tokens += 2  # every reply is primed with <im_start>assistant
            return num_tokens
        else:
            raise NotImplementedError(
                f"""num_tokens_from_messages() is not presently implemented for model {MODEL}""")
