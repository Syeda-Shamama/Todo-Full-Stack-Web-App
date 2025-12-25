# System Architecture

## Overview
Monorepo containing separate frontend and backend applications that communicate via REST API.

## Architecture Diagram
```
┌─────────────────┐
│   Browser       │
│  (Next.js UI)   │
└────────┬────────┘
         │ HTTP + JWT
         ▼
┌─────────────────┐
│  FastAPI        │
│  REST API       │
└────────┬────────┘
         │ SQLModel
         ▼
┌─────────────────┐
│  Neon PostgreSQL│
│  Database       │
└─────────────────┘
```

## Component Responsibilities

### Frontend (Next.js)
- User interface and interaction
- Better Auth integration (login/signup)
- JWT token management
- API calls to backend
- Client-side routing

### Backend (FastAPI)
- REST API endpoints
- JWT token verification
- Business logic
- Database operations via SQLModel
- User authorization

### Database (Neon PostgreSQL)
- User data storage
- Task data storage
- Persistent storage across sessions

## Authentication Flow
1. User signs up/logs in via Better Auth
2. Better Auth issues JWT token
3. Frontend stores token
4. Frontend includes token in all API requests
5. Backend verifies token and extracts user ID
6. Backend filters data by authenticated user

## Data Flow
```
User Action → Frontend → API Request + JWT → Backend → Verify JWT → Database Query → Response → Frontend → Update UI
```

## Security
- All API endpoints require valid JWT
- User data isolated by user_id
- Passwords hashed by Better Auth
- CORS configured properly
- Environment variables for secrets