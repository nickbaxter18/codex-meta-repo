import { Link } from 'react-router-dom'

import { Button } from '../ui/Button'

export const CTASection = () => (
  <section className="section" style={{ paddingBottom: '5rem' }}>
    <div
      className="container"
      style={{
        background: 'linear-gradient(135deg, rgba(37, 99, 235, 0.92), rgba(14, 165, 233, 0.9))',
        borderRadius: '1.5rem',
        padding: '3.5rem',
        color: '#fff',
        textAlign: 'center',
        boxShadow: 'var(--shadow-md)',
      }}
    >
      <h2 style={{ fontSize: '2.5rem', margin: 0 }}>Mobilize your next project with confidence</h2>
      <p style={{ margin: '1rem auto 2rem', maxWidth: '620px', fontSize: '1.1rem', color: 'rgba(255,255,255,0.9)' }}>
        Talk with a logistics engineer to define scope, reserve assets, and lock in delivery windows within minutes.
      </p>
      <div style={{ display: 'flex', gap: '1rem', justifyContent: 'center', flexWrap: 'wrap' }}>
        <Link to="/catalog">
          <Button>Build your fleet</Button>
        </Link>
        <Link to="/contact">
          <Button variant="outline" style={{ color: '#fff', borderColor: 'rgba(255,255,255,0.4)' }}>
            Request consultation
          </Button>
        </Link>
      </div>
    </div>
  </section>
)
