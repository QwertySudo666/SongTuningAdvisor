my_guitar_app/
├── alembic/                  # Database migrations (if you modify tables later)
├── src/
│   ├── api/                  # Routers / Endpoints
│   │   ├── v1/
│   │   │   ├── api.py        # Aggregates all routers
│   │   │   └── endpoints/
│   │   │       ├── auth.py   # Registration, login, token generation
│   │   │       ├── songs.py  # Add song, get user's song list
│   │   │       └── stats.py  # Tuning statistics and string recommendations
│   │   └── deps.py           # FastAPI dependencies (e.g., get_current_user)
│   │
│   ├── core/                 # Config and database setup
│   │   ├── config.py         # Environment variables (secret keys, DB URL)
│   │   └── database.py       # SQLAlchemy session setup
│   │
│   ├── models/               # SQLAlchemy models (database tables)
│   │   ├── user.py           # Users table (id, email, hashed_password)
│   │   └── song.py           # Songs table (id, title, tuning, user_id)
│   │
│   ├── schemas/              # Pydantic schemas (JSON validation)
│   │   ├── user.py           # UserCreate, UserResponse
│   │   └── song.py           # SongCreate, SongResponse, StatsResponse
│   │
│   ├── repositories/         # Database operations (SQL/ORM queries)
│   │   ├── user_repository.py
│   │   └── song_repository.py # Contains GROUP BY tuning queries for specific user stats
│   │
│   ├── services/             # Business logic layer
│   │   ├── auth_service.py   # Password hashing, JWT generation
│   │   └── string_recommendation_service.py # Logic for string gauge & scale length advice
│   │
│   └── main.py               # FastAPI application entry point
│
├── .env                      # Local environment secrets (keys, DB credentials)
├── .gitignore
├── Dockerfile                # Ready for future server or AWS Lambda deployment
└── requirements.txt          # Dependencies (fastapi, uvicorn, sqlalchemy, pydantic, etc.)# SongTuningAdvisor
