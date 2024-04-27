from sqlalchemy.orm import Session
from .models import User, Quiz, Question, QuizSession

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_quiz(db: Session, quiz_data: dict):
    quiz = Quiz(title=quiz_data['title'], is_public=quiz_data['is_public'])
    db.add(quiz)
    db.commit()
    db.refresh(quiz)
    return quiz

def create_question(db: Session, question_data: dict, quiz_id: int):
    question = Question(text=question_data['text'], answer=question_data['answer'], quiz_id=quiz_id)
    db.add(question)
    db.commit()
    db.refresh(question)
    return question

def create_session(db: Session, session_data: dict, quiz_id: int):
    session = QuizSession(quiz_id=quiz_id, scheduled_time=session_data['scheduled_time'], number_of_retakes=session_data['number_of_retakes'])
    db.add(session)
    db.commit()
    db.refresh(session)
    return session
