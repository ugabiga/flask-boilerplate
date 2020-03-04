from app.core.use_cases.create_tasks import CreateTaskUseCaseOutput
from app.extensions.marshmallow import ma


class TaskSchema(ma.Schema):
    class Meta:
        fields = ("id", "user_id", "title", "contents")


def build_create_task_success_response(use_case_output: CreateTaskUseCaseOutput):
    task = use_case_output.get_data()
    return TaskSchema.dump(task)
