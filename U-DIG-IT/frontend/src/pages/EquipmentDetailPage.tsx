import { useEffect, useMemo, useState } from 'react'
import { useForm } from 'react-hook-form'
import { useNavigate, useParams } from 'react-router-dom'

import { Card } from '../components/ui/Card'
import { Tag } from '../components/ui/Tag'
import { Button } from '../components/ui/Button'
import { InputField } from '../components/ui/InputField'
import { useEquipmentDetail } from '../hooks/useEquipmentDetail'
import { useLocations } from '../hooks/useLocations'
import { useAuth } from '../hooks/useAuth'
import { formatCurrency, formatDateShort } from '../utils/formatters'
import { submitReservation, checkEquipmentAvailability } from '../api/endpoints'
import type { ReservationPayload } from '../types'

interface ReservationFormFields {
  startDate: string
  endDate: string
  locationId: string
  notes?: string
  customerPhone?: string
}

export const EquipmentDetailPage = () => {
  const params = useParams<{ slug: string }>()
  const slug = params.slug ?? ''
  const navigate = useNavigate()
  const { data: equipment, isLoading } = useEquipmentDetail(slug)
  const { data: locations } = useLocations()
  const { user, isAuthenticated } = useAuth()

  const [availabilityMessage, setAvailabilityMessage] = useState<string | null>(null)
  const [reservationSuccess, setReservationSuccess] = useState<string | null>(null)
  const [availabilityLoading, setAvailabilityLoading] = useState(false)

  const {
    register,
    handleSubmit,
    watch,
    setValue,
    formState: { isSubmitting },
  } = useForm<ReservationFormFields>({
    defaultValues: {
      startDate: '',
      endDate: '',
      locationId: locations?.[0]?.id ? String(locations[0].id) : '',
    },
  })

  useEffect(() => {
    if (locations && locations.length) {
      setValue('locationId', String(locations[0].id), { shouldDirty: false })
    }
  }, [locations, setValue])

  const locationIdValue = watch('locationId')
  const startDateValue = watch('startDate')
  const endDateValue = watch('endDate')

  const selectedLocation = useMemo(() => {
    if (!locations || !locationIdValue) return undefined
    return locations.find((location) => String(location.id) === String(locationIdValue))
  }, [locations, locationIdValue])

  const handleAvailabilityCheck = async () => {
    if (!slug) return
    if (!startDateValue || !endDateValue) {
      setAvailabilityMessage('Select start and end dates to check availability.')
      return
    }

    try {
      setAvailabilityLoading(true)
      const status = await checkEquipmentAvailability(slug, {
        startDate: startDateValue,
        endDate: endDateValue,
      })
      if (status.isAvailable) {
        setAvailabilityMessage('Available: ' + status.availableQuantity + ' unit(s) ready for deployment in this window.')
      } else {
        setAvailabilityMessage('All units are reserved for these dates. Try adjusting your schedule or contact logistics for overrides.')
      }
    } catch (error) {
      console.error('Availability check failed', error)
      setAvailabilityMessage('Availability service is temporarily unavailable. Please retry or contact our logistics desk.')
    } finally {
      setAvailabilityLoading(false)
    }
  }

  const onSubmit = handleSubmit(async (values) => {
    if (!equipment || !isAuthenticated || !user) {
      navigate('/login', { state: { from: '/equipment/' + slug } })
      return
    }

    const payload: ReservationPayload = {
      equipmentSlug: slug,
      locationId: Number(values.locationId),
      startDate: values.startDate,
      endDate: values.endDate,
      notes: values.notes,
      customerPhone: values.customerPhone,
      customerName: user.fullName,
      customerEmail: user.email,
      customerId: user.id,
    }

    try {
      const response = await submitReservation(payload)
      setReservationSuccess(response.message)
      setAvailabilityMessage(null)
    } catch (error) {
      console.error('Reservation request failed', error)
      setReservationSuccess('Unable to confirm reservation right now. Please retry or contact our logistics desk directly.')
    }
  })

  if (isLoading || !equipment) {
    return (
      <div className="container" style={{ padding: '4rem 0' }}>
        <Card>Loading equipment profile…</Card>
      </div>
    )
  }

  return (
    <div className="section" style={{ paddingTop: '2rem' }}>
      <div className="container" style={{ display: 'grid', gap: '2.5rem' }}>
        <div style={{ display: 'grid', gap: '2rem', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))' }}>
          <Card style={{ padding: 0 }}>
            {equipment.gallery.length ? (
              <img
                src={equipment.gallery[0].url}
                alt={equipment.gallery[0].altText ?? equipment.name}
                style={{ width: '100%', height: '100%', objectFit: 'cover', borderRadius: '1.5rem 1.5rem 0 0' }}
              />
            ) : (
              <div style={{ padding: '4rem', textAlign: 'center' }}>High-resolution media available upon request.</div>
            )}
          </Card>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
            <Tag>{equipment.category.name}</Tag>
            <div>
              <h1 style={{ margin: '0 0 0.75rem' }}>{equipment.name}</h1>
              <p style={{ color: 'var(--color-text-muted)' }}>{equipment.description ?? equipment.summary}</p>
            </div>
            <div style={{ display: 'flex', gap: '2rem', flexWrap: 'wrap', alignItems: 'center' }}>
              <strong style={{ fontSize: '1.75rem' }}>{formatCurrency(equipment.dailyRate)} / day</strong>
              <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
                {equipment.tags.map((tag) => (
                  <Tag key={tag}>{tag}</Tag>
                ))}
              </div>
            </div>
            {equipment.specifications && (
              <Card>
                <h3 style={{ marginTop: 0 }}>Key specifications</h3>
                <ul style={{ margin: 0, paddingLeft: '1rem', color: 'var(--color-text-muted)' }}>
                  {Object.entries(equipment.specifications).map(([key, value]) => (
                    <li key={key} style={{ marginBottom: '0.35rem' }}>
                      <strong>{key}:</strong> {value ?? 'N/A'}
                    </li>
                  ))}
                </ul>
              </Card>
            )}
          </div>
        </div>

        <Card>
          <h2 style={{ marginTop: 0 }}>Reserve this equipment</h2>
          <p style={{ color: 'var(--color-text-muted)', maxWidth: '560px' }}>
            Choose deployment window and logistics hub. Reservations require an active account so we can provide delivery
            timeline, documentation, and operator onboarding resources.
          </p>

          {!isAuthenticated && (
            <div className="alert" style={{ marginBottom: '1.5rem' }}>
              Please log in before reserving equipment. You will be redirected after authentication.
            </div>
          )}

          <form onSubmit={onSubmit} style={{ display: 'grid', gap: '1rem', marginTop: '1.5rem' }}>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem' }}>
              <InputField type="date" label="Start date" required {...register('startDate', { required: true })} />
              <InputField type="date" label="End date" required {...register('endDate', { required: true })} />
            </div>
            <label style={{ display: 'block' }}>
              <span style={{ display: 'block', marginBottom: '0.35rem', fontWeight: 600 }}>Deployment hub</span>
              <select {...register('locationId', { required: true })}>
                {(locations ?? []).map((location) => (
                  <option key={location.id} value={location.id}>
                    {location.name} — {location.city}, {location.state}
                  </option>
                ))}
              </select>
            </label>
            <InputField
              type="tel"
              label="Best contact number"
              placeholder="e.g., +1 303 555 0123"
              {...register('customerPhone')}
            />
            <label style={{ display: 'block' }}>
              <span style={{ display: 'block', marginBottom: '0.35rem', fontWeight: 600 }}>Notes for our logistics team</span>
              <textarea rows={3} placeholder="Delivery constraints, access notes, or operator requirements" {...register('notes')} />
            </label>

            {selectedLocation && (
              <div style={{ fontSize: '0.9rem', color: 'var(--color-text-muted)' }}>
                <strong>Logistics hub:</strong> {selectedLocation.name} — {selectedLocation.addressLine1}, {selectedLocation.city}, {selectedLocation.state}
              </div>
            )}

            {availabilityMessage && <Card style={{ background: 'rgba(37,99,235,0.08)' }}>{availabilityMessage}</Card>}
            {reservationSuccess && <Card style={{ background: 'rgba(22,163,74,0.12)', borderColor: 'rgba(22,163,74,0.2)' }}>{reservationSuccess}</Card>}

            <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
              <Button type="submit" disabled={isSubmitting || !isAuthenticated}>
                {isSubmitting ? 'Confirming…' : 'Confirm reservation'}
              </Button>
              <Button type="button" variant="outline" onClick={handleAvailabilityCheck} disabled={availabilityLoading}>
                {availabilityLoading ? 'Checking…' : 'Check availability'}
              </Button>
            </div>
          </form>
        </Card>

        {equipment.reviews.length > 0 && (
          <Card>
            <h2 style={{ marginTop: 0 }}>Operator feedback</h2>
            <div className="grid two" style={{ marginTop: '1.5rem' }}>
              {equipment.reviews.map((review) => (
                <div key={review.id}>
                  <strong>{review.authorName}</strong>
                  <p style={{ margin: '0.25rem 0', color: 'var(--color-text-muted)' }}>{review.authorCompany ?? 'Verified partner'}</p>
                  <p style={{ fontWeight: 600 }}>{review.headline ?? 'High-performing asset'}</p>
                  <p style={{ color: 'var(--color-text-muted)' }}>{review.comment}</p>
                  <p style={{ fontSize: '0.8rem', color: 'var(--color-text-muted)' }}>
                    Delivered {review.createdAt ? formatDateShort(review.createdAt) : 'recently'}
                  </p>
                </div>
              ))}
            </div>
          </Card>
        )}
      </div>
    </div>
  )
}
