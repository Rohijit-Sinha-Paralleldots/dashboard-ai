from .storage.storage_factory import storage_obj


class ContextStore:
    def __init__(self) -> None:
        self._storage_obj = storage_obj

    def save_context(self, context: str) -> str:
        con_uid = self._storage_obj.save_context(context)
        # print("con_uid=>",con_uid)
        # print("context=>",self._storage_obj._storage)
        return con_uid

    def get_context_by_id(self, uid: str) -> str:
        context = self._storage_obj.get_context_by_id(uid)
        # print("context=>",self._storage_obj._storage)
        return context
