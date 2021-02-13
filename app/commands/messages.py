from datetime import datetime
from time import sleep

import click
import inject
from flask import current_app

from app.extensions.database import sql
from core.repositories.tasks import TaskRepository
from core.repositories.users import UserRepository


@current_app.cli.command("data")
def create_data():
    sql.drop_all()
    sql.create_all()
    user_repo = inject.instance(UserRepository)
    task_repo = inject.instance(TaskRepository)

    user = user_repo.create_user("sample")
    task_repo.create_task(user_id=user.id, title="sample", contents="contents")


@click.argument("topic")
@current_app.cli.command("producer")
def run_producer(topic: str):
    from core.messages.producer import MessageProducer

    producer = MessageProducer()
    producer.init_app("")
    while True:
        producer.send(f"test_{topic}", value={"result": True})
        print(f"sending topic=={topic} at=={datetime.now()}")
        sleep(0.1)


@click.argument("topic")
@current_app.cli.command("consumer")
def run_consumer(topic: str):
    from core.messages.consumer import MessageConsumer

    consumer = MessageConsumer()
    consumer.init_app("", f"test_{topic}")

    while True:
        message = consumer.get_message()

        if message is None:
            print(".")
            continue

        print(f"processing topic=={topic} at=={message.timestamp}")
        user_repo = inject.instance(UserRepository)
        user_repo.update_user(1, f"new_{topic}")
        consumer.commit_message(message)
