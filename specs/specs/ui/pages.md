# UI Pages Specification

## Page Structure
All pages follow this layout:
```
┌─────────────────────────────────────┐
│           Header                    │
├─────────────────────────────────────┤
│                                     │
│         Page Content                │
│                                     │
└─────────────────────────────────────┘
```

---

## Pages

### 1. Sign In Page (`/signin`)
**Route:** `/signin`  
**Auth Required:** No  
**Redirect:** If authenticated → `/tasks`

**Layout:**
```
┌─────────────────────────────────────┐
│                                     │
│       📝 Todo App                   │
│                                     │
│    ┌─────────────────────┐          │
│    │   AuthForm          │          │
│    │   (mode: signin)    │          │
│    └─────────────────────┘          │
│                                     │
└─────────────────────────────────────┘
```

**Features:**
- Centered auth form
- Link to sign up page
- Error messages for invalid credentials
- Loading state during authentication

---

### 2. Sign Up Page (`/signup`)
**Route:** `/signup`  
**Auth Required:** No  
**Redirect:** If authenticated → `/tasks`

**Layout:**
```
┌─────────────────────────────────────┐
│                                     │
│       📝 Todo App                   │
│                                     │
│    ┌─────────────────────┐          │
│    │   AuthForm          │          │
│    │   (mode: signup)    │          │
│    └─────────────────────┘          │
│                                     │
└─────────────────────────────────────┘
```

**Features:**
- Centered auth form
- Link to sign in page
- Validation errors
- Success redirect to tasks page

---

### 3. Tasks Page (`/tasks`)
**Route:** `/tasks` or `/`  
**Auth Required:** Yes  
**Redirect:** If not authenticated → `/signin`

**Layout:**
```
┌─────────────────────────────────────┐
│ Header (with user info & logout)    │
├─────────────────────────────────────┤
│                                     │
│  Add New Task                       │
│  ┌─────────────────────┐            │
│  │   TaskForm          │            │
│  └─────────────────────┘            │
│                                     │
│  My Tasks                           │
│  ┌─────────────────────┐            │
│  │   TaskList          │            │
│  │   - TaskCard        │            │
│  │   - TaskCard        │            │
│  │   - TaskCard        │            │
│  └─────────────────────┘            │
│                                     │
└─────────────────────────────────────┘
```

**Features:**
- Task creation form at top
- Filter tabs (All/Pending/Completed)
- List of tasks
- Each task can be edited/deleted/toggled
- Empty state when no tasks
- Loading state while fetching

**Functionality:**
- Fetch tasks on mount
- Real-time updates after CRUD operations
- Optimistic UI updates (optional)
- Error handling with toast notifications

---

### 4. Loading Page
**Purpose:** Show while initial auth check happens

**Layout:**
```
┌─────────────────────────────────────┐
│                                     │
│             ⏳                       │
│          Loading...                 │
│                                     │
└─────────────────────────────────────┘
```

---

### 5. 404 Page (Not Found)
**Route:** `*` (catch-all)

**Layout:**
```
┌─────────────────────────────────────┐
│                                     │
│            404                      │
│       Page Not Found                │
│                                     │
│    [Go to Tasks]                    │
│                                     │
└─────────────────────────────────────┘
```

---

## Page Flow Diagram
```
User visits app
    ↓
Is authenticated?
    ↓ No              ↓ Yes
/signin           /tasks
    ↓
Sign in success
    ↓
/tasks
    ↓
Click logout
    ↓
/signin
```

---

## Mobile Responsive Behavior

### Mobile (< 640px)
- Single column layout
- Task form stacked vertically
- Filter tabs scrollable
- Tasks full width

### Tablet (640px - 1024px)
- Two column layout for task cards
- Task form in modal (optional)

### Desktop (> 1024px)
- Max width container (1024px)
- Centered layout
- Side-by-side form and list (optional)

---

## SEO & Meta Tags

### Sign In Page
```html
<title>Sign In - Todo App</title>
<meta name="description" content="Sign in to your Todo App account" />
```

### Tasks Page
```html
<title>My Tasks - Todo App</title>
<meta name="description" content="Manage your tasks efficiently" />
```

---

## Accessibility
- Keyboard navigation support
- ARIA labels for buttons
- Focus visible styles
- Screen reader friendly error messages
- Semantic HTML (header, main, nav)
```

---

## ✅ **All 8 Files Complete!**

Ab tumhara **specs/** folder completely ready hai:
```
specs/
├── overview.md              ✅
├── architecture.md          ✅
├── features/
│   ├── task-crud.md        ✅
│   └── authentication.md   ✅
├── api/
│   └── rest-endpoints.md   ✅
├── database/
│   └── schema.md           ✅
└── ui/
    ├── components.md       ✅
    └── pages.md            ✅