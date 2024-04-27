from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from ....schemas import QuizCreate, QuizRead
from ....crud import create_quiz, get_quiz
from ....database import get_db

router = APIRouter()

@router.post("/", response_model=QuizRead)
async def create_quiz_endpoint(quiz_data: QuizCreate, db: AsyncSession = Depends(get_db)):
    """
    Create a new quiz with the provided quiz data.
    """
    quiz = await create_quiz(db, quiz_data=quiz_data)
    if not quiz:
        raise HTTPException(status_code=404, detail="Failed to create the quiz")
    return quiz

@router.get("/{quiz_id}", response_model=QuizRead)
async def read_quiz(quiz_id: int, db: AsyncSession = Depends(get_db)):
    """
    Retrieve a specific quiz by its ID.
    """
    quiz = await get_quiz(db, quiz_id=quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz
