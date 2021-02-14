import json

from kafka import KafkaProducer

from core.messages.host_resolver import MessageHostResolver


class MessageProducer:
    def __init__(self, config: dict):
        bootstrap_servers = MessageHostResolver.make_from_dict(
            config
        ).get_bootstrap_servers()
        self.__producer: KafkaProducer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            compression_type="gzip",
            value_serializer=lambda x: json.dumps(x).encode("utf-8"),
        )

    def send(self, topic: str, value: dict):
        self.__producer.send(topic=topic, value=value)
