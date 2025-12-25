# UI Components Specification

## Design Principles
- Mobile-first responsive design
- Clean, modern aesthetic
- Consistent spacing and typography
- Accessible (WCAG 2.1 AA)
- Loading states for all async operations
- Error handling with user-friendly messages

## Component Library: Tailwind CSS + shadcn/ui (optional)

---

## Core Components

### 1. TaskCard
**Purpose:** Display a single task

**Props:**
- `task`: Task object
- `onToggle`: Function to toggle completion
- `onEdit`: Function to edit task
- `onDelete`: Function to delete task

**Design:**
```
┌─────────────────────────────────────┐
│ [ ] Task Title             [Edit][×]│
│     Task description...             │
│     Created: Jan 15, 2024           │
└─────────────────────────────────────┘
```

**States:**
- Default: White background, checkbox unchecked
- Completed: Gray background, checkbox checked, strikethrough text
- Hover: Slight shadow, visible action buttons
- Loading: Disabled, spinner on action

**Styling:**
- Rounded corners (8px)
- Padding: 16px
- Border: 1px solid gray-200
- Hover: shadow-md

---

### 2. TaskList
**Purpose:** Display list of tasks

**Props:**
- `tasks`: Array of Task objects
- `filter`: "all" | "pending" | "completed"
- `onFilterChange`: Function to change filter

**Design:**
```
┌─────────────────────────────────────┐
│ [All] [Pending] [Completed]         │
├─────────────────────────────────────┤
│ TaskCard                            │
│ TaskCard                            │
│ TaskCard                            │
└─────────────────────────────────────┘
```

**Empty State:**
```
┌─────────────────────────────────────┐
│         No tasks yet!               │
│    Create your first task above     │
└─────────────────────────────────────┘
```

---

### 3. TaskForm
**Purpose:** Create or edit a task

**Props:**
- `task`: Task object (optional, for editing)
- `onSubmit`: Function to handle form submission
- `onCancel`: Function to cancel editing

**Design:**
```
┌─────────────────────────────────────┐
│ Title: [________________]           │
│                                     │
│ Description:                        │
│ [____________________________]      │
│ [____________________________]      │
│                                     │
│      [Cancel]  [Save Task]          │
└─────────────────────────────────────┘
```

**Validation:**
- Title required (show error if empty)
- Title max 200 chars (show counter)
- Description max 1000 chars (show counter)

---

### 4. Header
**Purpose:** App header with navigation and user info

**Design:**
```
┌─────────────────────────────────────┐
│ 📝 Todo App    user@email.com [Logout]│
└─────────────────────────────────────┘
```

**Features:**
- App logo/title on left
- User email in center
- Logout button on right
- Mobile: Hamburger menu

---

### 5. AuthForm
**Purpose:** Sign up / Sign in form

**Props:**
- `mode`: "signup" | "signin"
- `onSubmit`: Function to handle authentication

**Design (Sign In):**
```
┌─────────────────────────────────────┐
│          Welcome Back!              │
│                                     │
│ Email: [________________]           │
│                                     │
│ Password: [________________] [👁]   │
│                                     │
│      [Sign In]                      │
│                                     │
│ Don't have an account? Sign Up      │
└─────────────────────────────────────┘
```

**Design (Sign Up):**
```
┌─────────────────────────────────────┐
│        Create Account               │
│                                     │
│ Name: [________________]            │
│                                     │
│ Email: [________________]           │
│                                     │
│ Password: [________________] [👁]   │
│                                     │
│      [Sign Up]                      │
│                                     │
│ Already have an account? Sign In    │
└─────────────────────────────────────┘
```

**Validation:**
- Email format validation
- Password minimum 8 characters
- Show inline errors below fields

---

### 6. Button
**Purpose:** Reusable button component

**Variants:**
- `primary`: Blue background, white text
- `secondary`: White background, gray border
- `danger`: Red background, white text

**States:**
- Default
- Hover: Darker shade
- Disabled: Gray, not clickable
- Loading: Spinner inside button

---

### 7. Input
**Purpose:** Text input field

**Props:**
- `label`: Field label
- `type`: "text" | "email" | "password"
- `error`: Error message (optional)
- `required`: Boolean

**Design:**
```
Label *
[____________________________]
Error message here (if any)
```

---

### 8. LoadingSpinner
**Purpose:** Show loading state

**Design:** Rotating circle animation

**Usage:**
- Full page loading
- Button loading
- Card loading

---

## Responsive Breakpoints
- Mobile: < 640px
- Tablet: 640px - 1024px
- Desktop: > 1024px

## Color Palette
- Primary: Blue (#3B82F6)
- Success: Green (#10B981)
- Danger: Red (#EF4444)
- Gray-50 to Gray-900 for text/backgrounds

## Typography
- Headings: font-bold, text-2xl/xl/lg
- Body: font-normal, text-base
- Small: text-sm

## Spacing
- Use Tailwind spacing scale (4px increments)
- Consistent padding: p-4, p-6
- Consistent margins: mb-4, mt-6