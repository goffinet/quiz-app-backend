from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ....schemas import UserCreate, User
from ....crud import get_user, create_user
from ....database import get_db

router = APIRouter()

@router.post("/", response_model=User)
async def create_user_endpoint(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await get_user(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await create_user(db=db, user=user)

@router.get("/{user_id}", response_model=User)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
