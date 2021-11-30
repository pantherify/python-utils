import os
import base64
from typing import Any
from uuid import UUID, uuid4, uuid5
from dotenv import load_dotenv

from .logger.core import logger
from .validator.core import Validator


class Fur:
    def __init__(self) -> None:
        load_dotenv()

        self.secret: UUID = UUID(self.__get_env("secret"))
        self.seed: bytes = self.__generate_seed()
        self.name: str = self.__generate_name()

    def __get_env(self, key, default=None) -> str | None:
        Validator.validate_str(key)

        if default is not None:
            Validator.validate_str(default)

        value = os.getenv(key)
        if not value:
            return default
        return value

    def __generate_seed(self) -> bytes:
        seed = uuid4().__str__().encode("ascii")

        return seed

    def __generate_name(self) -> str:
        name: str = base64.b64encode(self.seed).decode("ascii")

        return name

    def __generate_key(self) -> str:
        key: str = uuid5(namespace=self.secret, name=self.name).__str__()

        return key

    def generate_keyring(self) -> dict[str, Any]:
        keyring: dict[str, Any] = {"header": self.name, "key": self.__generate_key()}

        return keyring
