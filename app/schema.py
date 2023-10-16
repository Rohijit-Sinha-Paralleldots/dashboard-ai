from typing import List, Dict, Union, Any

from sqlalchemy.engine.row import RowMapping
from pydantic import BaseModel


class ChatBody(BaseModel):
    role: str
    context_uid: str


class ChatInput(BaseModel):
    history: Union[List[ChatBody], None]
    user_input: str


class ChatResult(BaseModel):
    response: str
    status: int
    query: str = None
    message: Union[str, None] = None


class RequestResult(BaseModel):
    context_uid: str
    result: Union[str, int, List[Dict]]
