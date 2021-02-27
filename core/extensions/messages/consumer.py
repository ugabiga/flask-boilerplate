import json
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Optional

# noinspection PyProtectedMember
from kafka import KafkaConsumer, OffsetAndMetadata, TopicPartition
from kafka.consumer.fetcher import ConsumerRecord

from core.extensions.messages.host_resolver import MessageHostResolver


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

    @classmethod
    def from_kafka_message(cls, message: ConsumerRecord):
        return MessageConsumerDto(*message)


class MessageConsumer:
    def __init__(self, config: dict):
        self.__bootstrap_servers = MessageHostResolver.make_from_dict(
            config
        ).get_bootstrap_servers()

        self.__group_id = config["MESSAGE_CONSUMER_GROUP_ID"]
        self.__consumer: KafkaConsumer = KafkaConsumer(
            bootstrap_servers=self.__bootstrap_servers,
            auto_offset_reset="earliest",
            enable_auto_commit=False,
            group_id=self.__group_id,
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
            consumer_timeout_ms=1000,
        )

    def set_topics(self, topics=()) -> None:
        self.__consumer.unsubscribe()
        self.__consumer.subscribe(topics=topics)

    def get_message(self) -> Optional[MessageConsumerDto]:
        for message in self.__consumer:
            if isinstance(message, ConsumerRecord):
                return MessageConsumerDto.from_kafka_message(message)
            return message

        return None

    def commit_message(self, dto: MessageConsumerDto) -> None:
        topic_partition = TopicPartition(dto.topic, dto.partition)
        offsets = {topic_partition: OffsetAndMetadata(dto.offset + 1, None)}
        self.__consumer.commit(offsets)
