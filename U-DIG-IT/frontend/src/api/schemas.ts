import { z } from 'zod'

export const categorySchema = z
  .object({
    id: z.number(),
    slug: z.string(),
    name: z.string(),
    description: z.string().nullable().optional(),
    icon: z.string().nullable().optional(),
    equipment_count: z.number().default(0),
  })
  .transform(({ equipment_count, ...rest }) => ({
    ...rest,
    equipmentCount: equipment_count ?? 0,
  }))

export const equipmentSummarySchema = z
  .object({
    id: z.number(),
    name: z.string(),
    slug: z.string(),
    summary: z.string(),
    description: z.string().nullable().optional(),
    daily_rate: z.number(),
    deposit_amount: z.number(),
    featured: z.boolean().default(false),
    tags: z.array(z.string()).default([]),
    primary_image: z.string().nullable().optional(),
    average_rating: z.number().nullable().optional(),
    review_count: z.number().default(0),
    category: z.object({
      slug: z.string(),
      name: z.string(),
      description: z.string().nullable().optional(),
      icon: z.string().nullable().optional(),
    }),
  })
  .transform(
    ({
      daily_rate,
      deposit_amount,
      average_rating,
      primary_image,
      review_count,
      ...rest
    }) => ({
      ...rest,
      dailyRate: daily_rate,
      depositAmount: deposit_amount,
      averageRating: average_rating ?? null,
      primaryImage: primary_image ?? null,
      reviewCount: review_count ?? 0,
    }),
  )

const equipmentMediaSchema = z
  .object({
    id: z.number(),
    url: z.string(),
    alt_text: z.string().nullable().optional(),
    is_primary: z.boolean(),
    media_type: z.string(),
  })
  .transform(({ alt_text, is_primary, media_type, ...rest }) => ({
    ...rest,
    altText: alt_text ?? null,
    isPrimary: is_primary,
    mediaType: media_type,
  }))

const reviewSchema = z
  .object({
    id: z.number(),
    author_name: z.string(),
    author_company: z.string().nullable().optional(),
    rating: z.number(),
    headline: z.string().nullable().optional(),
    comment: z.string().nullable().optional(),
    published: z.boolean(),
    created_at: z.string().nullable().optional(),
  })
  .transform(({ author_name, author_company, created_at, ...rest }) => ({
    ...rest,
    authorName: author_name,
    authorCompany: author_company ?? null,
    createdAt: created_at ?? null,
  }))

export const equipmentDetailSchema = equipmentSummarySchema
  .extend({
    specifications: z.record(z.union([z.string(), z.number(), z.null()])).nullable().optional(),
    gallery: z.array(equipmentMediaSchema).default([]),
    maintenance_statuses: z.array(z.string()).default([]),
    reviews: z.array(reviewSchema).default([]),
  })
  .transform(({ maintenance_statuses, ...rest }) => ({
    ...rest,
    maintenanceStatuses: maintenance_statuses ?? [],
  }))

export const catalogResponseSchema = z
  .object({
    categories: z.array(categorySchema),
    featured: z.array(equipmentSummarySchema),
    equipment: z.array(equipmentSummarySchema),
    available_tags: z.array(z.string()).default([]),
  })
  .transform(({ available_tags, ...rest }) => ({
    ...rest,
    availableTags: available_tags ?? [],
  }))

export const availabilitySchema = z
  .object({
    equipment_id: z.number(),
    equipment_name: z.string(),
    available_quantity: z.number(),
    is_available: z.boolean(),
  })
  .transform(({ equipment_id, equipment_name, available_quantity, is_available }) => ({
    equipmentId: equipment_id,
    equipmentName: equipment_name,
    availableQuantity: available_quantity,
    isAvailable: is_available,
  }))

export const landingStatsSchema = z
  .object({
    total_inventory: z.number(),
    active_customers: z.number(),
    locations_served: z.number(),
    on_time_delivery_rate: z.number(),
    average_rating: z.number(),
    featured_testimonials: z.array(reviewSchema).default([]),
  })
  .transform(
    ({
      total_inventory,
      active_customers,
      locations_served,
      on_time_delivery_rate,
      average_rating,
      featured_testimonials,
    }) => ({
      totalInventory: total_inventory,
      activeCustomers: active_customers,
      locationsServed: locations_served,
      onTimeDeliveryRate: on_time_delivery_rate,
      averageRating: average_rating,
      featuredTestimonials: featured_testimonials ?? [],
    }),
  )

