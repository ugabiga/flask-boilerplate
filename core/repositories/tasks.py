from typing import List, Optional

from core.entities.tasks import Task as TaskEntity
from core.extensions import rdb
from core.models.task import TaskModel


class TaskRepository:
    def create_task(self, user_id: int, title: str, contents: str) -> TaskEntity:
        new_task = TaskModel(user_id=user_id, title=title, contents=contents)
        task = rdb.Query(new_task).create()

        return task.to_entity()

    def update_task(
        self, task_id: int, title: Optional[str] = None, contents: Optional[str] = None
    ) -> Optional[TaskEntity]:
        task = rdb.Query(TaskModel).filter(TaskModel.id == task_id).one_or_none()

        if not task:
            return None

        task.title = title if title else task.title
        task.contents = contents if contents else task.contents

        rdb.Query(TaskModel).filter(TaskModel.id == task_id).update(
            {
                TaskModel.title: task.title,
                TaskModel.contents: task.contents,
            }
        )

        return task.to_entity()

    def read_task(self, task_id) -> Optional[TaskEntity]:
        task = rdb.Query(TaskModel).filter(TaskModel.id == task_id).one_or_none()

        if not task:
            return None

        return task.to_entity()

    def get_tasks(self, previous_id: int, limit: int) -> List[TaskEntity]:
        query = rdb.Query(TaskModel)

        if previous_id > 0:
            query = query.filter(TaskModel.id > previous_id)

        tasks = query.order_by(TaskModel.id).limit(limit).all()

        return [task.to_entity() for task in tasks]

    def delete_all_tasks(self) -> bool:
        rdb.Query(TaskModel).delete()

        return True
