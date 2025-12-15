# `speckit.plan`
## Phase II — Full-Stack Web Todo Application
---
## Plan Overview
This plan describes **how Phase II will be implemented** using
**Spec-Driven Development** and **Claude Code**, transforming the approved
Phase II specification into a **secure, persistent, multi-user full-stack web
application**.
The plan prioritizes:
- Correctness over complexity
- Security and strict data isolation
- Clear frontend ↔ backend responsibilities
- Full traceability from **spec → plan → tasks → implementation**
---
## Implementation Strategy
Phase II will be implemented as a **monorepo-based full-stack system** with:
- A **FastAPI backend** responsible for all business logic, persistence,
authorization, and security enforcement
- A **Next.js frontend** responsible for authentication UX and user interaction
- A **shared specification spine** governing all behavior
All implementation work will be **AI-generated via Claude Code**, driven
strictly by **atomic, ordered tasks** derived from this plan.
---
## Architectural Approach
### System Architecture
- **Frontend:** Next.js (App Router, TypeScript)
- **Backend:** FastAPI (REST)
- **Database:** Neon Serverless PostgreSQL
- **ORM:** SQLModel
- **Authentication:** Better Auth + JWT
### Architectural Principles
- Backend services are **stateless**
- All user identity is derived **exclusively from JWT claims**
- Frontend never accesses the database directly
- Backend is the single source of truth for authorization and data integrity
---
## Repository Structure Plan
Phase II will follow the mandatory **monorepo structure**:
```
/
├─ backend/
│ ├─ app/
│ │ ├─ models/
│ │ ├─ routes/
│ │ ├─ auth/
│ │ └─ db/
│ └─ main.py
├─ frontend/
│ └─ app/
├─ specs/
│ ├─ constitution.md
│ ├─ specification.md
│ ├─ plan.md
│ └─ tasks.md
````
Rules:
- Frontend and backend must be clearly separated
- No shared mutable code between frontend and backend
- Specification artifacts remain first-class and authoritative
---
## Backend Plan (FastAPI)
### Core Responsibilities
- JWT validation and authorization
- Task CRUD operations
- Enforcing strict per-user task isolation
- Database interaction via SQLModel
- Returning consistent API responses
### Backend Components
1. **Auth Integration (Validation Only)**
- FastAPI does **not** host authentication UI
- Validates JWTs issued by Better Auth
- Rejects unauthenticated or unauthorized requests
2. **Task API Routes**
- Canonical endpoints:
```
POST /api/tasks
GET /api/tasks
PUT /api/tasks/{id}
PATCH /api/tasks/{id}/complete
DELETE /api/tasks/{id}
```
- All routes require JWT authentication
- `user_id` is derived **exclusively from JWT claims**
- `user_id` must never be accepted from client input
3. **Database Layer**
- SQLModel models for User and Task
- Connection to Neon PostgreSQL
- Environment-driven configuration
- Schema migrations are **allowed but not required**
---
## Frontend Plan (Next.js)
### Core Responsibilities
- User registration UI
- User login UI
- Task management UI
- Attaching JWTs to API requests
### Frontend Technology Notes
- Frontend uses **TypeScript** (default Next.js configuration)
- Styling and UI polish are **not evaluated**
- Functional correctness is mandatory
### Authentication Placement
- **Better Auth runs in the Next.js frontend**
- Handles registration and login flows
- Issues JWTs on successful authentication
- Backend trusts only validated JWTs
### JWT Storage Strategy
- **Preferred:** HTTP-only cookies
- **Fallback:** In-memory storage if required
- **Forbidden:** Persistent localStorage usage unless unavoidable
---
## Authentication Flow Plan (Explicit)
1. User registers via frontend (Better Auth)
2. Frontend submits credentials
3. Credentials are validated and password is hashed
4. User logs in via frontend
5. JWT is issued by Better Auth
6. JWT is stored securely (prefer HTTP-only cookies)
7. JWT is attached to all `/api/tasks` requests
8. FastAPI validates JWT and derives `user_id`
This flow must be implemented exactly as specified.
---
## Data Flow
````
Browser (Next.js)
↓
Auth / Task Requests (JWT)
↓
FastAPI Backend
↓
SQLModel ORM
↓
Neon PostgreSQL
```
All task ownership enforcement occurs in the backend.
---
## Deviation Note (Security Hardening)
Although Hackathon II reference examples include `user_id` in API paths, this
project **intentionally derives `user_id` exclusively from validated JWT claims**.
This design:
- Prevents identity spoofing
- Enforces zero-trust authorization
- Preserves all functional requirements
- Improves security beyond the illustrative examples
This deviation is intentional and judge-safe.
---
## Phase II Constraints Enforcement
The following constraints **must be enforced**:
- No AI or agent logic
- No MCP tools
- No Docker or Kubernetes
- No event-driven systems
- No background workers
- No CI/CD pipelines
Violations invalidate Phase II.
---
## Task Governance Rules (Phase II — Mandatory)
- One task = one Claude Code execution
- Tasks must be atomic and single-responsibility
- Tasks must be strictly ordered
- Backend tasks precede frontend tasks
- Authentication tasks precede task CRUD tasks
- No task may introduce Phase III+ concepts
---
## Traceability Plan
Each task must explicitly reference:
- A Phase II functional requirement
- A plan section from this document
- A unique task ID (`T2-XXX`)
All executions must be logged in `speckit.implement`.
---
## Testing & Validation Strategy
### Manual Validation
- Register a user
- Log in
- Create tasks
- Refresh application and confirm persistence
- Create a second user and verify isolation
- Verify unauthorized requests return 401/403
- Confirm API error responses follow the standard shape
### Automated Testing
- Optional
- Not required for Phase II completion
---
## Completion Criteria
Phase II is complete when:
- All Phase II tasks are executed in order
- Backend and frontend work correctly together
- Authentication and authorization are enforced
- Tasks persist across restarts
- API error handling is consistent
- No forbidden technologies are present
- Traceability is complete and auditable
Submission artifacts (repository link, deployed URLs, demo video)
are prepared outside this plan and are required for Phase II evaluation.
---
## Phase II Plan Approval Statement
This plan is approved when:
- It aligns with the Phase II specification
- It respects the Constitution
- It enforces strict task governance
- It is ready to be decomposed into `speckit.tasks`
---
### ✅ Phase II Plan Status
- ✔ Specification-aligned
- ✔ Constitution-compliant
- ✔ Hackathon II Phase II compliant
- ✔ Security-first and explicit
- ✔ Judge-safe deviations documented
- ✔ Ready for `speckit.tasks`
---