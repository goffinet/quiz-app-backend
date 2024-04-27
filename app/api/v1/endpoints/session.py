from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from ....schemas import SessionCreate, SessionRead
from ....crud import create_quiz_session, get_quiz_session
from ....database import get_db

router = APIRouter()

@router.post("/", response_model=SessionRead)
async def create_session(session_data: SessionCreate, db: AsyncSession = Depends(get_db)):
    """
    Create a new quiz session with the provided session data.
    """
    session = await create_quiz_session(db, session_data=session_data)
    if not session:
        raise HTTPException(status_code=404, detail="Failed to create the session")
    return session

@router.get("/{session_id}", response_model=SessionRead)
async def read_session(session_id: int, db: AsyncSession = Depends(get_db)):
    """
    Retrieve a specific quiz session by its ID.
    """
    session = await get_quiz_session(db, session_id=session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session
