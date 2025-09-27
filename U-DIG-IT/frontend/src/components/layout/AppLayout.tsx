import { Outlet } from 'react-router-dom'

import { Footer } from './Footer'
import { Navigation } from './Navigation'

export const AppLayout = () => (
  <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
    <Navigation />
    <main style={{ flex: 1 }}>
      <Outlet />
    </main>
    <Footer />
  </div>
)
