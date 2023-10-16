from typing import Dict

from .abstract_storage import AbstractStorage


class ObjectStorage(AbstractStorage):
    def __init__(self) -> None:
        self._storage: Dict[str, str] = {}

    def save_context(self, context: str):
        uid = self._get_id()
        self._storage[uid] = context
        return uid

    def get_context_by_id(self, id: str):
        return self._storage.get(id, None)
