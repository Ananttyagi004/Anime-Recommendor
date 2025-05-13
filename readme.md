#  Anime Recommendation API

A Django REST API that allows user registration, login with JWT authentication, saving anime genre preferences, and fetching anime suggestions using the AniList GraphQL API.

---

##  Features

- JWT-based User Authentication
- Save and update anime genre preferences
- Fetch anime recommendations using AniList GraphQL API
- Built with Django REST Framework

---

##  Getting Started

###  Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)
- PostgreSQL or CockroachDB

---

## ⚙️ Local Setup Instructions

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/your-repo.git
cd your-repo
````

### 2️⃣ Create and Activate Virtual Environment

```
python -m venv env
source env/bin/activate  
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

##  CockroachDB Setup (PostgreSQL-Compatible)

### Install CockroachDB:

```
brew install cockroach  
```

Or [download manually](https://www.cockroachlabs.com/docs/stable/install-cockroachdb.html)

### Start a single-node cluster:

```
cockroach start-single-node --insecure --listen-addr=localhost:26257 --http-addr=localhost:8080
```

### Create a database and user:

```
cockroach sql --insecure
```

Inside the shell:

```sql
CREATE DATABASE anime_db;
CREATE USER anime_user WITH PASSWORD 'yourpassword';
GRANT ALL ON DATABASE anime_db TO anime_user;
```

### Add to `.env`:

```env
SECRET_KEY=your_secret_key_here
DEBUG=True
DATABASE_URL=postgresql://anime_user:yourpassword@localhost:26257/anime_db?sslmode=disable
```

---

## 🧱 Migrations

```
python manage.py migrate
```

---

## 🖥️ Run the Development Server

```
python manage.py runserver
```

---

## 📬 REST API Endpoints

###  Register User

curl --location 'http://localhost:8000/user/register/' \
--header 'Content-Type: application/json' \
--data-raw '{
  "username": "testuser",
  "email": "test@example.com",
  "password": "strongpassword123"
}'

#### Response:

```json
{
  "msg": "User Created",
  "token": {
    "refresh": "jwt_refresh_token",
    "access": "jwt_access_token"
  }
}
```

---

###  Login User

curl --location 'http://localhost:8000/user/login/' \
--header 'Content-Type: application/json' \
--data '{
  "username": "testuser",
  "password": "strongpassword123"
}'
#### Response:

```json
{
  "msg": "Login Success!",
  "token": {
    "refresh": "jwt_refresh_token",
    "access": "jwt_access_token"
  }
}
```

---

###  Save Genre Preference

*curl --location 'http://localhost:8000/user/preference/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ3NzYxMTkxLCJpYXQiOjE3NDcxNTYzOTEsImp0aSI6IjNlMDY4Y2JjYzcwYTRjOTliMzNhMDI5NmE5ZjZhZDI5IiwidXNlcl9pZCI6MTA3MTc5NDUwNzg2ODE0MzYxN30.6hwZEM1fK457EA5lEZwva0WmDJBuZ6KnNKNSN0CMLws' \
--header 'Content-Type: application/json' \
--data '{
  "prefrence": ["anime, action, drama"]
}'

#### Response:

```json
{
  "message": "Preference saved"
}
```

---

### Get Anime Suggestions

curl --location --request POST 'http://localhost:8000/anime/recommendations/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ3NzYxMTkxLCJpYXQiOjE3NDcxNTYzOTEsImp0aSI6IjNlMDY4Y2JjYzcwYTRjOTliMzNhMDI5NmE5ZjZhZDI5IiwidXNlcl9pZCI6MTA3MTc5NDUwNzg2ODE0MzYxN30.6hwZEM1fK457EA5lEZwva0WmDJBuZ6KnNKNSN0CMLws'

#### Response:

```json
{
  "data": {
    "Page": {
      "media": [
        {
          "id": 11061,
          "title": {
            "romaji": "Hunter x Hunter (2011)",
            "english": "Hunter x Hunter",
            "native": "ハンター×ハンター"
          },
          "genres": [
            "Action",
            "Adventure",
            "Fantasy"
          ]
        },
        {
          "id": 9253,
          "title": {
            "romaji": "Steins;Gate",
            "english": "Steins;Gate",
            "native": "シュタインズ・ゲート"
          },
          "genres": [
            "Sci-Fi",
            "Drama",
            "Thriller"
          ]
        }
      ]
    }
  }
}
```

---

### Search Anime
curl --location 'http://localhost:8000/anime/search/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ3NzYxMTkxLCJpYXQiOjE3NDcxNTYzOTEsImp0aSI6IjNlMDY4Y2JjYzcwYTRjOTliMzNhMDI5NmE5ZjZhZDI5IiwidXNlcl9pZCI6MTA3MTc5NDUwNzg2ODE0MzYxN30.6hwZEM1fK457EA5lEZwva0WmDJBuZ6KnNKNSN0CMLws' \
--data '{
  "search": "Naruto",
  "genre": "Action"
}'

#### Response 
```json
{
  "status": "success",
  "message": "Anime recommendations fetched successfully",
  "data": [
    {
      "id": 20,
      "title": {
        "romaji": "NARUTO",
        "english": "Naruto",
        "native": "NARUTO -ナルト-"
      },
      "genres": ["Action", "Adventure", "Comedy", "Drama", "Fantasy", "Supernatural"]
    },
    {
      "id": 21220,
      "title": {
        "romaji": "BORUTO: NARUTO THE MOVIE",
        "english": "Boruto: Naruto the Movie",
        "native": "BORUTO -NARUTO THE MOVIE-"
      },
      "genres": ["Action", "Adventure", "Comedy"]
    },
    {
      "id": 3480,
      "title": {
        "romaji": "Nayuta",
        "english": "Nayuta",
        "native": "那由他"
      },
      "genres": ["Action", "Sci-Fi"]
    },
    {
      "id": 6000,
      "title": {
        "romaji": "Haruwo",
        "english": null,
        "native": "ハルヲ"
      },
      "genres": ["Action", "Sci-Fi"]
    },
    {
      "id": 97938,
      "title": {
        "romaji": "BORUTO: NARUTO NEXT GENERATIONS",
        "english": "Boruto: Naruto Next Generations",
        "native": "BORUTO-ボルト- NARUTO NEXT GENERATIONS"
      },
      "genres": ["Action", "Adventure", "Fantasy"]
    }
    
  ]
}
'''