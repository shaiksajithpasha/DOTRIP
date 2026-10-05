import { useEffect, useState } from "react";
import "./Dashboard.css";

interface DashboardStats {
  total_users: number;
  total_drivers: number;
  available_drivers: number;
  total_vehicles: number;
  total_vendors: number;
  total_bookings: number;
  pending_bookings: number;
  total_trips: number;
  ongoing_trips: number;
  completed_trips: number;
  total_invoices: number;
  total_feedback: number;
}

function Dashboard() {
  const [stats, setStats] = useState<DashboardStats | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    let cancelled = false;

    const loadDashboardStats = async () => {
      try {
        const token = localStorage.getItem("token");

        const response = await fetch(
          `${import.meta.env.VITE_API_URL}/dashboard/stats`,
          {
            method: "GET",
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );

        if (!response.ok) {
          throw new Error("Failed to load dashboard statistics");
        }

        const data: DashboardStats = await response.json();

        if (!cancelled) {
          setStats(data);
          setError("");
          setLoading(false);
        }
      } catch (err) {
        console.error(err);

        if (!cancelled) {
          setError("Unable to load dashboard statistics");
          setLoading(false);
        }
      }
    };

    loadDashboardStats();

    return () => {
      cancelled = true;
    };
  }, []);

  if (loading) {
    return (
      <div className="dashboard">
        <h1>Dashboard</h1>
        <p>Loading dashboard...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="dashboard">
        <h1>Dashboard</h1>
        <p className="dashboard-error">{error}</p>
      </div>
    );
  }

  return (
    <div className="dashboard">
      <div className="dashboard-header">
        <div>
          <h1>Dashboard</h1>
          <p>Welcome to DOTRIP Admin Dashboard</p>
        </div>
      </div>

      <div className="stats-grid">
        <div className="stat-card">
          <h3>Users</h3>
          <div className="stat-number">
            {stats?.total_users ?? 0}
          </div>
        </div>

        <div className="stat-card">
          <h3>Drivers</h3>
          <div className="stat-number">
            {stats?.total_drivers ?? 0}
          </div>
          <p>
            {stats?.available_drivers ?? 0} available
          </p>
        </div>

        <div className="stat-card">
          <h3>Vehicles</h3>
          <div className="stat-number">
            {stats?.total_vehicles ?? 0}
          </div>
        </div>

        <div className="stat-card">
          <h3>Vendors</h3>
          <div className="stat-number">
            {stats?.total_vendors ?? 0}
          </div>
        </div>

        <div className="stat-card">
          <h3>Bookings</h3>
          <div className="stat-number">
            {stats?.total_bookings ?? 0}
          </div>
          <p>
            {stats?.pending_bookings ?? 0} pending
          </p>
        </div>

        <div className="stat-card">
          <h3>Trips</h3>
          <div className="stat-number">
            {stats?.total_trips ?? 0}
          </div>
          <p>
            {stats?.ongoing_trips ?? 0} ongoing
          </p>
        </div>

        <div className="stat-card">
          <h3>Completed Trips</h3>
          <div className="stat-number">
            {stats?.completed_trips ?? 0}
          </div>
        </div>

        <div className="stat-card">
          <h3>Invoices</h3>
          <div className="stat-number">
            {stats?.total_invoices ?? 0}
          </div>
        </div>

        <div className="stat-card">
          <h3>Feedback</h3>
          <div className="stat-number">
            {stats?.total_feedback ?? 0}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;