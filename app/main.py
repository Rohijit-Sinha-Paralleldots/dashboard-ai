from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncConnection

from .schema import ChatInput, ChatResult, RequestResult
from .openai_chat import QueryConversation
from .dependencies import get_db_engine

app = FastAPI()


@app.post("/get-sql-query/{project_id}")
async def get_sql_query(project_id: str, chat_input: ChatInput) -> ChatResult:
    """Takes NLP query and gives us corresponding sql query for the project with id project_id"""
    convo = QueryConversation(project_id)
    query = convo.get_sql_query(chat_input)
    return query


@app.post("/get-token-count/{project_id}")
async def get_token_count(project_id: str, chat_input: ChatInput) -> int:
    convo = QueryConversation(project_id)
    count = convo.get_token_count(chat_input)
    return count


@app.post("/get-query-result/{project_id}")
async def get_query_result(project_id: str, chat_input: ChatInput, conn: AsyncConnection = Depends(get_db_engine)) -> RequestResult:
    """Takes nlp query and gives us the data for the query"""
    print("----------------------------")
    convo = QueryConversation(project_id)
    result = await convo.get_db_data(chat_input, conn)
    return result
