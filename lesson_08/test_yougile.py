import os
from dotenv import load_dotenv
from project_api import ProjectApi
from faker import Faker


fake = Faker()
load_dotenv()
api = ProjectApi("https://ru.yougile.com/api-v2")


def test_get_project():
    body = api.get_projects_list(token=os.getenv("TOKEN"))
    assert len(body) > 0


def test_new_project_positive():
    token = os.getenv("TOKEN")
    title = fake.word()
    users = {"c1d0a8ad-c24d-4de7-935b-06149d8873dc": "admin"}
    result = api.create_project(token, title, users)

    assert "id" in result
    new_id = result["id"]
    created_project = api.get_project(token, new_id)
    assert created_project["title"] == title


def test_new_project_negative():
    token = os.getenv("TOKEN")
    title = ""
    users = {"c1d0a8ad-c24d-4de7-935b-06149d8873dc": "admin"}
    response = api.create_project_raw(token, title, users)

    assert response.status_code == 400
    body = response.json()
    assert body["error"] == "Bad Request"
    assert "title should not be empty" in body["message"]


def test_edit_positive():
    token = os.getenv("TOKEN")
    title = fake.word()
    users = {"c1d0a8ad-c24d-4de7-935b-06149d8873dc": "admin"}
    result = api.create_project(token, title, users)
    new_id = result["id"]

    new_title = fake.word()

    edited = api.edit_project(token, new_id, new_title)
    assert "id" in edited
    new_id = edited["id"]


def test_edit_negative():
    token = os.getenv("TOKEN")
    fake_id = "00000000-0000-0000-0000-000000000000"
    new_title = fake.word()
    response = api.edit_project_raw(token, fake_id, new_title)

    assert response.status_code == 404
    body = response.json()
    assert body["error"] == "Not Found"
    assert "Проект не найден" in body["message"]


def test_get_project_by_id_positive():
    token = os.getenv("TOKEN")
    title = fake.word()
    users = {"c1d0a8ad-c24d-4de7-935b-06149d8873dc": "admin"}
    result = api.create_project(token, title, users)
    new_id = result["id"]

    response = api.get_project(token, new_id)
    assert "id" in response
    new_id = response["id"]
    assert title == response["title"]
    assert users == response["users"]


def test_get_project_by_id_negative():
    fake_token = ""
    id = "a10de812-b1ae-4102-b8f8-563c8b840422"
    response = api.get_project_raw(fake_token, id)

    assert response.status_code == 401
    body = response.json()
    assert body["error"] == "Unauthorized"
    assert "Unauthorized" in body["message"]
