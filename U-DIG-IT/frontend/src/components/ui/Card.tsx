import clsx from 'clsx'
import type { HTMLAttributes } from 'react'

export const Card = ({ className, ...props }: HTMLAttributes<HTMLDivElement>) => (
  <div className={clsx('card', className)} {...props} />
)
