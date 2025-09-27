/**
 * API test fixtures and mock data
 */
import { CatalogResponse, Equipment, Category, Location } from '@/types'

export const mockCategory: Category = {
  id: 1,
  name: 'Excavators',
  slug: 'excavators',
  description: 'Heavy construction equipment',
  icon: 'excavator-icon'
}

export const mockLocation: Location = {
  id: 1,
  name: 'Main Depot',
  address: '123 Construction Way',
  city: 'Test City',
  state: 'TS',
  zipCode: '12345',
  phone: '555-0123',
  email: 'depot@test.com'
}

export const mockEquipment: Equipment = {
  id: 1,
  name: 'Test Excavator',
  slug: 'test-excavator',
  description: 'A test excavator for testing',
  dailyRate: 500.00,
  categoryId: 1,
  locationId: 1,
  isAvailable: true,
  specifications: {
    'Engine Power': '200 HP',
    'Operating Weight': '20,000 lbs',
    'Bucket Capacity': '2.5 cubic yards'
  },
  tags: ['heavy-duty', 'construction'],
  media: []
}

export const mockCatalogResponse: CatalogResponse = {
  categories: [mockCategory],
  featured: [mockEquipment],
  equipment: [mockEquipment]
}

export const mockUser = {
  id: 1,
  email: 'test@example.com',
  fullName: 'Test User',
  role: 'customer' as const,
  isActive: true
}

export const mockTokenResponse = {
  accessToken: 'mock-jwt-token',
  tokenType: 'Bearer',
  expiresIn: 86400
}

export const mockReservation = {
  id: 1,
  reservationCode: 'RES-001',
  equipmentId: 1,
  customerId: 1,
  startDate: '2024-01-01',
  endDate: '2024-01-07',
  totalAmount: 3500.00,
  status: 'confirmed' as const,
  notes: 'Test reservation'
}

export const mockDashboardData = {
  totalReservations: 25,
  totalRevenue: 125000.00,
  topEquipment: [
    { id: 1, name: 'Test Excavator', revenue: 50000.00 },
    { id: 2, name: 'Test Bulldozer', revenue: 30000.00 }
  ],
  recentReservations: [mockReservation]
}

