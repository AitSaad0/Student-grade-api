from fastapi import FastAPI, HTTPException
from .models import Student


app = FastAPI()

students: dict[int, Student] = {}
next_id = 1

@app.get("/students")
def get_students():
    return students


@app.post("/students", status_code=201)
def add_student(student: Student):
    global next_id
    students[next_id] = student 
    next_id += 1
    return {"id": next_id - 1, "student": student}


@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students: 
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id] 