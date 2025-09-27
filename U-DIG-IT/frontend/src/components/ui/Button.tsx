import clsx from 'clsx'
import type { ButtonHTMLAttributes, ReactNode } from 'react'

export interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'outline'
  icon?: ReactNode
}

export const Button = ({ variant = 'primary', icon, className, children, ...props }: ButtonProps) => (
  <button className={clsx('btn', variant === 'primary' ? 'btn-primary' : 'btn-outline', className)} {...props}>
    {icon}
    {children}
  </button>
)
