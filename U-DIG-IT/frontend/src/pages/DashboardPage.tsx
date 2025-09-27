import { useDashboardSnapshot } from '../hooks/useDashboard'
import { Card } from '../components/ui/Card'
import { formatCurrency, formatDateShort } from '../utils/formatters'

export const DashboardPage = () => {
  const { data, isLoading } = useDashboardSnapshot()

  if (isLoading || !data) {
    return (
      <div className="container" style={{ padding: '4rem 0' }}>
        <Card>Loading control tower metrics…</Card>
      </div>
    )
  }

  const totalRevenue = data.analytics.reduce((acc, item) => acc + item.totalRevenue, 0)
  const totalReservations = data.analytics.reduce((acc, item) => acc + item.totalReservations, 0)

  return (
    <div className="section" style={{ paddingTop: '2rem' }}>
      <div className="container" style={{ display: 'grid', gap: '2rem' }}>
        <header>
          <h1 style={{ margin: 0 }}>Operations dashboard</h1>
          <p style={{ color: 'var(--color-text-muted)', maxWidth: '640px' }}>
            Monitor reservation velocity, revenue contribution, and equipment performance across logistics hubs.
          </p>
        </header>

        <div className="grid three">
          <Card>
            <h3 style={{ marginTop: 0 }}>Revenue YTD</h3>
            <p style={{ fontSize: '2rem', fontWeight: 700 }}>{formatCurrency(totalRevenue)}</p>
            <p style={{ color: 'var(--color-text-muted)' }}>{data.analytics.length} months of reporting</p>
          </Card>
          <Card>
            <h3 style={{ marginTop: 0 }}>Reservations fulfilled</h3>
            <p style={{ fontSize: '2rem', fontWeight: 700 }}>{totalReservations}</p>
            <p style={{ color: 'var(--color-text-muted)' }}>Completed reservations across all hubs</p>
          </Card>
          <Card>
            <h3 style={{ marginTop: 0 }}>Top performing asset</h3>
            <p style={{ fontSize: '1.25rem', fontWeight: 700 }}>
              {data.topEquipment[0]?.equipment.name ?? 'Awaiting deployments'}
            </p>
            <p style={{ color: 'var(--color-text-muted)' }}>
              {data.topEquipment[0]
                ? formatCurrency(data.topEquipment[0].revenue) + ' revenue across ' + data.topEquipment[0].reservationCount + ' rentals'
                : 'Your first deployment will appear here.'}
            </p>
          </Card>
        </div>

        <Card>
          <h2 style={{ marginTop: 0 }}>Active reservations</h2>
          <div style={{ overflowX: 'auto', marginTop: '1rem' }}>
            <table className="table">
              <thead>
                <tr>
                  <th>Reservation</th>
                  <th>Equipment</th>
                  <th>Status</th>
                  <th>Total</th>
                  <th>Schedule</th>
                </tr>
              </thead>
              <tbody>
                {data.reservations.map((reservation) => (
                  <tr key={reservation.reservationCode}>
                    <td>{reservation.reservationCode}</td>
                    <td>{reservation.equipment.name}</td>
                    <td>{reservation.status}</td>
                    <td>{formatCurrency(reservation.totalAmount)}</td>
                    <td>
                      {formatDateShort(reservation.startDate)} → {formatDateShort(reservation.endDate)}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </Card>

        <Card>
          <h2 style={{ marginTop: 0 }}>Equipment performance</h2>
          <div className="grid two" style={{ marginTop: '1.5rem' }}>
            {data.topEquipment.map((entry) => (
              <Card key={entry.equipment.id}>
                <h3 style={{ marginTop: 0 }}>{entry.equipment.name}</h3>
                <p style={{ color: 'var(--color-text-muted)' }}>{entry.equipment.summary}</p>
                <p style={{ fontWeight: 600 }}>{formatCurrency(entry.revenue)} revenue</p>
                <p style={{ color: 'var(--color-text-muted)' }}>{entry.reservationCount} fulfilled reservations</p>
              </Card>
            ))}
          </div>
        </Card>
      </div>
    </div>
  )
}
