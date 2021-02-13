import json

from kafka import KafkaProducer


class MessageProducer:
    def __init__(self):
        # noinspection PyTypeChecker
        self.__producer: KafkaProducer = None

    def init_app(self, env):
        self.__producer = KafkaProducer(
            bootstrap_servers="app-kafka:9093",
            compression_type="gzip",
            value_serializer=lambda x: json.dumps(x).encode("utf-8"),
        )

    def send(self, topic: str, value: dict):
        self.__producer.send(topic=topic, value=value)
