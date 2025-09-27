import { apiClient } from './client'
import {
  availabilitySchema,
  catalogResponseSchema,
  categorySchema,
  dashboardSnapshotSchema,
  equipmentDetailSchema,
  equipmentSummarySchema,
  landingStatsSchema,
  locationSchema,
  reservationSuccessSchema,
  tokenResponseSchema,
  userSchema,
} from './schemas'
import type {
  AvailabilityResponse,
  CatalogResponse,
  DashboardSnapshot,
  EquipmentDetail,
  LandingStats,
  Location,
  ReservationPayload,
  ReservationSuccessResponse,
  TokenResponse,
  AuthUser,
} from '../types'

export interface CatalogFilters {
  category?: string | null
  search?: string | null
  featured?: boolean
  tag?: string | null
}

export const fetchCatalog = async (filters: CatalogFilters = {}): Promise<CatalogResponse> => {
  const response = await apiClient.get('/api/catalog', {
    params: {
      category: filters.category ?? undefined,
      search: filters.search ?? undefined,
      tag: filters.tag ?? undefined,
    },
  })
  const parsed = catalogResponseSchema.parse(response.data)
  return parsed
}

export const fetchCategories = async () => {
  const response = await apiClient.get('/api/catalog/categories')
  return response.data.map((item: unknown) => categorySchema.parse(item))
}

export const fetchEquipment = async (filters: CatalogFilters = {}) => {
  const response = await apiClient.get('/api/catalog/equipment', {
    params: {
      category: filters.category ?? undefined,
      search: filters.search ?? undefined,
      featured: filters.featured ?? undefined,
      tag: filters.tag ?? undefined,
    },
  })
  return response.data.map((item: unknown) => equipmentSummarySchema.parse(item))
}

export const fetchEquipmentDetail = async (slug: string): Promise<EquipmentDetail> => {
  const response = await apiClient.get(`/api/catalog/equipment/${slug}`)
  return equipmentDetailSchema.parse(response.data)
}

export const checkEquipmentAvailability = async (
  slug: string,
  params: { startDate: string; endDate: string },
): Promise<AvailabilityResponse> => {
  const response = await apiClient.get(`/api/catalog/equipment/${slug}/availability`, {
    params: {
      start_date: params.startDate,
      end_date: params.endDate,
    },
  })
  return availabilitySchema.parse(response.data)
}

export const fetchLandingStats = async (): Promise<LandingStats> => {
  const response = await apiClient.get('/api/catalog/landing')
  return landingStatsSchema.parse(response.data)
}

export const fetchLocations = async (): Promise<Location[]> => {
  const response = await apiClient.get('/api/catalog/locations')
  return response.data.map((item: unknown) => locationSchema.parse(item))
}

export const submitReservation = async (
  payload: ReservationPayload,
): Promise<ReservationSuccessResponse> => {
  const response = await apiClient.post('/api/reservations', payload)
  return reservationSuccessSchema.parse(response.data)
}

export const fetchDashboardSnapshot = async (): Promise<DashboardSnapshot> => {
  const response = await apiClient.get('/api/analytics/dashboard')
  return dashboardSnapshotSchema.parse(response.data)
}

export const login = async (email: string, password: string): Promise<TokenResponse> => {
  const formData = new URLSearchParams()
  formData.append('username', email)
  formData.append('password', password)
  const response = await apiClient.post('/api/auth/login', formData, {
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  })
  return tokenResponseSchema.parse(response.data)
}

export const register = async (payload: {
  email: string
  fullName: string
  password: string
  phoneNumber?: string
  companyName?: string
}): Promise<TokenResponse> => {
  const response = await apiClient.post('/api/auth/register', {
    email: payload.email,
    full_name: payload.fullName,
    password: payload.password,
    phone_number: payload.phoneNumber,
    company_name: payload.companyName,
  })
  return tokenResponseSchema.parse(response.data)
}

export const fetchCurrentUser = async (): Promise<AuthUser> => {
  const response = await apiClient.get('/api/auth/me')
  return userSchema.parse(response.data)
}
