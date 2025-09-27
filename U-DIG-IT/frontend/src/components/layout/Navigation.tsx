import { NavLink } from 'react-router-dom'

import { Button } from '../ui/Button'
import { useAuth } from '../../hooks/useAuth'

const navLinkClass = ({ isActive }: { isActive: boolean }) =>
  ['nav-link', isActive ? 'active' : ''].filter(Boolean).join(' ')

export const Navigation = () => {
  const { isAuthenticated, logout } = useAuth()

  return (
    <header className="container">
      <nav className="navbar">
        <NavLink to="/" className="brand" style={{ fontWeight: 700, fontSize: '1.25rem' }}>
          U-DIG-IT
        </NavLink>
        <div className="nav-links">
          <NavLink to="/catalog" className={navLinkClass}>
            Catalog
          </NavLink>
          <NavLink to="/solutions" className={navLinkClass}>
            Solutions
          </NavLink>
          <NavLink to="/about" className={navLinkClass}>
            About
          </NavLink>
          {isAuthenticated && (
            <NavLink to="/dashboard" className={navLinkClass}>
              Dashboard
            </NavLink>
          )}
        </div>
        <div className="nav-actions" style={{ display: 'flex', gap: '0.75rem', alignItems: 'center' }}>
          {isAuthenticated ? (
            <Button variant="outline" onClick={logout}>
              Sign out
            </Button>
          ) : (
            <>
              <NavLink to="/login" className={navLinkClass}>
                Log in
              </NavLink>
              <NavLink to="/register">
                <Button>Start renting</Button>
              </NavLink>
            </>
          )}
        </div>
      </nav>
    </header>
  )
}
