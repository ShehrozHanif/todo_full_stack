---
description: "Task list for feature implementation"
---

# Tasks: Full-Stack Web Todo Application

**Input**: Design documents from `specs/002-full-stack-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md, contracts/

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T2-001 [P] Create the mandatory Phase II monorepo structure in `/backend` and `/frontend`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented.

- [X] T2-002 Configure FastAPI backend environment and database connectivity in `.env` and `backend/app/db/`.
- [X] T2-003 Define the persistent `User` model using SQLModel in `backend/app/models/user.py`.
- [X] T2-004 Define the persistent `Task` model scoped to users in `backend/app/models/task.py`.
- [X] T2-005 Implement database schema initialization in `backend/app/db/`.
- [X] T2-006 Explicitly configure CORS to allow frontend → backend communication in `backend/main.py`.
- [X] T2-007 [P] Integrate Better Auth into the Next.js frontend for registration and login in `frontend/app/auth/`.
- [X] T2-008 Implement JWT validation in FastAPI in `backend/app/auth/`.

---

## Phase 3: User Story 1 - Authenticated Task Management (Priority: P1) 🎯 MVP

**Goal**: Users can manage their tasks through the web interface.

**Independent Test**: A user can register, log in, create, view, update, and delete their own tasks. A second user cannot see or interact with the first user's tasks.

### Implementation for User Story 1

- [X] T2-009 [US1] Implement authenticated task creation endpoint `POST /api/tasks` in `backend/app/routes/tasks.py`.
- [X] T2-010 [US1] Implement authenticated task listing endpoint `GET /api/tasks` in `backend/app/routes/tasks.py`.
- [X] T2-011 [US1] Implement authenticated task update endpoint `PUT /api/tasks/{id}` in `backend/app/routes/tasks.py`.
- [X] T2-012 [US1] Implement task completion endpoint `PATCH /api/tasks/{id}/complete` in `backend/app/routes/tasks.py`.
- [X] T2-013 [US1] Implement task deletion endpoint `DELETE /api/tasks/{id}` in `backend/app/routes/tasks.py`.
- [X] T2-014 [US1] Implement frontend UI for authenticated task management in `frontend/app/tasks/`.

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories.

- [X] T2-015 Implement user logout behavior in the frontend in `frontend/app/auth/`.
- [X] T2-016 Enforce consistent API error responses in `backend/app/`.
- [X] T2-017 Manually validate Phase II behavior.
- [X] T2-018 Prepare required Phase II submission materials.

---

## Dependencies & Execution Order

- **Setup (Phase 1)** must be completed first.
- **Foundational (Phase 2)** depends on Setup and blocks all other phases.
- **User Story 1 (Phase 3)** depends on the Foundational phase.
- **Polish (Phase 4)** depends on all previous phases.
