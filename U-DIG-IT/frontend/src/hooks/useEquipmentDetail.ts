import { useQuery } from '@tanstack/react-query'

import { checkEquipmentAvailability, fetchEquipmentDetail } from '../api/endpoints'
import type { AvailabilityResponse, EquipmentDetail } from '../types'

export const equipmentKeys = {
  detail: (slug: string) => ['equipment', slug] as const,
  availability: (slug: string, startDate: string, endDate: string) =>
    ['equipment', slug, 'availability', startDate, endDate] as const,
}

export const useEquipmentDetail = (slug: string) =>
  useQuery<EquipmentDetail>({
    queryKey: equipmentKeys.detail(slug),
    queryFn: () => fetchEquipmentDetail(slug),
    enabled: Boolean(slug),
  })

export const fetchAvailability = async (slug: string, startDate: string, endDate: string) =>
  checkEquipmentAvailability(slug, { startDate, endDate })

export const availabilityKey = (slug: string, startDate: string, endDate: string) =>
  equipmentKeys.availability(slug, startDate, endDate)
