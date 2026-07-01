from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def greet():
    return {
        "message": "good afternoon"
    }

@app.get('/student')
def students():
    return {
        "name": "John Doe",
        "city": "Kathua"
    }