import { useQuery } from '@tanstack/react-query'

import { fetchDashboardSnapshot } from '../api/endpoints'
import type { DashboardSnapshot } from '../types'

export const dashboardKey = ['dashboard-snapshot']

export const useDashboardSnapshot = () =>
  useQuery<DashboardSnapshot>({
    queryKey: dashboardKey,
    queryFn: fetchDashboardSnapshot,
  })
