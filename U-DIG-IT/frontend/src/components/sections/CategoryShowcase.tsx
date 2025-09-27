import { Link } from 'react-router-dom'

import type { Category, EquipmentSummary } from '../../types'
import { Card } from '../ui/Card'
import { Tag } from '../ui/Tag'
import { SectionHeading } from '../ui/SectionHeading'
import { truncate, formatCurrency } from '../../utils/formatters'

interface CategoryShowcaseProps {
  categories: Category[]
  featured: EquipmentSummary[]
}

const iconMap: Record<string, string> = {
  'earth-moving': '⛏️',
  'power-lighting': '⚡',
  'site-services': '🏗️',
}

export const CategoryShowcase = ({ categories, featured }: CategoryShowcaseProps) => (
  <section className="section" style={{ background: '#fff' }}>
    <div className="container">
      <SectionHeading
        eyebrow="Rental Intelligence"
        title="Instant access to the gear your crews rely on"
        description="Category specialists maintain curated fleets with manufacturer-certified maintenance logs, telemetry, and training protocols."
      />
      <div className="grid three" style={{ marginBottom: '2.5rem' }}>
        {categories.map((category) => (
          <Card key={category.id}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '1rem' }}>
              <span style={{ fontSize: '1.75rem' }}>{iconMap[category.slug] ?? '🛠️'}</span>
              <Tag>{category.equipmentCount} assets</Tag>
            </div>
            <h3 style={{ marginTop: 0 }}>{category.name}</h3>
            <p style={{ color: 'var(--color-text-muted)' }}>{category.description ?? 'Highly maintained equipment ready for deployment.'}</p>
            <Link to={'/catalog?category=' + category.slug} style={{ fontWeight: 600, color: 'var(--color-primary)' }}>
              View inventory →
            </Link>
          </Card>
        ))}
      </div>

      <SectionHeading
        eyebrow="Featured Fleet"
        title="Ready-to-roll equipment packages"
        description="Smarter bundles engineered for data centers, renewable energy projects, municipal upgrades, and industrial expansions."
      />
      <div className="grid two">
        {featured.map((item) => (
          <Card key={item.id}>
            {item.primaryImage && (
              <img
                src={item.primaryImage}
                alt={item.name}
                style={{ borderRadius: '1rem', height: '220px', objectFit: 'cover', marginBottom: '1rem' }}
              />
            )}
            <Tag style={{ marginBottom: '0.75rem' }}>{item.category.name}</Tag>
            <h3 style={{ marginTop: 0 }}>{item.name}</h3>
            <p style={{ color: 'var(--color-text-muted)' }}>{truncate(item.summary, 140)}</p>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '1rem' }}>
              <strong>{formatCurrency(item.dailyRate)} / day</strong>
              <Link to={'/equipment/' + item.slug} style={{ fontWeight: 600, color: 'var(--color-primary)' }}>
                Details
              </Link>
            </div>
          </Card>
        ))}
      </div>
    </div>
  </section>
)
