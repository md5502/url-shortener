# URL Shortener API

A RESTful API service for shortening long URLs. This API allows users to create, retrieve, update, and delete short URLs, and also provides statistics on the number of times a short URL has been accessed.

## Project Structure

```bash
.
├── api
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_url_full_url.py
│   │   ├── 0003_alter_url_counter.py
│   │   ├── 0004_alter_url_counter.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── config
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── docker-compose.yml
├── manage.py
├── requirements.txt
└── ruff.toml
```

## Features

- Create a new short URL
- Retrieve the original URL from a short URL
- Update an existing short URL
- Delete an existing short URL
- Track and retrieve the number of times a short URL has been accessed

## API Endpoints

1. **Create Short URL**  
   `POST /shorten`  
   Request:
   ```json
   {
     "url": "https://www.example.com/some/long/url"
   }
   ```

   Response:
   ```json
   {
     "id": "1",
     "url": "https://www.example.com/some/long/url",
     "shortCode": "abc123",
     "createdAt": "2021-09-01T12:00:00Z",
     "updatedAt": "2021-09-01T12:00:00Z"
   }
   ```

2. **Retrieve Original URL**  
   `GET /shorten/{shortCode}`  
   Response:
   ```json
   {
     "id": "1",
     "url": "https://www.example.com/some/long/url",
     "shortCode": "abc123",
     "createdAt": "2021-09-01T12:00:00Z",
     "updatedAt": "2021-09-01T12:00:00Z"
   }
   ```

3. **Update Short URL**  
   `PUT /shorten/{shortCode}`  
   Request:
   ```json
   {
     "url": "https://www.example.com/some/updated/url"
   }
   ```

4. **Delete Short URL**  
   `DELETE /shorten/{shortCode}`

5. **Get URL Statistics**  
   `GET /shorten/{shortCode}/stats`  
   Response:
   ```json
   {
     "id": "1",
     "url": "https://www.example.com/some/long/url",
     "shortCode": "abc123",
     "createdAt": "2021-09-01T12:00:00Z",
     "updatedAt": "2021-09-01T12:00:00Z",
     "accessCount": 10
   }
   ```

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