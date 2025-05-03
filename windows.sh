export DATABASE_URL=sqlite:///./sqlite.db

uvicorn src.main:server --reload