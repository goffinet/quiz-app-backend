from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)

class Quiz(Base):
    __tablename__ = 'quizzes'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    is_public = Column(Boolean, default=True)
    questions = relationship("Question", back_populates="quiz")

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'))
    text = Column(String)
    answer = Column(String)
    quiz = relationship("Quiz", back_populates="questions")

class QuizSession(Base):
    __tablename__ = 'quiz_sessions'
    id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'))
    scheduled_time = Column(DateTime)
    number_of_retakes = Column(Integer, default=1)
    is_active = Column(Boolean, default=True)
    quiz = relationship("Quiz", back_populates="sessions")

Quiz.sessions = relationship("QuizSession", order_by=QuizSession.id, back_populates="quiz")
