from datetime import datetime

import click
import inject
from flask import current_app
from pydantic import ValidationError

from app.extensions.database import sql
from core.extensions.messages.consumer import MessageConsumer, MessageConsumerDto
from core.extensions.messages.producer import MessageProducer
from core.repositories.users import UserRepository
from core.use_cases.users.update_user import UpdateUserDto, UpdateUserUseCase


@current_app.cli.command("data")
def create_data():
    sql.drop_all()
    sql.create_all()

    user_repo = inject.instance(UserRepository)
    user_repo.create_user("sample")


@click.argument("topic")
@current_app.cli.command("producer")
def run_producer(topic: str):
    producer = MessageProducer(current_app.config)
    producer.send(f"{topic}", value={"user_id": 1, "nickname": "sample nickname"})
    print(f"sending topic=={topic} at=={datetime.now()}")


@click.argument("topic")
@current_app.cli.command("consumer")
def run_consumer(topic: str):
    consumer = MessageConsumer(current_app.config)
    consumer.set_topics(
        topics=f"{topic}",
    )

    while True:
        message = consumer.get_message()
        if message is None:
            print(".")
            continue

        try:
            execute_by_consumer(topic, message)
        except ValidationError as e:
            print(f"validation error == {e}")

        consumer.commit_message(message)


def execute_by_consumer(topic: str, message: MessageConsumerDto):
    if topic in ["1", "2"]:
        dto = UpdateUserDto.validate_from_dict(message.value)
        output = inject.instance(UpdateUserUseCase).execute(dto)
        print(output.get_data())
    else:
        print("wrong topic")
        return
