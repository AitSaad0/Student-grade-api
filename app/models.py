from pydantic import BaseModel

class Student(BaseModel):
    username: str
    grade: float