import { Card } from '../components/ui/Card'
import { Button } from '../components/ui/Button'

export const ContactPage = () => (
  <div className="section" style={{ paddingTop: '3rem' }}>
    <div className="container" style={{ maxWidth: '540px' }}>
      <Card>
        <h1 style={{ marginTop: 0 }}>Connect with logistics engineering</h1>
        <p style={{ color: 'var(--color-text-muted)' }}>
          Ready to scope your next project? Our specialist team will align equipment, operators, and delivery windows within 30
          minutes.
        </p>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem', marginTop: '1.5rem' }}>
          <Button onClick={() => (window.location.href = 'tel:18008344247')}>Call 1-800-UDIG-247</Button>
          <Button variant="outline" onClick={() => (window.location.href = 'mailto:logistics@u-dig-it.com')}>
            Email logistics@u-dig-it.com
          </Button>
        </div>
      </Card>
    </div>
  </div>
)
