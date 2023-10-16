from typing import Dict

from redis import Redis

from .abstract_storage import AbstractStorage
from app.exceptions import ImproperlyConfiguredException

class RedisStorage(AbstractStorage):
    def __init__(self, config: Dict) -> None:
        if {"host","port","password"} not in set(config.keys()):
            raise ImproperlyConfiguredException
        self._conn = Redis(**config)
        