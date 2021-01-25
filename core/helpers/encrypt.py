import hashlib


class EncryptHelper:
    def __init__(self, salt: str = "secret") -> None:
        self.__salt: str = salt

    def encode(self, keyword: str) -> str:
        return hashlib.sha512((keyword + self.__salt).encode("utf-8")).hexdigest()
