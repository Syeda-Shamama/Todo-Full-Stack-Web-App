# Feature: Task CRUD Operations

## User Stories

### As a user, I can create a new task
- I enter a title (required)
- I can optionally enter a description
- Task is saved and appears in my task list
- Task is marked as incomplete by default

### As a user, I can view all my tasks
- I see a list of all my tasks
- Each task shows: title, status, created date
- I can filter tasks by status (all/pending/completed)
- I only see MY tasks, not other users' tasks

### As a user, I can update a task
- I can edit the title
- I can edit the description
- Changes are saved immediately

### As a user, I can delete a task
- I can remove a task permanently
- Deleted tasks don't appear in my list

### As a user, I can mark a task complete/incomplete
- I can toggle task completion status
- Completed tasks are visually distinct

## Acceptance Criteria

### Create Task
- Title is required (1-200 characters)
- Description is optional (max 1000 characters)
- Task must be associated with logged-in user
- Return 401 if user not authenticated
- Return 400 if validation fails

### View Tasks
- Only show tasks for authenticated user
- Display: title, description, completed status, created_at
- Support filtering: all, pending, completed
- Default sort: newest first

### Update Task
- Only task owner can update
- Return 404 if task doesn't exist
- Return 403 if user doesn't own task
- Validate title length (1-200 chars)

### Delete Task
- Only task owner can delete
- Return 404 if task doesn't exist
- Return 403 if user doesn't own task
- Soft delete or hard delete (implement hard delete)

### Toggle Complete
- Only task owner can toggle
- Return 404 if task doesn't exist
- Return 403 if user doesn't own task
- Update completed field and updated_at timestamp

## UI Requirements
- Clean, modern interface
- Mobile responsive
- Loading states during API calls
- Error messages for failures
- Success feedback for actions