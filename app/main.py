from fastapi import FastAPI
from .api.v1.endpoints import users, quiz, session
from .database import engine, Base

app = FastAPI()

# Import all models (This could be done dynamically if there are many)
from .models import User, Quiz, Question, QuizSession

# Create database tables
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(quiz.router, prefix="/quiz", tags=["quiz"])
app.include_router(session.router, prefix="/session", tags=["session"])
