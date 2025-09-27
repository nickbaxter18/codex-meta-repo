import { Navigate, Outlet, useLocation } from 'react-router-dom'

import { useAuth } from '../../hooks/useAuth'

interface ProtectedRouteProps {
  roles?: Array<'admin' | 'manager' | 'customer'>
}

export const ProtectedRoute = ({ roles }: ProtectedRouteProps) => {
  const location = useLocation()
  const { isAuthenticated, user, loading } = useAuth()

  if (loading) {
    return (
      <div className="container" style={{ padding: '4rem 0', textAlign: 'center' }}>
        <p>Preparing your workspace…</p>
      </div>
    )
  }

  if (!isAuthenticated) {
    return <Navigate to="/login" replace state={{ from: location }} />
  }

  if (roles && user && !roles.includes(user.role)) {
    return <Navigate to="/" replace />
  }

  return <Outlet />
}
