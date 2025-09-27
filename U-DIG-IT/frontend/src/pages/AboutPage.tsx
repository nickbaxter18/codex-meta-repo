import { Card } from '../components/ui/Card'

export const AboutPage = () => (
  <div className="section" style={{ paddingTop: '3rem' }}>
    <div className="container" style={{ display: 'grid', gap: '2rem' }}>
      <Card>
        <h1 style={{ marginTop: 0 }}>Built by field operators, trusted by builders</h1>
        <p style={{ color: 'var(--color-text-muted)', fontSize: '1.05rem' }}>
          U-DIG-IT started as a single logistics yard in Denver supporting emergency infrastructure repairs. Today, we orchestrate
          complex deployments for energy, data center, and municipal partners across the Mountain West. Every asset is maintained
          by manufacturer-certified technicians with telemetry, maintenance logs, and digital operator onboarding.
        </p>
        <p style={{ color: 'var(--color-text-muted)' }}>
          Our control tower blends human expertise with real-time data from OpenAI agents, enabling rapid response to project shifts,
          proactive maintenance, and accurate forecasting. The result: predictable uptime, safer job sites, and lower total project cost.
        </p>
      </Card>
    </div>
  </div>
)
