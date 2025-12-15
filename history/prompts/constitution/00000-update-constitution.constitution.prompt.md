---
id: 00000
title: Update Constitution
stage: constitution
date: 2025-12-15
surface: agent
model: gemini-cli-agent
feature: none
branch: main
user: user
command: /sp.constitution
labels: ["constitution", "governance"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- .specify/memory/constitution.md
tests: null
---

## Prompt

```text
/sp.constitution 

# Constitution — Hackathon II: The Evolution of Todo

## Purpose

This project exists to demonstrate **Spec-Driven Development (SDD)** applied to the full
evolution of a real software system — from a simple CLI application to a cloud-native,
AI-powered, event-driven system deployed on Kubernetes.

The primary goal is **not writing code**, but **designing, governing, and evolving systems
using specifications and AI agents**, in strict accordance with Hackathon II requirements.

---

## Core Principles (Non-Negotiable)

1. **Spec Before Code**
   - No code may be written or generated before the specification is complete.
   - Specifications are the single source of truth.

2. **No Manual Coding**
   - All implementation must be generated via **Claude Code**.
   - If output is incorrect, the specification must be refined — not the code.

3. **Single Evolving System**
   - This project is **one Todo system**, not multiple disconnected projects.
   - Each phase extends the same domain, architecture, and codebase.

4. **Traceability**
   - Every implementation must trace back to:
     - Specification section
     - Plan section
     - Task ID
   - No task = no code.

5. **AI as Executor, Human as Architect**
   - Humans define intent, constraints, and architecture.
   - AI agents execute strictly within those boundaries.

---

## Mandatory Spec-Driven Development Workflow

This project **must** use **Spec-Kit Plus** as the official Spec-Driven Development system.

All work must follow the **Spec-Kit lifecycle**:

```

Specify → Plan → Tasks → Implement

```

- Specifications, plans, tasks, and implementation logs must be managed using
  **Spec-Kit Plus artifacts**.
- MCP-exposed Spec-Kit commands must be used where applicable.
- The full specification and refinement history is subject to evaluation.

Deviation from this workflow is not permitted.

---

## Spec-Driven Development Hierarchy

All work in this project must follow this strict hierarchy:

```

Constitution
↓
Specification (WHAT)
↓
Plan (HOW)
↓
Tasks (ATOMIC WORK)
↓
Implementation (AI-Generated Code)

```

Higher-level documents override lower-level ones.
Conflicts must be resolved by updating the higher document.

---

## Project Scope & Evolution Rules

- The project evolves through **five mandatory phases**:
  1. CLI In-Memory Todo App
  2. Full-Stack Web Application
  3. AI-Powered Todo Chatbot
  4. Local Kubernetes Deployment
  5. Cloud-Native Event-Driven System

- Phases are **layered**, not isolated.
- Earlier functionality must continue to work unless explicitly deprecated.
- Architecture may evolve but **must never reset**.

---

## Phase I Constraint — In-Memory Only

- **Phase I must be strictly in-memory**.
- No database, file storage, or persistence of any kind is allowed.
- All data must be lost on application exit.

This constraint is constitutional and non-negotiable.

---

## Domain Principles

- The **Todo domain** is central and persistent.
- Core entity: **Task**
- Task behavior must remain consistent across:
  - CLI
  - Web
  - Chatbot
  - Distributed services
- New capabilities (authentication, AI, events) **extend the domain**, not replace it.

---

## Security & Multi-User Data Isolation

- From **Phase II onward**, the system must support **multiple users**.
- **Strict data isolation is mandatory**:
  - Users may only access their own tasks.
  - All backend operations must be scoped to authenticated users.
- Authentication must use **Better Auth with JWT**.
- Unauthorized requests must be rejected.

Security is a constitutional requirement, not an implementation detail.

---

## Interface & Compatibility Guarantees

- All task operations exposed via:
  - REST APIs (implemented using FastAPI)
  - MCP tools
  - Event payloads
  must maintain **consistent semantics** once introduced.

- Backward compatibility is required unless a breaking change is explicitly specified
  and versioned in the specification.

---

## Architectural Principles

1. **Stateless Services**
   - All services must be stateless.
   - State must live in databases or external systems.

2. **Clear and Stable Interfaces**
   - REST APIs, MCP tools, and events are contracts.
   - Contracts must not change silently.

3. **Progressive Complexity**
   - Use the simplest architecture per phase.
   - Introduce complexity only when required.

4. **Event-Driven by Design**
   - Advanced features (reminders, recurrence, audit logs, notifications)
     must be implemented via **asynchronous event-driven architecture**.
   - Kafka (or compatible) is mandatory for inter-service communication.

5. **Cloud-Native First**
   - Kubernetes is the target runtime.
   - Local and cloud environments must share the same architecture.

---

## AI, Agents & Tool Governance

- AI agents must:
  - Obey the Constitution, Specification, Plan, and Tasks.
  - Never invent features.
  - Halt and request clarification when specs are incomplete.

- **AI agents may only mutate system state through approved MCP tools**.
  - Direct database access or hidden logic is forbidden.

- Chat systems must be:
  - Stateless at the API level
  - Backed by persistent conversation and message storage
  - Able to resume conversations after restarts

---

## Reusable Intelligence

- The system should support **reusable intelligence**, including:
  - Agent skills
  - Subagents
  - Cloud-native intelligence blueprints

This is a guiding principle aligned with Hackathon II bonus criteria.

---

## Technology Constraints

Unless explicitly updated in the specification, the following are mandatory:

- **Languages & Frameworks**
  - Python (FastAPI)
  - Next.js (App Router)
  - SQLModel

- **AI**
  - Claude Code
  - OpenAI Agents SDK
  - Official MCP SDK
  - OpenAI ChatKit

- **Infrastructure**
  - Docker
  - Kubernetes (Minikube locally, managed Kubernetes in cloud)
  - Helm Charts
  - Kafka (or Kafka-compatible service)
  - Dapr

- **Authentication**
  - Better Auth with JWT

---

## CI/CD Requirement (Phase V)

- A **CI/CD pipeline using GitHub Actions** is mandatory in Phase V.
- The pipeline must:
  - Build
  - Test
  - Deploy to Kubernetes
- Automation is required; manual deployments are insufficient.

---

## Quality, Validation & Evidence Standards

- Each phase must be:
  - Spec-complete
  - Functionally demonstrable
  - Explainable to non-technical audiences

- Manual testing steps must be documented.
- Demo videos must show **real running systems**, not mockups.

---

## Submission & Delivery Requirements (Mandatory)

The following artifacts are required:

- One public GitHub repository
- Complete spec history
- `CLAUDE.md` and `AGENTS.md`
- Deployment URLs (where applicable)
- Demo videos (≤ 90 seconds)
- Clear and complete `README.md`

Missing artifacts constitute an incomplete submission.

---

## Change Management

- Feature changes → Specification
- Architecture changes → Plan
- Work changes → Tasks
- Principle changes → Constitution

Silent changes are forbidden.

---

## Success Definition

The project is successful when:

- All five phases exist in one evolving system
- Spec-Driven Development via Spec-Kit Plus is evident
- AI agents perform real, tool-based work
- The system runs locally on Kubernetes
- The system runs in the cloud with event-driven architecture
- All artifacts are public and complete

---

## Final Rule

> **If it is not specified, it does not exist.**  
> **If it is not traceable, it is invalid.**  
> **If it is not spec-driven, it does not count.**
```
---

## ✅ Status

* ✔ Fully compliant with **Hackathon II**
* ✔ All approved YES decisions implemented
* ✔ Judge-proof
* ✔ Ready to lock as **Constitution v1.2 (final)**

---
```

## Response snapshot

The project constitution has been updated to version 1.2 with the provided content. The `Ratified` and `Last Amended` dates are set to `2025-12-15`. A Sync Impact Report has been included as an HTML comment at the top of the file, listing the version change and flagging templates that may require manual alignment with the updated principles.

**New version:** 1.2
**Bump rationale:** Finalized Hackathon II principles.

**Suggested commit message:**
```
docs: Update constitution to v1.2 (finalized Hackathon II principles)
```

**Files flagged for manual follow-up (to check for alignment with new constitution):**
- `.specify/templates/plan-template.md`
- `.specify/templates/spec-template.md`
- `.specify/templates/tasks-template.md`
- `.specify/templates/adr-template.md`
- `.specify/templates/agent-file-template.md`
- `.specify/templates/checklist-template.md`
- `.specify/templates/phr-template.prompt.md`
- `.specify/templates/commands/sp.adr.toml`
- `.specify/templates/commands/sp.analyze.toml`
- `.specify/templates/commands/sp.checklist.toml`
- `.specify/templates/commands/sp.clarify.toml`
- `.specify/templates/commands/sp.constitution.toml`
- `.specify/templates/commands/sp.git.commit_pr.toml`
- `.specify/templates/commands/sp.implement.toml`
- `.specify/templates/commands/sp.phr.toml`
- `.specify/templates/commands/sp.plan.toml`
- `.specify/templates/commands/sp.specify.toml`
- `.specify/templates/commands/sp.tasks.toml`

## Outcome

- ✅ Impact: The project's constitution has been updated to its final version, establishing core principles and guidelines for all future development.
- 🧪 Tests: No tests were run as this was a documentation update.
- 📁 Files: One file was modified: `.specify/memory/constitution.md`. One file was created: `history/prompts/constitution/00000-update-constitution.constitution.prompt.md`.
- 🔁 Next prompts: The user should consider reviewing the flagged templates for alignment with the new constitution and then commit the changes.
- 🧠 Reflection: The agent successfully handled the request to update the constitution and generated a PHR using agent-native tools after a shell script failure, demonstrating resilience.

## Evaluation notes (flywheel)

- Failure modes observed: The shell script for PHR creation failed, likely due to environment differences (PowerShell vs. bash). The agent successfully fell back to agent-native tool usage.
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