export const locationSchema = z
  .object({
    id: z.number(),
    name: z.string(),
    address_line1: z.string(),
    address_line2: z.string().nullable().optional(),
    city: z.string(),
    state: z.string(),
    postal_code: z.string(),
    country: z.string(),
    phone_number: z.string().nullable().optional(),
  })
  .transform(({ address_line1, address_line2, postal_code, phone_number, ...rest }) => ({
    ...rest,
    addressLine1: address_line1,
    addressLine2: address_line2 ?? null,
    postalCode: postal_code,
    phoneNumber: phone_number ?? null,
  }))

export const reservationSummarySchema = z
  .object({
    reservation_code: z.string(),
    status: z.string(),
    payment_status: z.string(),
    start_date: z.string(),
    end_date: z.string(),
    total_days: z.number(),
    subtotal_amount: z.number(),
    deposit_amount: z.number(),
    total_amount: z.number(),
    equipment: equipmentSummarySchema,
  })
  .transform(
    ({
      reservation_code,
      payment_status,
      start_date,
      end_date,
      total_days,
      subtotal_amount,
      deposit_amount,
      total_amount,
      ...rest
    }) => ({
      reservationCode: reservation_code,
      paymentStatus: payment_status,
      startDate: start_date,
      endDate: end_date,
      totalDays: total_days,
      subtotalAmount: subtotal_amount,
      depositAmount: deposit_amount,
      totalAmount: total_amount,
      ...rest,
    }),
  )

export const reservationSuccessSchema = z.object({
  reservation: reservationSummarySchema,
  message: z.string(),
})

export const analyticsSummarySchema = z
  .object({
    date: z.string(),
    total_reservations: z.number(),
    total_revenue: z.number(),
    new_customers: z.number(),
    average_order_value: z.number(),
    utilization_rate: z.number(),
  })
  .transform(
    ({
      total_reservations,
      total_revenue,
      new_customers,
      average_order_value,
      utilization_rate,
      ...rest
    }) => ({
      totalReservations: total_reservations,
      totalRevenue: total_revenue,
      newCustomers: new_customers,
      averageOrderValue: average_order_value,
      utilizationRate: utilization_rate,
      ...rest,
    }),
  )

export const topEquipmentSchema = z
  .object({
    equipment: equipmentSummarySchema,
    revenue: z.number(),
    reservation_count: z.number(),
  })
  .transform(({ reservation_count, ...rest }) => ({
    ...rest,
    reservationCount: reservation_count,
  }))

export const dashboardSnapshotSchema = z.object({
  reservations: z.array(reservationSummarySchema),
  analytics: z.array(analyticsSummarySchema),
  top_equipment: z.array(topEquipmentSchema),
})

export const userSchema = z
  .object({
    id: z.number(),
    email: z.string(),
    full_name: z.string(),
    role: z.enum(['admin', 'manager', 'customer']),
    is_active: z.boolean(),
    customer_profile: z
      .object({
        id: z.number(),
        phone_number: z.string().nullable().optional(),
        company_name: z.string().nullable().optional(),
        preferred_contact_method: z.string().nullable().optional(),
        loyalty_tier: z.string(),
      })
      .nullable()
      .optional(),
  })
  .transform(({ full_name, is_active, customer_profile, ...rest }) => ({
    ...rest,
    fullName: full_name,
    isActive: is_active,
    customerProfile: customer_profile
      ? {
          id: customer_profile.id,
          phoneNumber: customer_profile.phone_number ?? null,
          companyName: customer_profile.company_name ?? null,
          preferredContactMethod: customer_profile.preferred_contact_method ?? null,
          loyaltyTier: customer_profile.loyalty_tier,
        }
      : null,
  }))

export const tokenResponseSchema = z
  .object({
    access_token: z.string(),
    token_type: z.string(),
    expires_in: z.number().optional(),
  })
  .transform(({ access_token, token_type, expires_in }) => ({
    accessToken: access_token,
    tokenType: token_type,
    expiresIn: expires_in ?? 0,
  }))

export type CategoryDto = z.infer<typeof categorySchema>
export type EquipmentSummaryDto = z.infer<typeof equipmentSummarySchema>
export type EquipmentDetailDto = z.infer<typeof equipmentDetailSchema>
export type CatalogResponseDto = z.infer<typeof catalogResponseSchema>
export type LandingStatsDto = z.infer<typeof landingStatsSchema>
export type LocationDto = z.infer<typeof locationSchema>
export type ReservationSummaryDto = z.infer<typeof reservationSummarySchema>
export type DashboardSnapshotDto = z.infer<typeof dashboardSnapshotSchema>
export type UserDto = z.infer<typeof userSchema>
export type TokenResponseDto = z.infer<typeof tokenResponseSchema>
