'use client';

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from './context/AuthContext';

export default function Home() {
  const router = useRouter();
  const { user, isLoading } = useAuth();

  useEffect(() => {
    if (!isLoading) {
      if (user) {
        router.push('/tasks');
      } else {
        router.push('/login');
      }
    }
  }, [user, isLoading, router]);

  return (
    <div className="container" style={{ textAlign: 'center', marginTop: '100px' }}>
      <h1>Todo Full-Stack App</h1>
      <p>Loading...</p>
    </div>
  );
}
