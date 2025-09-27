import { useEffect } from 'react'
import { useForm } from 'react-hook-form'
import { useNavigate, Link } from 'react-router-dom'

import { Card } from '../components/ui/Card'
import { InputField } from '../components/ui/InputField'
import { Button } from '../components/ui/Button'
import { useAuth } from '../hooks/useAuth'

interface RegisterFormFields {
  email: string
  fullName: string
  password: string
  phoneNumber?: string
  companyName?: string
}

export const RegisterPage = () => {
  const { register: registerUser, isAuthenticated } = useAuth()
  const navigate = useNavigate()

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<RegisterFormFields>({
    defaultValues: { email: '', fullName: '', password: '' },
  })

  useEffect(() => {
    if (isAuthenticated) {
      navigate('/dashboard', { replace: true })
    }
  }, [isAuthenticated, navigate])

  const onSubmit = handleSubmit(async (values) => {
    await registerUser(values)
    navigate('/dashboard', { replace: true })
  })

  return (
    <div className="section" style={{ paddingTop: '3rem' }}>
      <div className="container" style={{ maxWidth: '520px' }}>
        <Card>
          <h1 style={{ marginTop: 0 }}>Create your operations account</h1>
          <p style={{ color: 'var(--color-text-muted)' }}>
            Unlock fleet reservations, live logistics tracking, and utilization dashboards tailored to your projects.
          </p>
          <form onSubmit={onSubmit} style={{ display: 'grid', gap: '1rem', marginTop: '1.5rem' }}>
            <InputField
              label="Full name"
              placeholder="Jordan Michaels"
              error={errors.fullName?.message}
              {...register('fullName', { required: 'Full name is required' })}
            />
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
              placeholder="Minimum 8 characters"
              error={errors.password?.message}
              {...register('password', { required: 'Password is required', minLength: { value: 8, message: 'Use at least 8 characters' } })}
            />
            <InputField
              label="Phone number"
              placeholder="Optional contact number"
              {...register('phoneNumber')}
            />
            <InputField
              label="Company"
              placeholder="Optional company name"
              {...register('companyName')}
            />
            <Button type="submit" disabled={isSubmitting}>
              {isSubmitting ? 'Creating account…' : 'Create account'}
            </Button>
          </form>
          <p style={{ marginTop: '1.5rem', color: 'var(--color-text-muted)' }}>
            Already have credentials? <Link to="/login">Sign in</Link>
          </p>
        </Card>
      </div>
    </div>
  )
}
