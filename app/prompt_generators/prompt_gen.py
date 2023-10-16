from typing import List, Dict
from .initial_texts.initial_texts import InitialText
from ..schema import ChatInput, ChatBody
from ..context_stores.context_store import ContextStore

MODEL = "gpt-3.5-turbo"


class PromptGen:
    def __init__(self, project_id) -> None:
        self.project_id = project_id

    def _get_system_text(self):
        initial_text = InitialText(self.project_id).get_initial_text()
        return initial_text
    
    def _get_context_by_id(self, uid:str)->str:
        con_store = ContextStore()
        context = con_store.get_context_by_id(uid)
        return context

    def _get_history(self, history: List[ChatBody]):
        history_list = [{
            "role": item.role,
            "content": self._get_context_by_id(item.context_uid)
        } for item in history]
        return history_list

    def generate_prompt_message(self, chat_input: ChatInput):
        initial_text = self._get_system_text()
        messages: List[Dict[str, str]] = []
        messages.append({
            "role": "system",
            "content": initial_text
        })
        history = self._get_history(chat_input.history)
        messages.extend(history)
        messages.append({
            "role": "user",
            "content": f"Input: {chat_input.user_input}"
        })
        return messages
