import { Link } from 'react-router-dom'

import type { LandingStats } from '../../types'
import { Button } from '../ui/Button'
import { formatCurrency, formatPercent } from '../../utils/formatters'

interface HeroSectionProps {
  stats?: LandingStats
}

export const HeroSection = ({ stats }: HeroSectionProps) => (
  <section className="hero">
    <div className="container hero-content">
      <div>
        <div className="badge" style={{ marginBottom: '1.5rem' }}>
          Precision logistics • Same-day deployment
        </div>
        <h1>Scale your infrastructure projects with mission-ready equipment</h1>
        <p>
          U-DIG-IT delivers heavy equipment rentals engineered for predictable uptime. From micro trenchers to telescopic boom
          lifts, our logistics team handles sourcing, transport, and on-site commissioning so you can stay ahead of schedule.
        </p>
        <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
          <Link to="/catalog">
            <Button>Browse catalog</Button>
          </Link>
          <Link to="/solutions">
            <Button variant="outline">Engineering services</Button>
          </Link>
        </div>
        {stats && (
          <div className="stats-bar">
            <div className="stat-card">
              <h3>{stats.totalInventory.toLocaleString()}+</h3>
              <span>Specialty assets ready to deploy</span>
            </div>
            <div className="stat-card">
              <h3>{stats.locationsServed}</h3>
              <span>Metro hubs served</span>
            </div>
            <div className="stat-card">
              <h3>{formatPercent(stats.onTimeDeliveryRate)}</h3>
              <span>On-time delivery performance</span>
            </div>
            <div className="stat-card">
              <h3>{formatCurrency(4200000)}</h3>
              <span>Client CapEx preserved YTD</span>
            </div>
          </div>
        )}
      </div>
      <div>
        <img
          src="https://images.unsplash.com/photo-1489515217757-5fd1be406fef"
          alt="Fleet of excavators ready for deployment"
          style={{ borderRadius: '1.5rem', boxShadow: 'var(--shadow-md)' }}
        />
      </div>
    </div>
  </section>
)
