from typing import Optional

import voluptuous as v

from app.core.dtos.tasks import UpdateTaskDto
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


class UpdateTaskRequest(BaseRequest):
    def __init__(
        self, task_id: int, title: Optional[str], contents: Optional[str]
    ) -> None:
        self.task_id = task_id
        self.title = title
        self.contents = contents

    def to_dto(self) -> UpdateTaskDto:
        return UpdateTaskDto(
            self.task_id,
            self.title,
            self.contents,
        )

    @classmethod
    def _get_validation_schema(cls) -> v.Schema:
        return v.Schema(
            {
                v.Required("task_id"): v.All(int),
                v.Optional("title"): v.All(str),
                v.Optional("contents"): v.All(str),
            }
        )
