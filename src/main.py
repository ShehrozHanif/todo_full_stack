#!/usr/bin/env python3
"""
Phase I — In-Memory CLI Todo Application

A pure Python, in-memory CLI application demonstrating Spec-Driven Development.
All data exists only in memory and is lost on application exit.

Spec Reference: specs/001-in-memory-cli-todo/spec.md
Plan Reference: specs/001-in-memory-cli-todo/plan.md
"""

from datetime import datetime
from typing import Optional


# =============================================================================
# T1-003: Task Domain Model
# =============================================================================

class Task:
    """
    Core domain entity representing a Todo task.

    Spec Reference: Domain Model -> Task Entity
    """

    def __init__(self, task_id: int, title: str, description: str = ""):
        self.id: int = task_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()

    def __str__(self) -> str:
        """Readable string representation for CLI output."""
        status = "[x]" if self.completed else "[ ]"
        desc_part = f" - {self.description}" if self.description else ""
        return f"{status} {self.id}. {self.title}{desc_part}"

    def detailed_str(self) -> str:
        """Detailed representation including timestamps."""
        status = "Completed" if self.completed else "Pending"
        lines = [
            f"  ID:          {self.id}",
            f"  Title:       {self.title}",
            f"  Description: {self.description if self.description else '(none)'}",
            f"  Status:      {status}",
            f"  Created:     {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}",
            f"  Updated:     {self.updated_at.strftime('%Y-%m-%d %H:%M:%S')}",
        ]
        return "\n".join(lines)


# =============================================================================
# T1-004: In-Memory Task Store
# =============================================================================

class TaskStore:
    """
    In-memory task store responsible for managing tasks.

    Spec Reference: Data Lifecycle Rules, FR-1 -> FR-5
    Plan Reference: Core Components -> In-Memory Task Store
    """

    def __init__(self):
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def create(self, title: str, description: str = "") -> Task:
        """Create a new task with sequential ID."""
        task = Task(self._next_id, title, description)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def list_all(self) -> list[Task]:
        """Return all tasks sorted by ID in ascending order."""
        return sorted(self._tasks.values(), key=lambda t: t.id)

    def get(self, task_id: int) -> Optional[Task]:
        """Get a task by ID, returns None if not found."""
        return self._tasks.get(task_id)

    def update(self, task_id: int, title: Optional[str] = None,
               description: Optional[str] = None) -> Optional[Task]:
        """Update a task's title and/or description."""
        task = self._tasks.get(task_id)
        if task is None:
            return None

        if title is not None and title.strip():
            task.title = title.strip()
        if description is not None:
            task.description = description.strip()

        task.updated_at = datetime.now()
        return task

    def complete(self, task_id: int) -> Optional[Task]:
        """Mark a task as completed."""
        task = self._tasks.get(task_id)
        if task is None:
            return None

        task.completed = True
        task.updated_at = datetime.now()
        return task

    def delete(self, task_id: int) -> bool:
        """Delete a task by ID. Returns True if deleted, False if not found."""
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False


# =============================================================================
# T1-005 to T1-011: CLI Controller and Application Lifecycle
# =============================================================================

