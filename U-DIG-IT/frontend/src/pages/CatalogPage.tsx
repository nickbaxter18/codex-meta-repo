import { useMemo, useState } from 'react'
import { useSearchParams, Link } from 'react-router-dom'

import { InputField } from '../components/ui/InputField'
import { Tag } from '../components/ui/Tag'
import { Card } from '../components/ui/Card'
import { Button } from '../components/ui/Button'
import { useCatalog } from '../hooks/useCatalog'
import { formatCurrency } from '../utils/formatters'

export const CatalogPage = () => {
  const [searchParams, setSearchParams] = useSearchParams()
  const [searchTerm, setSearchTerm] = useState(searchParams.get('search') ?? '')
  const categoryFilter = searchParams.get('category') ?? undefined
  const tagFilter = searchParams.get('tag') ?? undefined

  const { data, isLoading } = useCatalog({
    category: categoryFilter,
    search: searchParams.get('search'),
    tag: tagFilter,
  })

  const categories = data?.categories ?? []
  const equipment = data?.equipment ?? []
  const availableTags = data?.availableTags ?? []

  const filteredEquipment = useMemo(() => {
    if (!tagFilter) {
      return equipment
    }
    const normalizedTag = tagFilter.toLowerCase()
    return equipment.filter((item) => item.tags.some((tag) => tag.toLowerCase() === normalizedTag))
  }, [equipment, tagFilter])

  const handleCategorySelect = (slug?: string) => {
    const next = new URLSearchParams(searchParams)
    if (!slug) {
      next.delete('category')
    } else {
      next.set('category', slug)
    }
    setSearchParams(next)
  }

  const handleTagSelect = (tag?: string) => {
    const next = new URLSearchParams(searchParams)
    if (!tag) {
      next.delete('tag')
    } else {
      next.set('tag', tag)
    }
    setSearchParams(next)
  }

  const handleSearchSubmit = (event: React.FormEvent) => {
    event.preventDefault()
    const next = new URLSearchParams(searchParams)
    if (searchTerm) {
      next.set('search', searchTerm)
    } else {
      next.delete('search')
    }
    setSearchParams(next)
  }

  return (
    <div className="section" style={{ paddingTop: '2rem' }}>
      <div className="container" style={{ display: 'grid', gap: '2rem' }}>
        <header style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <h1 style={{ margin: 0 }}>Equipment catalog</h1>
          <p style={{ color: 'var(--color-text-muted)', maxWidth: '680px' }}>
            Reserve from a proven fleet of excavators, boom lifts, generators, and site services with ready-to-go delivery
            timelines and maintenance documentation.
          </p>
          <form onSubmit={handleSearchSubmit} style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
            <InputField
              name="search"
              value={searchTerm}
              onChange={(event) => setSearchTerm(event.target.value)}
              placeholder="Search equipment, capabilities, or specs"
              style={{ minWidth: '260px', flex: 1 }}
            />
            <Button type="submit">Search</Button>
          </form>
        </header>

        <div style={{ display: 'flex', gap: '0.75rem', flexWrap: 'wrap' }}>
          <Tag
            onClick={() => handleCategorySelect(undefined)}
            style={{ cursor: 'pointer', background: !categoryFilter ? 'rgba(37,99,235,0.15)' : undefined }}
          >
            All categories
          </Tag>
          {categories.map((category) => (
            <Tag
              key={category.id}
              onClick={() => handleCategorySelect(category.slug)}
              style={{
                cursor: 'pointer',
                background: categoryFilter === category.slug ? 'rgba(37,99,235,0.15)' : undefined,
                color: categoryFilter === category.slug ? 'var(--color-primary)' : undefined,
              }}
            >
              {category.name}
            </Tag>
          ))}
        </div>

        {!!availableTags.length && (
          <div style={{ display: 'flex', gap: '0.75rem', flexWrap: 'wrap' }}>
            <Tag
              onClick={() => handleTagSelect(undefined)}
              style={{
                cursor: 'pointer',
                background: !tagFilter ? 'rgba(37,99,235,0.15)' : undefined,
                color: !tagFilter ? 'var(--color-primary)' : undefined,
              }}
            >
              All tags
            </Tag>
            {availableTags.map((tag) => (
              <Tag
                key={tag}
                onClick={() => handleTagSelect(tag)}
                style={{
                  cursor: 'pointer',
                  background: tagFilter?.toLowerCase() === tag.toLowerCase() ? 'rgba(37,99,235,0.15)' : undefined,
                  color: tagFilter?.toLowerCase() === tag.toLowerCase() ? 'var(--color-primary)' : undefined,
                }}
                title={`Filter by ${tag}`}
              >
                #{tag}
              </Tag>
            ))}
          </div>
        )}

        {isLoading ? (
          <Card>Loading equipment packages…</Card>
        ) : (
          <div className="grid two">
            {filteredEquipment.map((item) => (
              <Card key={item.id} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                {item.primaryImage && (
                  <img
                    src={item.primaryImage}
                    alt={item.name}
                    style={{ borderRadius: '1rem', height: '200px', objectFit: 'cover' }}
                  />
                )}
                <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
                  {item.tags.map((tag) => (
                    <Tag
                      key={tag}
                      onClick={() => handleTagSelect(tag)}
                      style={{
                        cursor: 'pointer',
                        background: tagFilter?.toLowerCase() === tag.toLowerCase() ? 'rgba(37,99,235,0.15)' : undefined,
                        color: tagFilter?.toLowerCase() === tag.toLowerCase() ? 'var(--color-primary)' : undefined,
                      }}
                      title={`Show equipment tagged ${tag}`}
                    >
                      {tag}
                    </Tag>
                  ))}
                </div>
                <div>
                  <h2 style={{ margin: '0 0 0.5rem' }}>{item.name}</h2>
                  <p style={{ color: 'var(--color-text-muted)' }}>{item.summary}</p>
                </div>
                <div style={{ marginTop: 'auto', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <strong>{formatCurrency(item.dailyRate)} / day</strong>
                  <Link to={'/equipment/' + item.slug} style={{ fontWeight: 600, color: 'var(--color-primary)' }}>
                    View details
                  </Link>
                </div>
              </Card>
            ))}
            {!filteredEquipment.length && <Card>No equipment found. Try adjusting filters.</Card>}
          </div>
        )}
      </div>
    </div>
  )
}
