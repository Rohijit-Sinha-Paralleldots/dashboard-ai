from typing import List, Dict, Union, Any

from sqlalchemy.engine.row import RowMapping
from pydantic import BaseModel, Field


class ChatBody(BaseModel):
    role: str
    context_uid: str


class ChatInput(BaseModel):
    history: Union[List[ChatBody], None] = Field(default_factory=list, description="List of chat body objects.")
    user_input: str


class ChatResult(BaseModel):
    response: str
    status: int
    query: str = None
    message: Union[str, None] = None


class RequestResult(BaseModel):
    user_context_uid: str
    assistant_context_id: str
    result: Union[str, List[Dict]]
