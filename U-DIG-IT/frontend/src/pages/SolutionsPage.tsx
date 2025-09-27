import { Card } from '../components/ui/Card'
import { SectionHeading } from '../components/ui/SectionHeading'

const solutions = [
  {
    title: 'Renewable energy deployments',
    description:
      'Self-contained equipment packages engineered for solar, wind, and storage. Includes trenching, lifting, and commissioning support.',
  },
  {
    title: 'Data center expansions',
    description:
      'Precision lifting, HVAC, and backup power assets coordinated with strict tier certification and maintenance requirements.',
  },
  {
    title: 'Municipal infrastructure',
    description:
      'Bridge repairs, utility upgrades, and smart city rollouts backed by geofenced asset tracking and night-shift logistics.',
  },
]

export const SolutionsPage = () => (
  <div className="section" style={{ paddingTop: '3rem' }}>
    <div className="container" style={{ display: 'grid', gap: '2rem' }}>
      <SectionHeading
        eyebrow="Project Blueprints"
        title="Rental strategies aligned to your industry"
        description="Our solutions team packages equipment, logistics, and operator enablement for complex capital projects."
      />
      <div className="grid three">
        {solutions.map((solution) => (
          <Card key={solution.title}>
            <h2 style={{ marginTop: 0 }}>{solution.title}</h2>
            <p style={{ color: 'var(--color-text-muted)' }}>{solution.description}</p>
          </Card>
        ))}
      </div>
    </div>
  </div>
)
