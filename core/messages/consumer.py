import json
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Optional

# noinspection PyProtectedMember
from kafka import KafkaConsumer, OffsetAndMetadata, TopicPartition
from kafka.consumer.fetcher import ConsumerRecord


@dataclass
class MessageConsumerDto:
    topic: str
    partition: int
    offset: int
    timestamp: datetime
    timestamp_type: int
    key: str
    value: json  # type: ignore
    headers: list
    checksum: str
    serialized_key_size: int
    serialized_value_size: int
    serialized_header_size: int

    def __dict__(self):
        return asdict(self)


class MessageConsumer:
    def __init__(self):
        # noinspection PyTypeChecker
        self.__consumer: KafkaConsumer = None

    def init_app(self, env: str, topics=()) -> None:
        self.__init_consumer(topics=topics)

    def __init_consumer(self, topics=()) -> None:
        self.__consumer = KafkaConsumer(
            bootstrap_servers="app-kafka:9093",
            auto_offset_reset="earliest",
            enable_auto_commit=False,
            group_id="test_group",
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
            consumer_timeout_ms=1000,
        )
        self.__consumer.unsubscribe()
        self.__consumer.subscribe(topics=topics)

    def __convert_message_to_dict(self, message: ConsumerRecord):
        return MessageConsumerDto(*message)

    def get_message(self) -> Optional[MessageConsumerDto]:
        for message in self.__consumer:
            if isinstance(message, ConsumerRecord):
                return self.__convert_message_to_dict(message=message)
            return message

        return None

    def commit_message(self, dto: MessageConsumerDto) -> None:
        topic_partition = TopicPartition(dto.topic, dto.partition)
        offsets = {topic_partition: OffsetAndMetadata(dto.offset + 1, None)}
        self.__consumer.commit(offsets)
