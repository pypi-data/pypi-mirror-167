import time
import json
from typing import Union

from redis import StrictRedis, ConnectionPool

from config import settings


def standard_time() -> str:
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time())))


class DbRedisHelper(object):

    def __init__(self) -> None:
        self.connection = StrictRedis(
            connection_pool=ConnectionPool(
                host=settings.redis_host,
                port=settings.redis_port,
                db=settings.redis_lock_db,
                username=settings.redis_username,
                password=settings.redis_password,
                decode_responses=True
            )
        )
        self.prefix = 'lock'

    def __del__(self) -> None:
        self.connection.close()

    def acquire(self, lock_name: str, expire_time: int = None) -> bool:
        lock_key = f'{self.prefix}:{lock_name}'
        lock_value = standard_time()
        if expire_time is None:
            expire_time = settings.redis_spider_expire_time
        if self.connection.setnx(lock_key, lock_value):
            self.connection.expire(lock_key, expire_time)
            return True
        else:
            if self.connection.ttl(lock_key) == -1:
                self.connection.expire(lock_key, expire_time)
            return False

    def lock_exists(self, lock_name: str) -> int:
        return self.connection.exists(lock_name)

    def release(self, lock_name: str) -> None:
        lock_key = f'{self.prefix}:{lock_name}'
        self.connection.delete(lock_key)

    def process_acquire(self, lock_name: str, lock_value: str = None, expire_time: int = None) -> None:
        if lock_value is None:
            lock_value = standard_time()
        if expire_time is None:
            expire_time = settings.redis_process_expire_time
        if self.connection.setnx(lock_name, lock_value):
            self.connection.expire(lock_name, expire_time)
        else:
            self.connection.expire(lock_name, expire_time)

    def delete_key(self, lock_name: str) -> int:
        return self.connection.delete(lock_name)

    def from_key_get_value(self, key_name: str) -> Union[dict, None]:
        try:
            return json.loads(self.connection.get(key_name))
        except:
            return None

    def get_tasks(self, keys: list[str], is_load: bool = True) -> dict:
        values = self.connection.mget(keys)
        if is_load:
            values = []
            for value in self.connection.mget(keys):
                if value is not None:
                    value = json.loads(value)
                values.append(value)
        return dict(zip(keys, values))

    def get_proces_info(self) -> list:

        return self.connection.keys(pattern='node:*')

    def get_backend_task(self) -> list:
        return self.connection.keys(pattern='backend:*')

    def get_all_task(self) -> list:
        return self.connection.keys(pattern='all:*')

    def get_insert_task(self) -> list:
        return self.connection.keys(pattern='insert:*')

    def get_delete_task(self) -> list:
        return self.connection.keys(pattern='delete:*')

    def get_update_task(self) -> list:
        return self.connection.keys(pattern='update:*')

    def string_set(self, key: str, value: str) -> bool:
        return self.connection.set(key, value)


redis_db = DbRedisHelper()
