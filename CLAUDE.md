# Claude Code Instructions

This document provides instructions and constraints for Claude Code when working on this project.

## Project Context

This is **Hackathon II: The Evolution of Todo** — a demonstration of Spec-Driven Development (SDD).

## Governing Documents

Claude Code must respect the following hierarchy (higher overrides lower):

1. **Constitution** — `.specify/memory/constitution.md`
2. **Specification** — `specs/[feature]/spec.md`
3. **Plan** — `specs/[feature]/plan.md`
4. **Tasks** — `specs/[feature]/tasks.md`
5. **Implementation** — Generated code

## Core Principles

1. **Spec Before Code** — Never write code without an approved specification
2. **No Manual Coding** — All code must be generated via Claude Code
3. **Traceability** — Every implementation must reference spec/plan/task
4. **If Not Specified, It Doesn't Exist** — Do not invent features

## Current Phase: Phase II — Full-Stack Web Application

### Architecture

```
frontend/ (Next.js 14 App Router)
├── app/
│   ├── context/AuthContext.tsx   # Auth state management
│   ├── lib/api.ts                # API client
│   ├── login/page.tsx            # Login page
│   ├── register/page.tsx         # Registration page
│   └── tasks/page.tsx            # Main tasks page

backend/ (FastAPI)
├── app/
│   ├── auth/auth.py              # JWT authentication
│   ├── db/db.py                  # Database configuration
│   ├── models/                   # SQLModel entities
│   └── routes/                   # API routes
└── main.py                       # FastAPI application
```

### API Endpoints

- `POST /api/auth/register` — User registration
- `POST /api/auth/login` — User login (returns JWT)
- `GET /api/auth/me` — Get current user
- `POST /api/tasks/` — Create task
- `GET /api/tasks/` — List user's tasks
- `PUT /api/tasks/{id}` — Update task
- `PATCH /api/tasks/{id}/complete` — Mark task complete
- `DELETE /api/tasks/{id}` — Delete task

### Security Requirements

- All `/api/tasks` endpoints require JWT authentication
- User ID is derived from JWT claims (never from URL)
- Unauthorized access returns 401
- Cross-user access returns 403
- Passwords are hashed with bcrypt

## Technology Stack

### Backend
- FastAPI 0.109
- SQLModel 0.0.14
- bcrypt for password hashing
- python-jose for JWT
- SQLite (local) / PostgreSQL (production)

### Frontend
- Next.js 14 (App Router)
- React 18
- TypeScript

## Task Execution Rules

1. One task = one Claude Code execution
2. Execute tasks strictly in order
3. If output is incorrect, update spec/plan/tasks — not code directly
4. Log all executions in `specs/[feature]/implement.md`

## Running the Application

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## When Stuck

If specifications are incomplete or ambiguous:
1. Stop and request clarification
2. Do not assume or invent behavior
3. Update spec before proceeding
