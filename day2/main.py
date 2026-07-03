from fastapi import FastAPI, HTTPException

app = FastAPI()

students = [
    {"id": 1, "name": "Akhil", "course": "Python",  "city": "Hyderabad"},
    {"id": 2, "name": "Sai",   "course": "FastAPI", "city": "Vijaywada"},
    {"id": 3, "name": "Ravi",  "course": "SQL",     "city": "Guntur"   },
    {"id": 4, "name": "Kiran", "course": "Python",  "city": "Vizag"    },
    {"id": 5, "name": "Meena", "course": "FastAPI", "city": "Chennai"  }
]

@app.get('/')
def home():
    return {"message": "Welcome to the Student API"}

@app.get("/students")
def get_students():
    return students

@app.get("/students/topper")
def get_topper_student():
    return {
        "name": "Akhil",
        "rank": "topper"
    }

@app.get("/students/{student_id}")
def get_student_by_id(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code = 404, detail = "Student not found")
