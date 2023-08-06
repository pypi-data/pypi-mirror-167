import os
from typing import Optional

from motor.motor_asyncio import AsyncIOMotorClient

from .singleton import Singleton

DEFAULT_ENV_NAME = 'default'


_connections: dict = {}


class DBConnection(object, metaclass=Singleton):
    __slots__ = (
        'address',
        'db_name',
        'max_pool_size',
    )

    _connections: dict = {}

    def __init__(
        self,
        address: str,
        db_name: str,
        max_pool_size: int = 250,
        env_name: str = DEFAULT_ENV_NAME,
    ):
        self.address = address
        self.db_name = db_name
        self.max_pool_size = max_pool_size
        if env_name not in _connections:
            _connections[env_name] = self

    def _init_mongo_connection(self, connect: bool = False) -> AsyncIOMotorClient:
        client = AsyncIOMotorClient(self.address, connect=connect)
        return client

    def _get_motor_client(self) -> AsyncIOMotorClient:
        if os.getpid() in self._connections:
            return self._connections[os.getpid()]
        else:
            mongo_connection = self._init_mongo_connection()
            self._connections[os.getpid()] = mongo_connection
            return mongo_connection


def connect(
    address: str,
    database_name: str,
    ssl: bool = False,
    max_pool_size: int = 100,
    ssl_cert_path: Optional[str] = None,
    server_selection_timeout_ms: int = 60000,
    connect_timeout_ms: int = 30000,
    socket_timeout_ms: int = 60000,
    env_name: Optional[str] = DEFAULT_ENV_NAME,
) -> None:
    """init connection to mongodb

    Args:
        address (str): full connection string
        dbname (str): mongo db name
        ssl (bool, optional): flag for ssl cert. Defaults to False.
        max_pool_size (int, optional): max connection pool. Defaults to 100.
        ssl_cert_path (Optional[str], optional): path to ssl cert. Defaults to None.
        server_selection_timeout_ms (int, optional): ServerSelectionTimeoutMS. Defaults to 60000.
        connect_timeout_ms (int, optional): ConnectionTimeoutMS. Defaults to 30000.
        socket_timeout_ms (int, optional): SocketTimeoutMS. Defaults to 60000.
        env_name (Optional[str], optional): connection env name. Defaults to None.
    """
    os.environ['MOTORDANTIC_DATABASE'] = database_name
    os.environ['MOTORDANTIC_ADDRESS'] = address
    os.environ['MOTORDANTIC_ENV_NAME'] = env_name or DEFAULT_ENV_NAME
    _ = DBConnection(
        address=address,
        db_name=database_name,
        env_name=env_name or DEFAULT_ENV_NAME,
    )
