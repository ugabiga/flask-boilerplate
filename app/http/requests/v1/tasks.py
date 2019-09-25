from voluptuous import All, Required, Schema

from app.http.requests.v1 import BaseRequest


class CreateTaskRequest(BaseRequest):
    def __init__(self, user_id: int, title: str, contents: str):
        self.user_id = user_id
        self.title = title
        self.contents = contents

    @classmethod
    def _get_validation_schema(cls) -> Schema:
        return Schema(
            {
                Required("user_id"): All(int),
                Required("title"): All(str),
                Required("contents"): All(str),
            }
        )
