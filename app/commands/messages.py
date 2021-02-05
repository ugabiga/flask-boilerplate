from flask import current_app


@current_app.cli.command("run-producer")
def run_producer():
    from app.extensions.messages.producer import MessageProducer

    producer = MessageProducer()
    producer.init_app("")
    for _ in range(100):
        producer.send("test", value={"result": True})
        print("sent message")


@current_app.cli.command("run-consumer")
def run_consumer():
    from app.extensions.messages.consumer import MessageConsumer

    consumer = MessageConsumer()
    consumer.init_app("", "test")

    while True:
        message = consumer.get_message()

        if message is None:
            print(".")
            continue

        print(message.__dict__())
        consumer.commit_message(message)
