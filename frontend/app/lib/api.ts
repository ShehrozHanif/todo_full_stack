/**
 * API client for backend communication.
 *
 * Spec Reference: REST API Endpoint Specification
 */

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export interface User {
  id: number;
  email: string;
  username: string;
  is_active: boolean;
  created_at: string;
}

export interface Task {
  id: number;
  title: string;
  description: string | null;
  completed: boolean;
  owner_id: number;
  created_at: string;
  updated_at: string;
}

export interface LoginCredentials {
  username: string;
  password: string;
}

export interface RegisterData {
  email: string;
  username: string;
  password: string;
}

export interface TaskCreate {
  title: string;
  description?: string;
}

export interface TaskUpdate {
  title?: string;
  description?: string;
  completed?: boolean;
}

class ApiError extends Error {
  constructor(public status: number, message: string) {
    super(message);
    this.name = 'ApiError';
  }
}

function getToken(): string | null {
  if (typeof window !== 'undefined') {
    return localStorage.getItem('token');
  }
  return null;
}

async function request<T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<T> {
  const token = getToken();

  const headers: HeadersInit = {
    'Content-Type': 'application/json',
    ...options.headers,
  };

  if (token) {
    (headers as Record<string, string>)['Authorization'] = `Bearer ${token}`;
  }

  const response = await fetch(`${API_URL}${endpoint}`, {
    ...options,
    headers,
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: 'Unknown error' }));
    throw new ApiError(response.status, error.detail || 'Request failed');
  }

  // Handle 204 No Content
  if (response.status === 204) {
    return null as T;
  }

  return response.json();
}

// Auth API
export async function login(credentials: LoginCredentials): Promise<{ access_token: string }> {
  const formData = new URLSearchParams();
  formData.append('username', credentials.username);
  formData.append('password', credentials.password);

  const response = await fetch(`${API_URL}/api/auth/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: formData,
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: 'Unknown error' }));
    throw new ApiError(response.status, error.detail || 'Login failed');
  }

  return response.json();
}

export async function register(data: RegisterData): Promise<User> {
  return request<User>('/api/auth/register', {
    method: 'POST',
    body: JSON.stringify(data),
  });
}

export async function getCurrentUser(): Promise<User> {
  return request<User>('/api/auth/me');
}

// Tasks API
export async function getTasks(): Promise<Task[]> {
  return request<Task[]>('/api/tasks/');
}

export async function createTask(data: TaskCreate): Promise<Task> {
  return request<Task>('/api/tasks/', {
    method: 'POST',
    body: JSON.stringify(data),
  });
}

export async function updateTask(id: number, data: TaskUpdate): Promise<Task> {
  return request<Task>(`/api/tasks/${id}`, {
    method: 'PUT',
    body: JSON.stringify(data),
  });
}

export async function completeTask(id: number): Promise<Task> {
  return request<Task>(`/api/tasks/${id}/complete`, {
    method: 'PATCH',
  });
}

export async function deleteTask(id: number): Promise<void> {
  return request<void>(`/api/tasks/${id}`, {
    method: 'DELETE',
  });
}

export { ApiError };
