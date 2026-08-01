# Django Todo App

A beginner-friendly Django task manager for creating todos, assigning them to people, and tracking completion status.

## Features

- Create and view todos with priority, deadline, and completion state
- Associate todos with people using a Django foreign key
- View a person's assigned todos
- Django admin support for managing application data
- Docker Compose setup for a repeatable local environment
- CSRF-protected complete/delete actions and a small automated test suite

## Run locally

```powershell
uv sync
cd tutProject
uv run manage.py migrate
uv run manage.py runserver
```

Open <http://127.0.0.1:8000/todos>.

Create people from the Django admin at <http://127.0.0.1:8000/admin/>; they will then be available in the todo owner dropdown.

## Run with Docker

After Docker Desktop is running:

```powershell
docker compose up --build
```

Open <http://localhost:8000/todos>. The SQLite database is stored in a named Docker volume, so it persists across container restarts. This Compose setup is intended for local development.

To stop the app, press `Ctrl+C`. To remove the container and its database volume:

```powershell
docker compose down --volumes
```

## Useful commands

```powershell
cd tutProject
uv run manage.py createsuperuser
uv run manage.py check
uv run manage.py makemigrations
uv run manage.py migrate
uv run manage.py test
```
