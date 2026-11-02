
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working"}

@app.get("/students")
def students():
    return {
        "students": [
            {
                "id": 1,
                "name": "Rahul",
                "marks": 85
            },
            {
                "id": 2,
                "name": "Priya",
                "marks": 92
            }
        ]
    }
data=[
  {
    "id": 1,
    "name": "Rahul Sharma",
    "age": 20,
    "gender": "Male",
    "course": "B.Tech",
    "branch": "CSE",
    "marks": 85.5,
    "city": "Indore"
  },
  {
    "id": 2,
    "name": "Priya Verma",
    "age": 21,
    "gender": "Female",
    "course": "B.Tech",
    "branch": "AI & ML",
    "marks": 92.0,
    "city": "Bhopal"
  },
  {
    "id": 3,
    "name": "Aman Patel",
    "age": 19,
    "gender": "Male",
    "course": "BCA",
    "branch": "Computer Applications",
    "marks": 78.5,
    "city": "Jabalpur"
  },
  {
    "id": 4,
    "name": "Sneha Gupta",
    "age": 20,
    "gender": "Female",
    "course": "B.Tech",
    "branch": "IT",
    "marks": 88.0,
    "city": "Gwalior"
  },
  {
    "id": 5,
    "name": "Arjun Singh",
    "age": 22,
    "gender": "Male",
    "course": "MCA",
    "branch": "Computer Science",
    "marks": 74.5,
    "city": "Ujjain"
  }
]
@app.get("/students/{student_id}")
def get_id(student_id: int):
    for student in data:
        if student["id"] == student_id:
            return student
  
    return {"message": "Student not found"}
