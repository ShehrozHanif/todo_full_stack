# Hackathon II: The Evolution of Todo

A demonstration of **Spec-Driven Development (SDD)** applied to the evolution of a real software system — from a simple CLI application to a cloud-native, AI-powered, event-driven system.

## Project Overview

This project follows the **Spec-Kit Plus** lifecycle:

```
Constitution -> Specification -> Plan -> Tasks -> Implementation
```

All code is generated via **Claude Code** based on approved specifications. No manual coding is permitted.

## Current Phase: Phase II — Full-Stack Web Todo Application

Phase II evolves the system into a **persistent, multi-user, full-stack web application** with:
- FastAPI REST backend with JWT authentication
- Next.js frontend (App Router)
- SQLite database (local) / PostgreSQL (production)
- User registration, login, and data isolation

## Quick Start

### Prerequisites

- Python 3.9+
- Node.js 16+
- pip and npm

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs at: http://localhost:8000

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at: http://localhost:3000

## Features

### Authentication
- User registration with email/username/password
- JWT-based authentication
- Secure password hashing with bcrypt

### Task Management
- Create, read, update, delete tasks
- Mark tasks as complete
- Per-user data isolation
- Persistent storage

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/auth/register | Register new user |
| POST | /api/auth/login | Login and get JWT |
| GET | /api/auth/me | Get current user |
| POST | /api/tasks/ | Create task |
| GET | /api/tasks/ | List user's tasks |
| PUT | /api/tasks/{id} | Update task |
| PATCH | /api/tasks/{id}/complete | Mark complete |
| DELETE | /api/tasks/{id} | Delete task |

## Project Structure

```
todo_full_stack/
├── backend/
│   ├── app/
│   │   ├── auth/           # Authentication module
│   │   ├── db/             # Database configuration
│   │   ├── models/         # SQLModel entities
│   │   └── routes/         # API routes
│   ├── main.py             # FastAPI application
│   └── requirements.txt
├── frontend/
│   ├── app/
│   │   ├── context/        # React context (Auth)
│   │   ├── lib/            # API client
│   │   ├── login/          # Login page
│   │   ├── register/       # Registration page
│   │   └── tasks/          # Tasks page
│   └── package.json
├── specs/
│   ├── 001-in-memory-cli-todo/   # Phase I specs
│   └── 002-full-stack-todo-app/  # Phase II specs
├── src/
│   └── main.py             # Phase I CLI (preserved)
├── CLAUDE.md               # Claude Code instructions
└── README.md
```

## Validation Results

All Phase II requirements have been validated:

- [x] User registration works
- [x] User login returns JWT
- [x] Tasks persist across restarts
- [x] User isolation enforced (users only see own tasks)
- [x] Unauthorized access returns 401
- [x] Cross-user access returns 403
- [x] All CRUD operations work
- [x] Frontend connects to backend

## Technology Stack

### Backend
- FastAPI 0.109
- SQLModel 0.0.14
- bcrypt for password hashing
- python-jose for JWT

### Frontend
- Next.js 14 (App Router)
- React 18
- TypeScript

### Database
- SQLite (local development)
- PostgreSQL (production via Neon)

## Spec-Driven Development

This project strictly follows Spec-Driven Development principles:

1. **Spec Before Code** — No code without approved specification
2. **No Manual Coding** — All code generated via Claude Code
3. **Single Evolving System** — One system across all phases
4. **Traceability** — Every line traces to spec/plan/task
5. **AI as Executor** — Human architects, AI implements

## Phase Roadmap

| Phase | Description | Status |
|-------|-------------|--------|
| I | In-Memory CLI Todo App | Complete |
| II | Full-Stack Web Application | Complete |
| III | AI-Powered Todo Chatbot | Planned |
| IV | Local Kubernetes Deployment | Planned |
| V | Cloud-Native Event-Driven System | Planned |

## License

This project is part of Hackathon II.
