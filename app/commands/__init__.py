from flask import Flask


# noinspection PyUnusedLocal
def init_commands(app: Flask):
    from . import messages  # noqa isort:skip
