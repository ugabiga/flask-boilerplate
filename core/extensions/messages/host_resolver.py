from __future__ import annotations


class MessageHostResolver:
    def __init__(self, env: str, base_url: str):
        self.__env = env
        self.__base_url = base_url

    def get_bootstrap_servers(self):
        return self.__base_url

    @classmethod
    def make_from_dict(cls, config: dict) -> MessageHostResolver:
        return MessageHostResolver(
            env=config["ENV"], base_url=config["MESSAGE_BASE_URL"]
        )
