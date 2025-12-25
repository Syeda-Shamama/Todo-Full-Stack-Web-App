# Database Schema

## Database: Neon Serverless PostgreSQL

## Connection
- Use SQLModel for ORM
- Connection string in environment variable: `DATABASE_URL`
- Format: `postgresql://user:password@host:5432/dbname`

## Tables

### users
Managed by Better Auth - do not modify directly

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | VARCHAR(255) | PRIMARY KEY | Unique user identifier (UUID) |
| email | VARCHAR(255) | UNIQUE, NOT NULL | User email address |
| name | VARCHAR(255) | NOT NULL | User's full name |
| password | VARCHAR(255) | NOT NULL | Hashed password |
| created_at | TIMESTAMP | DEFAULT NOW() | Account creation time |
| updated_at | TIMESTAMP | DEFAULT NOW() | Last update time |

---

### tasks

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Unique task identifier |
| user_id | VARCHAR(255) | FOREIGN KEY (users.id), NOT NULL | Owner of the task |
| title | VARCHAR(200) | NOT NULL | Task title |
| description | TEXT | NULL | Optional task description |
| completed | BOOLEAN | DEFAULT FALSE | Completion status |
| created_at | TIMESTAMP | DEFAULT NOW() | Task creation time |
| updated_at | TIMESTAMP | DEFAULT NOW() | Last update time |

**Indexes:**
- `idx_tasks_user_id` on `user_id` (for fast filtering by user)
- `idx_tasks_completed` on `completed` (for status filtering)

**Foreign Key:**
- `user_id` REFERENCES `users(id)` ON DELETE CASCADE

---

## SQLModel Models

### User Model (Read-Only)
```python
from sqlmodel import SQLModel, Field
from datetime import datetime

class User(SQLModel, table=True):
    __tablename__ = "users"
    
    id: str = Field(primary_key=True)
    email: str = Field(unique=True, index=True)
    name: str
    password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
```

### Task Model
```python
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class Task(SQLModel, table=True):
    __tablename__ = "tasks"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(foreign_key="users.id", index=True)
    title: str = Field(max_length=200)
    description: Optional[str] = None
    completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
```

---

## Database Migrations
- Use Alembic for migrations (optional for Phase II)
- Or use SQLModel's `SQLModel.metadata.create_all(engine)` for simple setup

## Data Validation Rules
- `title`: 1-200 characters, required
- `description`: 0-1000 characters, optional
- `email`: Valid email format, unique
- `password`: Minimum 8 characters (enforced by Better Auth)

## Sample Data (for testing)
```sql
-- User (created by Better Auth)
INSERT INTO users (id, email, name, password, created_at, updated_at)
VALUES ('user-123', 'test@example.com', 'Test User', 'hashed_password', NOW(), NOW());

-- Tasks
INSERT INTO tasks (user_id, title, description, completed, created_at, updated_at)
VALUES 
  ('user-123', 'Buy groceries', 'Milk, eggs, bread', false, NOW(), NOW()),
  ('user-123', 'Finish project', 'Complete Phase II', true, NOW(), NOW());
```

## Backup and Recovery
- Neon provides automatic backups
- Test restore procedure before production