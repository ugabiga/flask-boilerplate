from app.core.repositories.tasks import TaskRepository
from app.data.sql.models.tasks import Task
from app.extensions.database import sql_session


class TaskSQLRepository(TaskRepository):
    def create_task(self, user_id: int, title: str, contents: str) -> Task:
        task = Task(user_id=user_id, title=title, contents=contents)
        sql_session.add(task)
        sql_session.commit()

        return task.to_entity()
