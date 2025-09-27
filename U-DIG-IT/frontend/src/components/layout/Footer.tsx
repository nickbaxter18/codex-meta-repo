import { Link } from 'react-router-dom'

export const Footer = () => (
  <footer className="footer">
    <div className="container" style={{ display: 'grid', gap: '2rem', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))' }}>
      <div>
        <h3 style={{ margin: 0 }}>U-DIG-IT Rentals</h3>
        <p style={{ color: 'rgba(226, 232, 240, 0.7)', marginTop: '0.75rem' }}>
          Heavy equipment rentals engineered for modern infrastructure teams. Nationwide coverage, precision logistics, and
          dedicated equipment specialists.
        </p>
      </div>
      <div>
        <h4>Company</h4>
        <nav style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem', marginTop: '0.75rem' }}>
          <Link to="/about">About</Link>
          <Link to="/solutions">Solutions</Link>
          <Link to="/catalog">Catalog</Link>
        </nav>
      </div>
      <div>
        <h4>Contact</h4>
        <p style={{ margin: '0.5rem 0' }}>1-800-UDIG-247</p>
        <a href="mailto:logistics@u-dig-it.com">logistics@u-dig-it.com</a>
        <p style={{ marginTop: '0.5rem', color: 'rgba(226, 232, 240, 0.7)' }}>
          1450 Market Street, Denver, CO 80202
        </p>
      </div>
    </div>
  </footer>
)
