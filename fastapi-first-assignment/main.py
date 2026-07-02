from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    return {
        "message": "Welcome to my first FastAPI assignment"
     }

@app.get('/about')
def about():
    return {
        "student_name": "Bharat Lashotra",
        "course_name": "FastAPI",
        "topic": "First API Assignment",
        "status": "Learning"
    }

@app.get('/trainer')
def get_trainer():
    return {
        "name": "Hemanth",
        "role": "Trainer",
        "subject": "FastAPI"
    }

@app.get('/courses')
def get_courses():
    return [
        {
            "id": 1,
            "name": "Python Basics",
            "duration": "1 week"
        }, 
        {
            "id": 2,
            "name": "FastAPI",
            "duration": "2 weeks"
        }, 
        {
            "id": 3,
            "name": "SQL Basics",
            "duration": "1 week"
        }

    ]
@app.get('/students')
def get_students():
    return [
        {
            "id": 1,
            "namw": "Akhil",
            "course": "Python",
            "city": "Hyderabad"
        },
        {
            "id": 2,
            "name": "Sai",
            "course": "FastAPI",
            "city": "Vijayawada"
        }
    ]

@app.get('/college')
def get_college():
    return {
        "college_name": "MIET",
        "location": "Jammu",
        "department": "CSE",
        "current_module": "FastAPI Basics"
    }


@app.get('/technologies')
def get_technology():
    return [
        "Python",
        "FastAPI",
        "JSON",
        "HTTP",
        "Rest API"
    ]

@app.get('/students/{student_id}')
def get_student_by_id(student_id: int):
    return {
        'student_id': student_id,
        'message': "Learning Dynamic URL's"
    }

@app.get('/courses/{course_id}')
def get_course_by_id(course_id: str):
    return {
        "course_id": course_id,
        "message": f"Successfully loaded the course details with id = {course_id}"
    }



@app.get('/books/{book_id}/author/{author_id}')
def get_book_by_author_idk(book_id: int, author_id: int):
    return {
        "Book_id": book_id,
        "author_id": author_id
    }