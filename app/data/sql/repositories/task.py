from typing import List
from typing import Optional

from core.entities.tasks import Task as TaskEntity
from core.repositories.tasks import TaskRepository
from app.data.sql.models.task import Task
from app.extensions.database import sql_session


class TaskSQLRepository(TaskRepository):
    def create_task(self, user_id: int, title: str, contents: str) -> TaskEntity:
        task = Task(user_id=user_id, title=title, contents=contents)
        sql_session.add(task)
        sql_session.commit()

        return task.to_entity()

    def update_task(self, entity: Task) -> Optional[TaskEntity]:
        task = self._one_or_none(entity.id)

        if not task:
            return None

        task.title = entity.title if entity.title else task.title
        task.contents = entity.contents if entity.contents else task.contents
        sql_session.commit()

        return task.to_entity()

    def read_task(self, task_id) -> Optional[TaskEntity]:
        task = self._one_or_none(task_id)

        if not task:
            return None

        return task.to_entity()

    def get_tasks(self, previous_id: int, limit: int) -> List[TaskEntity]:
        query = sql_session.query(Task)

        if previous_id > 0:
            query = query.filter(Task.id > previous_id)

        tasks = query.order_by(Task.id).limit(limit).all()

        return [task.to_entity() for task in tasks]

    def delete_all_tasks(self) -> bool:
        sql_session.query(Task).delete()
        sql_session.commit()

        return True

    def _one_or_none(self, task_id: int) -> Task:
        task = sql_session.query(Task).filter(Task.id == task_id).one_or_none()
        return task
