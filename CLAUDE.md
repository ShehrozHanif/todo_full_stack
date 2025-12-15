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

## Phase I Constraints

Phase I is strictly in-memory:

- No databases
- No file persistence
- No networking
- No third-party libraries
- No CLI frameworks (Typer, Click, Rich, etc.)
- Pure Python I/O only (`input()` and `print()`)

## Technology Stack

- **Python 3.13+**
- Standard library only (Phase I)
- UV as recommended package manager

## Task Execution Rules

1. One task = one Claude Code execution
2. Execute tasks strictly in order
3. If output is incorrect, update spec/plan/tasks — not code directly
4. Log all executions in `specs/[feature]/implement.md`

## Code Style

- Keep code simple and readable
- Avoid over-engineering
- Use meaningful names
- Include docstrings referencing spec sections
- No deep module hierarchies in Phase I

## When Stuck

If specifications are incomplete or ambiguous:
1. Stop and request clarification
2. Do not assume or invent behavior
3. Update spec before proceeding
