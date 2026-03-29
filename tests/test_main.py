from fastapi.testclient import TestClient
from app.main import app, students

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

def test_delete_student():
    client.post("/students", json={"username": "amzazi", "grade": 18.5})
    response = client.delete("/students/1")
    assert response.status_code == 204

def test_delete_student_not_found():
    response = client.delete("/students/999")
    assert response.status_code == 404

def test_update_student():
    client.post("/students", json={"username": "amzazi", "grade": 18.5})
    response = client.put("/students/1", json={"username": "amzazi_updated", "grade": 19.0})
    assert response.status_code == 200
    assert response.json()["student"]["username"] == "amzazi_updated"

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

