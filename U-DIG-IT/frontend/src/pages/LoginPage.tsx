import { useEffect } from 'react'
import { useForm } from 'react-hook-form'
import { useLocation, useNavigate, Link } from 'react-router-dom'

import { Card } from '../components/ui/Card'
import { InputField } from '../components/ui/InputField'
import { Button } from '../components/ui/Button'
import { useAuth } from '../hooks/useAuth'

interface LoginFormFields {
  email: string
  password: string
}

export const LoginPage = () => {
  const { login, isAuthenticated } = useAuth()
  const navigate = useNavigate()
  const location = useLocation()
  const fromPath = (location.state as { from?: string } | null)?.from ?? '/dashboard'

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<LoginFormFields>({
    defaultValues: { email: '', password: '' },
  })

  useEffect(() => {
    if (isAuthenticated) {
      navigate('/dashboard', { replace: true })
    }
  }, [isAuthenticated, navigate])

  const onSubmit = handleSubmit(async (values) => {
    await login(values.email, values.password)
    navigate(fromPath, { replace: true })
  })

  return (
    <div className="section" style={{ paddingTop: '3rem' }}>
      <div className="container" style={{ maxWidth: '420px' }}>
        <Card>
          <h1 style={{ marginTop: 0 }}>Welcome back</h1>
          <p style={{ color: 'var(--color-text-muted)' }}>Log in with your reservation credentials to access the operations dashboard.</p>
          <form onSubmit={onSubmit} style={{ display: 'grid', gap: '1rem', marginTop: '1.5rem' }}>
            <InputField
              label="Email"
              type="email"
              placeholder="you@company.com"
              error={errors.email?.message}
              {...register('email', { required: 'Email is required' })}
            />
            <InputField
              label="Password"
              type="password"
              placeholder="••••••••"
              error={errors.password?.message}
              {...register('password', { required: 'Password is required' })}
            />
            <Button type="submit" disabled={isSubmitting}>
              {isSubmitting ? 'Signing in…' : 'Sign in'}
            </Button>
          </form>
          <p style={{ marginTop: '1.5rem', color: 'var(--color-text-muted)' }}>
            Need access? <Link to="/register">Create an account</Link>
          </p>
        </Card>
      </div>
    </div>
  )
}
