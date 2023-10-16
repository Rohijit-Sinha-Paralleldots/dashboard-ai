from ..storage_classes.object_storage import ObjectStorage


class StorageFactory:
    def __init__(self) -> None:
        self._storage_obj = self.get_storage_obj()

    def get_storage_obj(self):
        if hasattr(self, "_storage_obj"):
            return self._storage_obj
        return ObjectStorage()


storage_obj = StorageFactory().get_storage_obj()
