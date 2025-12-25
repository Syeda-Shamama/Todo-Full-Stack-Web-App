from sqlmodel import create_engine, SQLModel, Session
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get DATABASE_URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

# Validate DATABASE_URL exists
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is required")

# Create engine with proper PostgreSQL settings
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Log SQL queries (useful for debugging)
    pool_pre_ping=True,  # Verify connections before using
    pool_size=5,  # Number of connections to maintain
    max_overflow=10  # Max connections beyond pool_size
)

def create_db_and_tables():
    """Create all database tables"""
    print("Creating database tables...")
    SQLModel.metadata.create_all(engine)
    print("✅ Tables created successfully!")

def get_session():
    """
    Database session dependency for FastAPI.
    Properly manages session lifecycle.
    """
    with Session(engine) as session:
        yield session