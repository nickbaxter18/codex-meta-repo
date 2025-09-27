import { HeroSection } from '../components/sections/HeroSection'
import { CategoryShowcase } from '../components/sections/CategoryShowcase'
import { WorkflowSection } from '../components/sections/WorkflowSection'
import { TestimonialsSection } from '../components/sections/TestimonialsSection'
import { CTASection } from '../components/sections/CTASection'
import { useCatalog } from '../hooks/useCatalog'
import { useLandingStats } from '../hooks/useLandingStats'
import { Card } from '../components/ui/Card'

export const HomePage = () => {
  const { data: catalogData, isLoading: catalogLoading } = useCatalog()
  const { data: landingStats, isLoading: statsLoading } = useLandingStats()

  const categories = catalogData?.categories ?? []
  const featured = catalogData?.featured ?? []
  const testimonials = landingStats?.featuredTestimonials ?? []

  return (
    <div>
      <HeroSection stats={landingStats} />
      {catalogLoading && (
        <div className="container" style={{ marginTop: '-2rem' }}>
          <Card>Loading fleet intelligence…</Card>
        </div>
      )}
      {!catalogLoading && <CategoryShowcase categories={categories} featured={featured} />}
      <WorkflowSection />
      {!statsLoading && <TestimonialsSection testimonials={testimonials} />}
      <CTASection />
    </div>
  )
}
