export type UserRole = 'admin' | 'manager' | 'customer'

export interface Category {
  id: number
  slug: string
  name: string
  description?: string | null
  icon?: string | null
  equipmentCount: number
}

export interface EquipmentMedia {
  id: number
  url: string
  altText?: string | null
  isPrimary: boolean
  mediaType: string
}

export interface Review {
  id: number
  authorName: string
  authorCompany?: string | null
  rating: number
  headline?: string | null
  comment?: string | null
  published: boolean
  createdAt?: string | null
}

export interface EquipmentSummary {
  id: number
  name: string
  slug: string
  summary: string
  description?: string | null
  dailyRate: number
  depositAmount: number
  featured: boolean
  tags: string[]
  primaryImage?: string | null
  averageRating?: number | null
  reviewCount: number
  category: {
    slug: string
    name: string
    description?: string | null
    icon?: string | null
  }
}

export interface EquipmentDetail extends EquipmentSummary {
  specifications?: Record<string, string | number | null> | null
  gallery: EquipmentMedia[]
  maintenanceStatuses: string[]
  reviews: Review[]
}

export interface CatalogResponse {
  categories: Category[]
  featured: EquipmentSummary[]
  equipment: EquipmentSummary[]
  availableTags: string[]
}

export interface AvailabilityResponse {
  equipmentId: number
  equipmentName: string
  availableQuantity: number
  isAvailable: boolean
}

export interface LandingStats {
  totalInventory: number
  activeCustomers: number
  locationsServed: number
  onTimeDeliveryRate: number
  averageRating: number
  featuredTestimonials: Review[]
}

export interface Location {
  id: number
  name: string
  addressLine1: string
  addressLine2?: string | null
  city: string
  state: string
  postalCode: string
  country: string
  phoneNumber?: string | null
}

export interface ReservationPayload {
  equipmentSlug: string
  locationId: number
  startDate: string
  endDate: string
  customerName: string
  customerEmail: string
  customerPhone?: string
  notes?: string
  customerId?: number | null
}

export interface ReservationSummary {
  reservationCode: string
  status: string
  paymentStatus: string
  startDate: string
  endDate: string
  totalDays: number
  subtotalAmount: number
  depositAmount: number
  totalAmount: number
  equipment: EquipmentSummary
}

export interface ReservationSuccessResponse {
  reservation: ReservationSummary
  message: string
}

export interface AnalyticsSummary {
  date: string
  totalReservations: number
  totalRevenue: number
  newCustomers: number
  averageOrderValue: number
  utilizationRate: number
}

export interface TopEquipmentPerformance {
  equipment: EquipmentSummary
  revenue: number
  reservationCount: number
}

export interface DashboardSnapshot {
  reservations: ReservationSummary[]
  analytics: AnalyticsSummary[]
  topEquipment: TopEquipmentPerformance[]
}

export interface TokenResponse {
  accessToken: string
  tokenType: string
  expiresIn: number
}

export interface AuthUser {
  id: number
  email: string
  fullName: string
  role: UserRole
  isActive: boolean
  customerProfile?: {
    id: number
    phoneNumber?: string | null
    companyName?: string | null
    preferredContactMethod?: string | null
    loyaltyTier: string
  } | null
}
