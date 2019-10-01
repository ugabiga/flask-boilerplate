import voluptuous as v

from app.http.requests import BaseRequest


class CreateTaskRequest(BaseRequest):
    def __init__(self, user_id: int, title: str, contents: str) -> None:
        self.user_id = user_id
        self.title = title
        self.contents = contents

    @classmethod
    def _get_validation_schema(cls) -> v.Schema:
        return v.Schema(
            {
                v.Required("user_id"): v.All(int),
                v.Required("title"): v.All(str),
                v.Required("contents"): v.All(str),
            }
        )


class GetAllTasksRequest(BaseRequest):
    def __init__(self, previous_id: int = 0, limit: int = 10) -> None:
        self.limit = limit
        self.previous_id = previous_id

    @classmethod
    def _get_validation_schema(cls) -> v.Schema:
        return v.Schema(
            {v.Optional("previous_id"): v.All(int), v.Optional("limit"): v.All(int)}
        )
