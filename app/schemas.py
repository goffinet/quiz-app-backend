from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class QuizBase(BaseModel):
    title: str
    is_public: bool = True

class QuizCreate(QuizBase):
    pass

class Quiz(QuizBase):
    id: int
    questions: List['Question'] = []

    class Config:
        orm_mode = True

class QuestionBase(BaseModel):
    text: str
    answer: str

class QuestionCreate(QuestionBase):
    pass

class Question(QuestionBase):
    id: int

    class Config:
        orm_mode = True

class SessionBase(BaseModel):
    scheduled_time: datetime
    number_of_retakes: int = 1

class SessionCreate(SessionBase):
    pass

class Session(SessionBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

Quiz.update_forward_refs()
