'use client';

import { useState, useEffect, FormEvent } from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from '../context/AuthContext';
import {
  Task,
  getTasks,
  createTask,
  updateTask,
  deleteTask,
  ApiError,
} from '../lib/api';

/**
 * Format a date string to human-readable format (e.g., "Jan 15, 2025")
 */
function formatDate(dateString: string): string {
  const date = new Date(dateString);
  return date.toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
  });
}

export default function TasksPage() {
  const router = useRouter();
  const { user, isLoading, logout } = useAuth();
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // New task form
  const [showNewTaskForm, setShowNewTaskForm] = useState(false);
  const [newTitle, setNewTitle] = useState('');
  const [newDescription, setNewDescription] = useState('');
  const [creating, setCreating] = useState(false);

  // Edit task modal
  const [editingTask, setEditingTask] = useState<Task | null>(null);
  const [editTitle, setEditTitle] = useState('');
  const [editDescription, setEditDescription] = useState('');
  const [updating, setUpdating] = useState(false);

  useEffect(() => {
    if (!isLoading && !user) {
      router.push('/login');
    }
  }, [user, isLoading, router]);

  useEffect(() => {
    if (user) {
      fetchTasks();
    }
  }, [user]);

  const fetchTasks = async () => {
    try {
      const data = await getTasks();
      setTasks(data);
      setError('');
    } catch (err) {
      if (err instanceof ApiError && err.status === 401) {
        logout();
        router.push('/login');
      } else {
        setError('Failed to load tasks');
      }
    } finally {
      setLoading(false);
    }
  };

  const handleCreateTask = async (e: FormEvent) => {
    e.preventDefault();
    if (!newTitle.trim()) return;

    setCreating(true);
    try {
      const task = await createTask({
        title: newTitle.trim(),
        description: newDescription.trim() || undefined,
      });
      setTasks([task, ...tasks]);
      setNewTitle('');
      setNewDescription('');
      setShowNewTaskForm(false);
      setError('');
    } catch (err) {
      if (err instanceof ApiError) {
        setError(err.message);
      } else {
        setError('Failed to create task');
      }
    } finally {
      setCreating(false);
    }
  };

  /**
   * Toggle task completion status (bidirectional: check and uncheck)
   * Uses PUT /api/tasks/{id} with completed field
   */
  const handleToggleComplete = async (task: Task) => {
    try {
      const updated = await updateTask(task.id, {
        completed: !task.completed,
      });
      setTasks(tasks.map((t) => (t.id === task.id ? updated : t)));
      setError('');
    } catch (err) {
      if (err instanceof ApiError) {
        setError(err.message);
      } else {
        setError('Failed to update task status');
      }
    }
  };

  const handleUpdateTask = async (e: FormEvent) => {
    e.preventDefault();
    if (!editingTask || !editTitle.trim()) return;

    setUpdating(true);
    try {
      const updated = await updateTask(editingTask.id, {
        title: editTitle.trim(),
        description: editDescription.trim(),
      });
      setTasks(tasks.map((t) => (t.id === editingTask.id ? updated : t)));
      setEditingTask(null);
      setError('');
    } catch (err) {
      if (err instanceof ApiError) {
        setError(err.message);
      } else {
        setError('Failed to update task');
      }
    } finally {
      setUpdating(false);
    }
  };

  const handleDeleteTask = async (task: Task) => {
    if (!confirm('Are you sure you want to delete this task?')) return;

    try {
      await deleteTask(task.id);
      setTasks(tasks.filter((t) => t.id !== task.id));
      setError('');
    } catch (err) {
      if (err instanceof ApiError) {
        setError(err.message);
      } else {
        setError('Failed to delete task');
      }
    }
  };

  const openEditModal = (task: Task) => {
    setEditingTask(task);
    setEditTitle(task.title);
    setEditDescription(task.description || '');
  };

  const handleLogout = () => {
    logout();
    router.push('/login');
  };

  if (isLoading || loading) {
    return <div className="container">Loading...</div>;
  }

  if (!user) {
    return null;
  }

  return (
    <div>
      <header className="header">
        <h1>My Tasks</h1>
        <div className="header-actions">
          <span>Welcome, {user.username}</span>
          <button onClick={handleLogout} className="btn btn-secondary">
            Logout
          </button>
        </div>
      </header>

      <div className="container">
        {error && <div className="error">{error}</div>}

        {/* New Task Button/Form */}
        {!showNewTaskForm ? (
          <button
            onClick={() => setShowNewTaskForm(true)}
            className="btn btn-primary"
            style={{ marginBottom: '20px' }}
          >
            + Add New Task
          </button>
        ) : (
          <div className="card">
            <h2 style={{ marginBottom: '16px' }}>New Task</h2>
            <form onSubmit={handleCreateTask}>
              <div className="form-group">
                <label htmlFor="newTitle">Title</label>
                <input
                  type="text"
                  id="newTitle"
                  value={newTitle}
                  onChange={(e) => setNewTitle(e.target.value)}
                  required
                  placeholder="Enter task title"
                />
              </div>
              <div className="form-group">
                <label htmlFor="newDescription">Description (optional)</label>
                <textarea
                  id="newDescription"
                  value={newDescription}
                  onChange={(e) => setNewDescription(e.target.value)}
                  placeholder="Enter task description"
                  rows={3}
                />
              </div>
              <div style={{ display: 'flex', gap: '10px' }}>
                <button type="submit" className="btn btn-primary" disabled={creating}>
                  {creating ? 'Creating...' : 'Create Task'}
                </button>
                <button
                  type="button"
                  onClick={() => {
                    setShowNewTaskForm(false);
                    setNewTitle('');
                    setNewDescription('');
                  }}
                  className="btn btn-secondary"
                >
                  Cancel
                </button>
              </div>
            </form>
          </div>
        )}

        {/* Task List */}
        {tasks.length === 0 ? (
          <div className="empty-state">
            <p>No tasks yet. Create your first task!</p>
          </div>
        ) : (
          <ul className="task-list">
            {tasks.map((task) => (
              <li key={task.id} className={`task-item ${task.completed ? 'completed' : ''}`}>
                <input
                  type="checkbox"
                  className="task-checkbox"
                  checked={task.completed}
                  onChange={() => handleToggleComplete(task)}
                  title={task.completed ? 'Mark as incomplete' : 'Mark as complete'}
                />
                <div className="task-content">
                  <div className="task-title">{task.title}</div>
                  {task.description && (
                    <div className="task-description">{task.description}</div>
                  )}
                  <div className="task-meta">
                    {formatDate(task.created_at)} • <span className={`task-status ${task.completed ? 'status-completed' : 'status-incomplete'}`}>
                      {task.completed ? 'Completed' : 'Incomplete'}
                    </span>
                  </div>
                </div>
                <div className="task-actions">
                  {!task.completed && (
                    <button
                      onClick={() => openEditModal(task)}
                      className="btn btn-secondary"
                    >
                      Edit
                    </button>
                  )}
                  <button
                    onClick={() => handleDeleteTask(task)}
                    className="btn btn-danger"
                  >
                    Delete
                  </button>
                </div>
              </li>
            ))}
          </ul>
        )}
      </div>

      {/* Edit Modal */}
      {editingTask && (
        <div className="modal-overlay" onClick={() => setEditingTask(null)}>
          <div className="modal" onClick={(e) => e.stopPropagation()}>
            <div className="modal-header">
              <h2>Edit Task</h2>
              <button className="close-btn" onClick={() => setEditingTask(null)}>
                &times;
              </button>
            </div>
            <form onSubmit={handleUpdateTask}>
              <div className="form-group">
                <label htmlFor="editTitle">Title</label>
                <input
                  type="text"
                  id="editTitle"
                  value={editTitle}
                  onChange={(e) => setEditTitle(e.target.value)}
                  required
                />
              </div>
              <div className="form-group">
                <label htmlFor="editDescription">Description</label>
                <textarea
                  id="editDescription"
                  value={editDescription}
                  onChange={(e) => setEditDescription(e.target.value)}
                  rows={3}
                />
              </div>
              <div style={{ display: 'flex', gap: '10px' }}>
                <button type="submit" className="btn btn-primary" disabled={updating}>
                  {updating ? 'Saving...' : 'Save Changes'}
                </button>
                <button
                  type="button"
                  onClick={() => setEditingTask(null)}
                  className="btn btn-secondary"
                >
                  Cancel
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
