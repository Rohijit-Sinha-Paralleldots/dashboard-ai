from uuid import uuid4
from abc import ABC, abstractmethod
from typing import Any


class AbstractStorage(ABC):
    def _get_id(self) -> str:
        uid = uuid4()
        return uid.hex

    @abstractmethod
    def save_context(self, context: str, id: str) -> str:
        pass

    @abstractmethod
    def get_context_by_id(self, id: str) -> str:
        pass
