import pytest
from .conftest import client, db_session
from app.crud import create_quiz

def test_create_quiz(client, db_session):
    quiz_data = {"title": "Test Quiz", "is_public": True}
    response = client.post("/api/v1/quiz/", json=quiz_data)
    assert response.status_code == 200
    assert response.json()['title'] == "Test Quiz"

def test_get_quiz(client, db_session):
    quiz = create_quiz(db_session, {"title": "New Quiz", "is_public": True})
    db_session.commit()
    response = client.get(f"/api/v1/quiz/{quiz.id}")
    assert response.status_code == 200
    assert response.json()['id'] == quiz.id
