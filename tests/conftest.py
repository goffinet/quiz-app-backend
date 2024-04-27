import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.main import app
from fastapi.testclient import TestClient

@pytest.fixture(scope="session")
def db_engine():
    engine = create_engine("sqlite:///./test_database.db")
    Base.metadata.create_all(engine)
    return engine

@pytest.fixture(scope="function")
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    session = sessionmaker(bind=connection)()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c
