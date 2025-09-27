import { format, parseISO } from 'date-fns'

export const formatCurrency = (value: number, currency = 'USD') =>
  new Intl.NumberFormat('en-US', { style: 'currency', currency }).format(value)

export const formatDateShort = (value: string | Date) => {
  const date = typeof value === 'string' ? parseISO(value) : value
  return format(date, 'MMM d, yyyy')
}

export const formatPercent = (value: number) => `${value.toFixed(1)}%`

export const truncate = (value: string, length = 120) =>
  value.length > length ? `${value.slice(0, length)}...` : value
