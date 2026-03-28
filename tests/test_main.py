from fastapi.testclient import TestClient
from app.main import app, students, next_id 

client = TestClient(app)


def setup_function():
    students.clear
    import app.main as m 
    m.next_id = 1

def test_get_students_empty():
    response = client.get("/students")
    assert response.status_code == 200
    assert response.json() == {}

def test_add_student():
    response = client.post("/students", json={"username": "amzazi", "grade": 18.5})
    assert response.status_code == 201
    assert response.json()["student"]["username"] == "amzazi"


def test_get_student():
    client.post("/students", json={"username": "amzazi", "grade": 18.5})
    response = client.get("/students/1")
    assert response.status_code == 200
    assert response.json()["username"] == "amzazi"

def test_get_student_not_found():
    response = client.get("/students/999")
    assert response.status_code == 404

