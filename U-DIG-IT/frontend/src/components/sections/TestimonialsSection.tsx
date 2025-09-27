import type { Review } from '../../types'
import { Card } from '../ui/Card'
import { SectionHeading } from '../ui/SectionHeading'

interface TestimonialsSectionProps {
  testimonials: Review[]
}

export const TestimonialsSection = ({ testimonials }: TestimonialsSectionProps) => {
  if (!testimonials.length) return null

  return (
    <section className="section">
      <div className="container">
        <SectionHeading
          eyebrow="Customer Stories"
          title="Teams that build the future trust U-DIG-IT"
          description="Energy developers, data center builders, and municipal agencies rely on our logistics discipline and preventive maintenance to keep projects on pace."
        />
        <div className="grid three">
          {testimonials.map((testimonial) => (
            <Card key={testimonial.id}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '1rem' }}>
                <div
                  style={{
                    width: '48px',
                    height: '48px',
                    borderRadius: '50%',
                    background: 'rgba(37, 99, 235, 0.12)',
                    display: 'grid',
                    placeItems: 'center',
                    fontWeight: 700,
                  }}
                >
                  {testimonial.authorName.slice(0, 1)}
                </div>
                <div>
                  <strong>{testimonial.authorName}</strong>
                  <p style={{ margin: 0, color: 'var(--color-text-muted)' }}>{testimonial.authorCompany ?? 'Verified client'}</p>
                </div>
              </div>
              <p style={{ fontWeight: 600 }}>{testimonial.headline ?? 'Exceptional field performance'}</p>
              <p style={{ color: 'var(--color-text-muted)' }}>{testimonial.comment}</p>
            </Card>
          ))}
        </div>
      </div>
    </section>
  )
}
