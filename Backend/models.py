from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ============= USER MODEL =============
# NOTE: In production, Better Auth manages users on frontend
# This model is for backend testing and JWT verification only
class User(SQLModel, table=True):
    __tablename__ = "users"
    
    id: str = Field(primary_key=True)
    email: str = Field(unique=True, index=True)
    name: str
    password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def set_password(self, password: str):
        """Hash and set password - for testing only"""
        self.password = pwd_context.hash(password)

    def verify_password(self, password: str) -> bool:
        """Verify password - for testing only"""
        return pwd_context.verify(password, self.password)


# ============= TASK MODELS =============
# Database Model
class Task(SQLModel, table=True):
    __tablename__ = "tasks"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(foreign_key="users.id", index=True)
    title: str = Field(max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = Field(default=False, index=True)  # Index for filtering
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# API Request Models
class TaskCreate(SQLModel):
    """Model for creating a new task"""
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)


class TaskUpdate(SQLModel):
    """Model for updating an existing task"""
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)


class TaskToggle(SQLModel):
    """Model for toggling task completion"""
    completed: bool


# API Response Model (optional, can use Task directly)
class TaskRead(SQLModel):
    """Model for task responses"""
    id: int
    user_id: str
    title: str
    description: Optional[str]
    completed: bool
    created_at: datetime
    updated_at: datetime