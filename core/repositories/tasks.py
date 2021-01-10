from typing import List, Optional

from app.extensions.database import session, sql_client
from core.entities.tasks import Task as TaskEntity
from core.models.task import TaskModel


class TaskRepository:
    def create_task(self, user_id: int, title: str, contents: str) -> TaskEntity:
        task = TaskModel(user_id=user_id, title=title, contents=contents)
        sql_client.add(task)

        return task.to_entity()

    def update_task(
        self, task_id: int, title: Optional[str] = None, contents: Optional[str] = None
    ) -> Optional[TaskEntity]:
        task = self._one_or_none(task_id)

        if not task:
            return None

        task.title = title if title else task.title
        task.contents = contents if contents else task.contents
        session.commit()

        return task.to_entity()

    def read_task(self, task_id) -> Optional[TaskEntity]:
        task = self._one_or_none(task_id)

        if not task:
            return None

        return task.to_entity()

    def get_tasks(self, previous_id: int, limit: int) -> List[TaskEntity]:
        query = session.query(TaskModel)

        if previous_id > 0:
            query = query.filter(TaskModel.id > previous_id)

        tasks = query.order_by(TaskModel.id).limit(limit).all()

        return [task.to_entity() for task in tasks]

    def delete_all_tasks(self) -> bool:
        session.query(TaskModel).delete()
        session.commit()

        return True

    def _one_or_none(self, task_id: int) -> TaskModel:
        task = session.query(TaskModel).filter(TaskModel.id == task_id).one_or_none()
        return task
