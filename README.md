# Quiz App Backend

## Overview
This project is the backend for a quiz application built with FastAPI. It supports features like user authentication, quiz management, and session scheduling.

## Features
- User management: Create, retrieve, update, and delete users.
- Quiz management: Admins can create, retrieve, update, and delete quizzes.
- Session management: Schedule quiz sessions with attributes like retakes and timing configurations.

## Requirements
- Python 3.8 or newer
- FastAPI
- Uvicorn: ASGI server for running FastAPI
- SQLAlchemy: ORM for database interactions
- Alembic: For database migrations
- Pydantic: For data validation through Python dataclasses
- PostgreSQL: For the production database

## Setup and Installation
1. Clone the repository:
    ```
    git clone https://github.com/yourrepository/quiz-app-backend.git
    ```
2. Navigate to the project directory:
    ```bash
    cd quiz-app-backend
    ```
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Create and configure your `.env` file with necessary environment variables:
    ```
    DATABASE_URL=postgresql://user:password@localhost/dbname
    SECRET_KEY=your_secret_key_here
    ```
5. Run the Alembic migrations to set up your database schema:
    ```
    alembic upgrade head
    ```
6. Start the application using Uvicorn:
    ```
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```

## Testing
To run the tests, use the following command:
    ```
    pytest
    ```

## Deployment
1. Ensure all sensitive data is secured in environment variables.
2. Set up a Docker container for the application using the provided `Dockerfile`.
3. Deploy using a WSGI server like Gunicorn and a reverse proxy like Nginx:
    ```
    gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
    ```
4. Consider using Docker Compose for managing service configurations:
    ```
    docker-compose up --build
    ```

## Support
For any queries or technical support, please open an issue on the project's GitHub page.

Thank you for using the Quiz App Backend!