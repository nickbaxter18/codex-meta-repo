import { useQuery } from '@tanstack/react-query'

import { fetchCatalog } from '../api/endpoints'
import type { CatalogResponse } from '../types'

type CatalogFilterOptions = { category?: string | null; search?: string | null; tag?: string | null }

export const catalogKeys = {
  all: ['catalog'] as const,
  filters: (filters?: CatalogFilterOptions) =>
    [...catalogKeys.all, filters?.category ?? 'all', filters?.search ?? '', filters?.tag ?? ''] as const,
}

export const useCatalog = (filters?: CatalogFilterOptions) => {
  return useQuery<CatalogResponse>({
    queryKey: catalogKeys.filters(filters),
    queryFn: () => fetchCatalog(filters),
  })
}
