from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_task() -> None:
    response = client.post(
        "/tasks/",
        json={"title": "New Task", "description": "Test", "completed": False},
    )
    assert response.status_code == 200
    assert response.json()["title"] == "New Task"


def test_get_tasks() -> None:
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_task_not_found() -> None:
    response = client.get("/tasks/9999/")
    assert response.status_code == 404


def test_delete_task() -> None:
    response = client.post(
        "/tasks/",
        json={"title": "Task to Delete", "description": "Delete", "completed": False},
    )
    task_id = response.json()["id"]
    delete_response = client.delete(f"/tasks/{task_id}/")
    assert delete_response.status_code == 200
