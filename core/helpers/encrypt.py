import hashlib


class EncryptHelper:
    def __init__(self, salt=""):
        if salt == "":
            self.__salt: str = "secret"
        else:
            self.__salt: str = salt

    def encode(self, keyword: str) -> str:
        return hashlib.sha512((keyword + self.__salt).encode("utf-8")).hexdigest()