class TodoCLI:
    """
    CLI controller for the Todo application.

    Spec Reference: CLI Interaction Model
    Plan Reference: CLI Controller, Application Lifecycle
    """

    MENU = """
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
"""

    def __init__(self):
        self.store = TaskStore()
        self.running = True

    def display_menu(self) -> None:
        """Display the main menu."""
        print(self.MENU)

    def get_input(self, prompt: str) -> str:
        """Get input from user with prompt."""
        return input(prompt).strip()

    def get_task_id(self) -> Optional[int]:
        """Get and validate task ID from user input."""
        try:
            task_id = int(self.get_input("Enter task ID: "))
            return task_id
        except ValueError:
            print("\nError: Please enter a valid number.")
            return None

    # T1-005: Create Task Flow
    def create_task(self) -> None:
        """
        Handle task creation flow.

        Spec Reference: FR-1: Create Task
        """
        print("\n--- Add New Task ---\n")

        title = self.get_input("Enter task title: ")
        if not title:
            print("\nError: Title cannot be empty.")
            return

        description = self.get_input("Enter task description (optional): ")

        task = self.store.create(title, description)

        print(f"\nTask created successfully!")
        print(task.detailed_str())

    # T1-006: List Tasks Flow
    def list_tasks(self) -> None:
        """
        Handle listing all tasks.

        Spec Reference: FR-2: List Tasks
        """
        print("\n--- All Tasks ---\n")

        tasks = self.store.list_all()

        if not tasks:
            print("No tasks found. Add a task to get started!")
            return

        for task in tasks:
            print(task)

        print(f"\nTotal: {len(tasks)} task(s)")

    # T1-007: Update Task Flow
    def update_task(self) -> None:
        """
        Handle task update flow.

        Spec Reference: FR-3: Update Task
        """
        print("\n--- Update Task ---\n")

        task_id = self.get_task_id()
        if task_id is None:
            return

        task = self.store.get(task_id)
        if task is None:
            print(f"\nError: Task with ID {task_id} not found.")
            return

        print(f"\nCurrent task:")
        print(task.detailed_str())

        print("\n(Press Enter to keep current value)")
        new_title = self.get_input(f"New title [{task.title}]: ")
        new_description = self.get_input(f"New description [{task.description or '(none)'}]: ")

        # Check if any update was provided
        if not new_title and new_description == "":
            # User pressed Enter for both - check if they want to clear description
            confirm = self.get_input("No changes provided. Keep current values? (y/n): ")
            if confirm.lower() != 'n':
                print("\nNo changes made.")
                return

        updated = self.store.update(
            task_id,
            title=new_title if new_title else None,
            description=new_description if new_description else None
        )

        if updated:
            print(f"\nTask updated successfully!")
            print(updated.detailed_str())

    # T1-008: Complete Task Flow
    def complete_task(self) -> None:
        """
        Handle marking a task as completed.

        Spec Reference: FR-4: Complete Task
        """
        print("\n--- Complete Task ---\n")

        task_id = self.get_task_id()
        if task_id is None:
            return

        task = self.store.complete(task_id)
        if task is None:
            print(f"\nError: Task with ID {task_id} not found.")
            return

        print(f"\nTask marked as completed!")
        print(task.detailed_str())

    # T1-009: Delete Task Flow
    def delete_task(self) -> None:
        """
        Handle task deletion flow.

        Spec Reference: FR-5: Delete Task
        """
        print("\n--- Delete Task ---\n")

        task_id = self.get_task_id()
        if task_id is None:
            return

        task = self.store.get(task_id)
        if task is None:
            print(f"\nError: Task with ID {task_id} not found.")
            return

        print(f"\nTask to delete:")
        print(task.detailed_str())

        confirm = self.get_input("\nAre you sure you want to delete this task? (y/n): ")
        if confirm.lower() != 'y':
            print("\nDeletion cancelled.")
            return

        if self.store.delete(task_id):
            print(f"\nTask {task_id} deleted successfully!")

    # T1-011: Graceful Exit
    def exit_application(self) -> None:
        """
        Handle graceful application exit.

        Spec Reference: FR-6: Exit Application
        """
        print("\n========================================")
        print("  Thank you for using Todo CLI!")
        print("  All tasks have been cleared.")
        print("  Goodbye!")
        print("========================================\n")
        self.running = False

    # T1-010: CLI Menu & Control Loop
    def run(self) -> None:
        """
        Main application loop.

        Spec Reference: CLI Interaction Model
        Plan Reference: Application Lifecycle
        """
        print("\nWelcome to the Phase I In-Memory Todo CLI!")
        print("All tasks exist only in memory and will be lost on exit.")

        while self.running:
            self.display_menu()
            choice = self.get_input("Select an option (1-6): ")

            if choice == "1":
                self.create_task()
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.complete_task()
            elif choice == "5":
                self.delete_task()
            elif choice == "6":
                self.exit_application()
            else:
                print("\nError: Invalid option. Please select 1-6.")


# =============================================================================
# Application Entry Point
# =============================================================================

def main() -> None:
    """Application entry point."""
    try:
        app = TodoCLI()
        app.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted. Goodbye!")
    except EOFError:
        print("\n\nInput stream ended. Goodbye!")


if __name__ == "__main__":
    main()
