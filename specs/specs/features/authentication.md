# Feature: User Authentication

## User Stories

### As a new user, I can sign up
- I provide email and password
- I provide my name
- Account is created in the system
- I'm automatically logged in after signup

### As a returning user, I can sign in
- I enter my email and password
- System verifies my credentials
- I receive a JWT token
- I'm redirected to my tasks

### As a logged-in user, I can sign out
- I can log out from the application
- My session is cleared
- I'm redirected to login page

## Acceptance Criteria

### Sign Up
- Email must be valid format
- Email must be unique (no duplicates)
- Password minimum 8 characters
- Name is required
- Return 400 if validation fails
- Return 409 if email already exists
- Issue JWT token on success
- Store user in database

### Sign In
- Email must exist in database
- Password must match hashed password
- Return 401 if credentials invalid
- Issue JWT token on success
- Token expires after 7 days

### Sign Out
- Clear JWT token from client
- Redirect to login page
- Server-side token invalidation (optional)

## Security Requirements
- Passwords hashed with bcrypt (handled by Better Auth)
- JWT tokens signed with secret key
- Tokens include: user_id, email, expiry
- HTTPS required in production
- Rate limiting on login attempts (optional)

## JWT Token Structure
```json
{
  "user_id": "uuid",
  "email": "user@example.com",
  "exp": 1234567890
}
```

## UI Requirements
- Separate pages for signup and signin
- Form validation with error messages
- Loading states during authentication
- Redirect authenticated users away from login pages
- Password visibility toggle
- "Remember me" option (optional)

## Integration Points
- Better Auth handles password hashing
- Better Auth issues JWT tokens
- Frontend stores token in memory or localStorage
- Backend verifies token on every API request
- Shared secret (BETTER_AUTH_SECRET) between frontend and backend