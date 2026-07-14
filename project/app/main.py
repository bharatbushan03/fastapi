from fastapi import FastAPI
from routers.book_routers import router

app = FastAPI(
    title='Library API',
    description = 'A modular FastAPI CRUD application',
    version = '1.0.0'
)

app.include_router(router)

@app.get('/', tags=['Root'])
def home():
    return {"message": "Welcome to Library API"}