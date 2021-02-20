import json
from typing import Optional

from kafka import KafkaProducer

from core.extensions.messages.host_resolver import MessageHostResolver


class MessageProducer:
    def __init__(self, config: dict):
        self.__bootstrap_servers = MessageHostResolver.make_from_dict(
            config
        ).get_bootstrap_servers()
        self.__producer: Optional[KafkaProducer] = None

    def __connect(self):
        if self.__producer is not None:
            return

        self.__producer: KafkaProducer = KafkaProducer(
            bootstrap_servers=self.__bootstrap_servers,
            compression_type="gzip",
            value_serializer=lambda x: json.dumps(x).encode("utf-8"),
        )

    def send(self, topic: str, value: dict):
        self.__connect()
        self.__producer.send(topic=topic, value=value)
