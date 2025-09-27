import { useQuery } from '@tanstack/react-query'

import { fetchLocations } from '../api/endpoints'
import type { Location } from '../types'

export const locationsKey = ['locations']

export const useLocations = () =>
  useQuery<Location[]>({
    queryKey: locationsKey,
    queryFn: fetchLocations,
  })
