'use client';

import { useState, FormEvent, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import { useAuth } from '../context/AuthContext';
import { login as apiLogin, ApiError } from '../lib/api';

export default function LoginPage() {
  const router = useRouter();
  const { login, user, isLoading } = useAuth();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => {
    if (!isLoading && user) {
      router.push('/tasks');
    }
  }, [user, isLoading, router]);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    setError('');
    setSubmitting(true);

    try {
      const response = await apiLogin({ username, password });
      await login(response.access_token);
      router.push('/tasks');
    } catch (err) {
      if (err instanceof ApiError) {
        setError(err.message);
      } else {
        setError('An unexpected error occurred');
      }
    } finally {
      setSubmitting(false);
    }
  };

  if (isLoading) {
    return <div className="container">Loading...</div>;
  }

  return (
    <div className="auth-container">
      <div className="card">
        <h1 style={{ marginBottom: '24px', textAlign: 'center' }}>Login</h1>

        {error && <div className="error">{error}</div>}

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="username">Username</label>
            <input
              type="text"
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
              autoComplete="username"
            />
          </div>

          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              autoComplete="current-password"
            />
          </div>

          <button
            type="submit"
            className="btn btn-primary"
            style={{ width: '100%' }}
            disabled={submitting}
          >
            {submitting ? 'Logging in...' : 'Login'}
          </button>
        </form>

        <p style={{ marginTop: '16px', textAlign: 'center' }}>
          Don&apos;t have an account?{' '}
          <Link href="/register" className="link">
            Register
          </Link>
        </p>
      </div>
    </div>
  );
}
