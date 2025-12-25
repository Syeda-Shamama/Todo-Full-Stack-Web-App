# REST API Endpoints

## Base URL
- Development: `http://localhost:8000`
- Production: `https://api.yourdomain.com`

## Authentication
All endpoints (except health check) require JWT token in header:
```
Authorization: Bearer <jwt_token>
```

## Response Format
### Success Response
```json
{
  "data": { ... },
  "message": "Success"
}
```

### Error Response
```json
{
  "error": "Error message",
  "detail": "Detailed error description"
}
```

## Endpoints

### Health Check
```
GET /health
```
**Description:** Check if API is running  
**Auth Required:** No  
**Response:**
```json
{
  "status": "ok",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

---

### List All Tasks
```
GET /api/{user_id}/tasks
```
**Description:** Get all tasks for authenticated user  
**Auth Required:** Yes  
**Path Parameters:**
- `user_id` (string): User ID from JWT token

**Query Parameters:**
- `status` (optional): "all" | "pending" | "completed" (default: "all")
- `sort` (optional): "created" | "title" | "updated" (default: "created")

**Response:** `200 OK`
```json
{
  "data": [
    {
      "id": 1,
      "user_id": "uuid",
      "title": "Buy groceries",
      "description": "Milk, eggs, bread",
      "completed": false,
      "created_at": "2024-01-15T10:00:00Z",
      "updated_at": "2024-01-15T10:00:00Z"
    }
  ]
}
```

**Errors:**
- `401 Unauthorized`: Invalid or missing JWT token
- `403 Forbidden`: user_id in URL doesn't match JWT token

---

### Create New Task
```
POST /api/{user_id}/tasks
```
**Description:** Create a new task  
**Auth Required:** Yes  
**Path Parameters:**
- `user_id` (string): User ID from JWT token

**Request Body:**
```json
{
  "title": "Task title",
  "description": "Optional description"
}
```

**Response:** `201 Created`
```json
{
  "data": {
    "id": 1,
    "user_id": "uuid",
    "title": "Task title",
    "description": "Optional description",
    "completed": false,
    "created_at": "2024-01-15T10:00:00Z",
    "updated_at": "2024-01-15T10:00:00Z"
  }
}
```

**Errors:**
- `400 Bad Request`: Invalid input (title missing or too long)
- `401 Unauthorized`: Invalid JWT
- `403 Forbidden`: user_id mismatch

---

### Get Task Details
```
GET /api/{user_id}/tasks/{id}
```
**Description:** Get details of a specific task  
**Auth Required:** Yes  
**Path Parameters:**
- `user_id` (string): User ID from JWT token
- `id` (integer): Task ID

**Response:** `200 OK`
```json
{
  "data": {
    "id": 1,
    "user_id": "uuid",
    "title": "Task title",
    "description": "Description",
    "completed": false,
    "created_at": "2024-01-15T10:00:00Z",
    "updated_at": "2024-01-15T10:00:00Z"
  }
}
```

**Errors:**
- `404 Not Found`: Task doesn't exist or doesn't belong to user
- `401 Unauthorized`: Invalid JWT
- `403 Forbidden`: user_id mismatch

---

### Update Task
```
PUT /api/{user_id}/tasks/{id}
```
**Description:** Update an existing task  
**Auth Required:** Yes  
**Path Parameters:**
- `user_id` (string): User ID from JWT token
- `id` (integer): Task ID

**Request Body:**
```json
{
  "title": "Updated title",
  "description": "Updated description"
}
```

**Response:** `200 OK`
```json
{
  "data": {
    "id": 1,
    "user_id": "uuid",
    "title": "Updated title",
    "description": "Updated description",
    "completed": false,
    "created_at": "2024-01-15T10:00:00Z",
    "updated_at": "2024-01-15T11:00:00Z"
  }
}
```

**Errors:**
- `400 Bad Request`: Invalid input
- `404 Not Found`: Task doesn't exist or doesn't belong to user
- `401 Unauthorized`: Invalid JWT
- `403 Forbidden`: user_id mismatch

---

### Delete Task
```
DELETE /api/{user_id}/tasks/{id}
```
**Description:** Delete a task permanently  
**Auth Required:** Yes  
**Path Parameters:**
- `user_id` (string): User ID from JWT token
- `id` (integer): Task ID

**Response:** `200 OK`
```json
{
  "message": "Task deleted successfully"
}
```

**Errors:**
- `404 Not Found`: Task doesn't exist or doesn't belong to user
- `401 Unauthorized`: Invalid JWT
- `403 Forbidden`: user_id mismatch

---

### Toggle Task Completion
```
PATCH /api/{user_id}/tasks/{id}/complete
```
**Description:** Mark task as complete or incomplete  
**Auth Required:** Yes  
**Path Parameters:**
- `user_id` (string): User ID from JWT token
- `id` (integer): Task ID

**Request Body:**
```json
{
  "completed": true
}
```

**Response:** `200 OK`
```json
{
  "data": {
    "id": 1,
    "user_id": "uuid",
    "title": "Task title",
    "description": "Description",
    "completed": true,
    "created_at": "2024-01-15T10:00:00Z",
    "updated_at": "2024-01-15T12:00:00Z"
  }
}
```

**Errors:**
- `404 Not Found`: Task doesn't exist or doesn't belong to user
- `401 Unauthorized`: Invalid JWT
- `403 Forbidden`: user_id mismatch

---

## Error Status Codes Summary

| Code | Meaning |
|------|---------|
| 200 | Success |
| 201 | Created |
| 400 | Bad Request (validation error) |
| 401 | Unauthorized (invalid/missing JWT) |
| 403 | Forbidden (user doesn't own resource) |
| 404 | Not Found |
| 500 | Internal Server Error |

## CORS Configuration
- Allow origins: Frontend URL (http://localhost:3000 in dev)
- Allow methods: GET, POST, PUT, PATCH, DELETE
- Allow headers: Authorization, Content-Type