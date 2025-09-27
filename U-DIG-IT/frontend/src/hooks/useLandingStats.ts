import { useQuery } from '@tanstack/react-query'

import { fetchLandingStats } from '../api/endpoints'
import type { LandingStats } from '../types'

export const landingStatsKey = ['landing-stats']

export const useLandingStats = () =>
  useQuery<LandingStats>({
    queryKey: landingStatsKey,
    queryFn: fetchLandingStats,
  })
