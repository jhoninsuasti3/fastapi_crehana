import pytest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from app.services.task_service import TaskService
from app.domain.task import Task
from app.schemas.task_schema import TaskSchema


@pytest.fixture
def mock_db_fixture() -> MagicMock:  # ✅ Cambiar el nombre del fixture
    return MagicMock(spec=Session)


@pytest.fixture
def sample_task() -> Task:
    return Task(id=1, title="Sample Task", description="Test task", completed=False)


@pytest.fixture
def sample_task_schema() -> TaskSchema:
    return TaskSchema(title="Sample Task", description="Test task", completed=False)


def test_get_all_tasks(mock_db_fixture: MagicMock) -> None:  # ✅ Usar el nuevo nombre del fixture
    mock_db_fixture.query.return_value.all.return_value = [
        Task(id=1, title="Test", description="Task", completed=False)
    ]
    tasks = TaskService.get_all_tasks(mock_db_fixture)
    assert len(tasks) == 1
    assert tasks[0].title == "Test"


def test_create_task(mock_db_fixture: MagicMock, sample_task_schema: TaskSchema) -> None:
    mock_db_fixture.add.return_value = None
    mock_db_fixture.commit.return_value = None
    mock_db_fixture.refresh.return_value = None

    task = TaskService.create_task(mock_db_fixture, sample_task_schema)
    assert task.title == sample_task_schema.title


def test_get_task_by_id(mock_db_fixture: MagicMock, sample_task: Task) -> None:
    mock_db_fixture.query.return_value.filter.return_value.first.return_value = sample_task
    task = TaskService.get_task_by_id(mock_db_fixture, 1)
    assert task is not None and task.id == 1


def test_update_task(
    mock_db_fixture: MagicMock, sample_task: Task, sample_task_schema: TaskSchema
) -> None:
    mock_db_fixture.query.return_value.filter.return_value.first.return_value = sample_task
    updated_task = TaskService.update_task(mock_db_fixture, 1, sample_task_schema)
    assert updated_task is not None and updated_task.title == sample_task_schema.title


def test_delete_task(mock_db_fixture: MagicMock, sample_task: Task) -> None:
    mock_db_fixture.query.return_value.filter.return_value.first.return_value = sample_task
    result = TaskService.delete_task(mock_db_fixture, 1)
    assert result is not None
