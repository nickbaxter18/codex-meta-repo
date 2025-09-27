interface SectionHeadingProps {
  eyebrow?: string
  title: string
  description?: string
  align?: 'left' | 'center'
}

export const SectionHeading = ({ eyebrow, title, description, align = 'left' }: SectionHeadingProps) => (
  <div className="section-heading" style={{ textAlign: align }}>
    {eyebrow && <span>{eyebrow}</span>}
    <h2>{title}</h2>
    {description && <p>{description}</p>}
  </div>
)
