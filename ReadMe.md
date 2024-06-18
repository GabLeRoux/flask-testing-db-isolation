## Flask Project with Docker and PostgreSQL

This project sets up a Flask application with Docker and PostgreSQL, including an isolated testing environment. Environment variables are configured to switch between development and test databases.

### Project Structure

```
flask_project/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── routes.py
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_routes.py
├── docker/
│   ├── flask/
│   │   ├── Dockerfile
│   │   └── init-db.sh
├── .gitignore
├── docker-compose.yml
├── manage.py
├── requirements.in
├── requirements.txt
└── README.md
```

### Setup and Installation

#### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

#### Installation Steps

1. **Build and run the Docker containers:**

   ```sh
   docker-compose up --build
   ```

2. **Run the tests:**

   ```sh
   docker-compose run web python -m unittest discover -s app/tests
   ```

### Project Details

- **Docker Compose** is used to manage the multi-container application, including the Flask app and PostgreSQL database.
- **Flask-SQLAlchemy** is used for ORM (Object-Relational Mapping) to handle database operations.
- **psycopg2-binary** is used as the PostgreSQL database adapter for Python.
- **Environment Configuration** allows switching between development and test databases using environment variables.
