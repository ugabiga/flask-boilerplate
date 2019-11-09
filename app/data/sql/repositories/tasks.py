from typing import List

from app.core.repositories.tasks import TaskRepository
from app.data.sql.models.tasks import Task
from app.extensions.database import sql_session


class TaskSQLRepository(TaskRepository):
    def get(self, previous_id: int, limit: int) -> List[Task]:
        query = sql_session.query(Task)

        if previous_id > 0:
            query = query.filter(Task.id > previous_id)

        tasks = query.order_by(Task.id).limit(limit).all()

        return [task.to_entity() for task in tasks]

    def create_task(self, user_id: int, title: str, contents: str) -> Task:
        task = Task(user_id=user_id, title=title, contents=contents)
        sql_session.add(task)
        sql_session.commit()

        return task.to_entity()
