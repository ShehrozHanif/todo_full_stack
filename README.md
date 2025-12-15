# Hackathon II: The Evolution of Todo

A demonstration of **Spec-Driven Development (SDD)** applied to the evolution of a real software system — from a simple CLI application to a cloud-native, AI-powered, event-driven system.

## Project Overview

This project follows the **Spec-Kit Plus** lifecycle:

```
Constitution -> Specification -> Plan -> Tasks -> Implementation
```

All code is generated via **Claude Code** based on approved specifications. No manual coding is permitted.

## Current Phase: Phase I — In-Memory CLI Todo Application

Phase I establishes the **foundational Todo domain** using a pure Python, in-memory CLI application.

### Features

- Create, list, update, complete, and delete tasks
- Sequential task IDs starting from 1
- Timestamps for creation and updates
- In-memory storage (all data lost on exit)
- Menu-based CLI interaction

### Constraints

- **No persistence** — all tasks exist only in memory
- **No external dependencies** — pure Python standard library
- **No frameworks** — simple, readable code

## Requirements

- **Python 3.13+**
- No additional packages required

## Recommended Tool

**UV** is the recommended Python environment and package manager for this project.

```bash
# Install UV (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or on Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Running the Application

### Using Python directly

```bash
python src/main.py
```

### Using UV

```bash
uv run src/main.py
```

## Usage

The application presents a menu-based interface:

```
========================================
        TODO CLI APPLICATION
========================================

  1. Add Task
  2. List Tasks
  3. Update Task
  4. Complete Task
  5. Delete Task
  6. Exit

========================================
```

### Demo Flow

1. Start the application
2. Add multiple tasks (option 1)
3. List tasks to verify ordering (option 2)
4. Update a task (option 3)
5. Complete a task (option 4)
6. Delete a task (option 5)
7. Exit the application (option 6)
8. Restart to confirm all tasks are cleared

## Project Structure

```
todo_full_stack/
├── .specify/                    # Spec-Kit Plus configuration
│   ├── memory/
│   │   └── constitution.md      # Project constitution
│   └── templates/               # Specification templates
├── specs/
│   └── 001-in-memory-cli-todo/  # Phase I specifications
│       ├── spec.md              # Feature specification
│       ├── plan.md              # Implementation plan
│       ├── tasks.md             # Task breakdown
│       └── implement.md         # Execution log
├── src/
│   └── main.py                  # Phase I implementation
├── CLAUDE.md                    # Claude Code instructions
└── README.md                    # This file
```

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
| I | In-Memory CLI Todo App | In Progress |
| II | Full-Stack Web Application | Planned |
| III | AI-Powered Todo Chatbot | Planned |
| IV | Local Kubernetes Deployment | Planned |
| V | Cloud-Native Event-Driven System | Planned |

## License

This project is part of Hackathon II.
