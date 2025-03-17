from app.services.task_service import TaskService
from app.schemas.task_schema import TaskSchema
from unittest.mock import MagicMock


def test_create_task() -> None:
    db_mock = MagicMock()
    task_data = TaskSchema(title="Test Task", description="Test Description", completed=False)

    TaskService.create_task(db_mock, task_data)

    db_mock.commit.assert_called_once()
