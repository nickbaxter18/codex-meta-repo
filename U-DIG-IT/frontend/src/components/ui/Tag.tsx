import clsx from 'clsx'
import type { HTMLAttributes } from 'react'

export const Tag = ({ className, ...props }: HTMLAttributes<HTMLSpanElement>) => (
  <span className={clsx('tag', className)} {...props} />
)
