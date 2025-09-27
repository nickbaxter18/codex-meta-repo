import { SectionHeading } from '../ui/SectionHeading'
import { Card } from '../ui/Card'

const steps = [
  {
    title: 'Scope & match',
    description:
      'Upload project constraints and we surface certified equipment packages, logistics windows, and any required site prep.',
    icon: '🧭',
  },
  {
    title: 'Mobilize quickly',
    description:
      'Same-day dispatch from regional yards with live GPS tracking, digital handoffs, and field-ready checklists.',
    icon: '🚛',
  },
  {
    title: 'Operate with confidence',
    description:
      'Operator onboarding, predictive maintenance, and utilization dashboards keep every asset accountable on site.',
    icon: '📊',
  },
]

export const WorkflowSection = () => (
  <section className="section" style={{ background: 'var(--color-muted)' }}>
    <div className="container">
      <SectionHeading
        eyebrow="Delivery Playbook"
        title="From quote to commissioning in under 24 hours"
        description="Our logistics control center orchestrates delivery, training, telemetry, and maintenance so field teams never lose momentum."
      />
      <div className="grid three">
        {steps.map((step) => (
          <Card key={step.title}>
            <div style={{ fontSize: '2rem', marginBottom: '1rem' }}>{step.icon}</div>
            <h3 style={{ marginTop: 0 }}>{step.title}</h3>
            <p style={{ color: 'var(--color-text-muted)' }}>{step.description}</p>
          </Card>
        ))}
      </div>
    </div>
  </section>
)
