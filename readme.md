# URL Shortener API

A RESTful API service for shortening long URLs. This API allows users to create, retrieve, update, and delete short URLs, and also provides statistics on the number of times a short URL has been accessed.
and for the faster and experian use cache system
## Project Structure

```bash
.
├── api
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tasks.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── config
│   ├── asgi.py
│   ├── celery.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── docker-compose.yml
├── dockerfile
├── Makefile
├── manage.py
├── readme.md
├── requirements.txt
├── ruff.toml
└── schema.yml
```

## Features

- Create a new short URL
- Retrieve the original URL from a short URL
- Update an existing short URL
- Delete an existing short URL
- Track and retrieve the number of times a short URL has been accessed


## Tech Stack

- **Backend Framework:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Cache:** Redis
- **Containerization:** Docker, Docker Compose

## Docker Setup

To set up and run the project using Docker, follow these steps:

1. **Build the Docker containers:**

   Run the following command to build and start the containers:
   ```bash
    docker compose -f docker-compose.yml up -d
   ```

2. **Access the API:**

   The API will be available at `http://localhost:8000`.
   swagger ui `http://localhost:8000/api/schema/swagger-ui/`.
   redoc ui `http://localhost:8000/api/schema/redocs/`.

3. **Shut down the containers:**

   To stop the containers, use:
   ```bash
   docker-compose down
   ```

## Virtualenv Setup

If you prefer to run the project locally without Docker, you can use Python's virtual environment.

1. **Create a virtual environment:**

   Run the following command to create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment:**

   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```

3. **Install dependencies:**

   With the virtual environment activated, install the project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   Run the following commands to set up the database:
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**

   Start the server by running:
   ```bash
   python manage.py runserver
   ```

6. **Deactivate the virtual environment:**

   When you're done, deactivate the virtual environment by running:
   ```bash
   deactivate
   ```

## Environment Variables

The following environment variables are required in the `docker-compose.yml` file:

- `POSTGRES_DB=urlshorter`
- `POSTGRES_USER=user`
- `POSTGRES_PASSWORD=password`

## How to Run Tests

To run the tests, execute:
```bash
python manage.py test
```
### Contribution and Development Status

This project is currently **under development**. Contributions are welcome to help improve and extend its functionality. If you're interested in contributing, feel free to reach out to discuss ideas, report issues, or collaborate on new features.

📧 **Contact Email:** [m.baniasadi.d@gmail.com](mailto:m.baniasadi.d@gmail.com)

I look forward to your contributions! 😊