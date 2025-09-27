import clsx from 'clsx'
import type { InputHTMLAttributes } from 'react'

type Props = InputHTMLAttributes<HTMLInputElement> & {
  label?: string
  helperText?: string
  error?: string
}

export const InputField = ({ label, helperText, error, className, id, ...props }: Props) => {
  const normalisedLabel = label?.toLowerCase().replace(/[^a-z0-9]+/g, '-') ?? 'input'
  const inputId = id ?? props.name?.toString() ?? 'field-' + normalisedLabel
  return (
    <label htmlFor={inputId} className={clsx('field', className)} style={{ display: 'block' }}>
      {label && (
        <span style={{ display: 'block', marginBottom: '0.35rem', fontWeight: 600 }}>{label}</span>
      )}
      <input id={inputId} {...props} />
      {helperText && !error && (
        <small style={{ display: 'block', marginTop: '0.35rem', color: 'var(--color-text-muted)' }}>{helperText}</small>
      )}
      {error && (
        <small style={{ display: 'block', marginTop: '0.35rem', color: '#dc2626' }}>{error}</small>
      )}
    </label>
  )
}
