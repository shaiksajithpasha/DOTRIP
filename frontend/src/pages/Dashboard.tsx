
import { useNavigate } from "react-router-dom";
import "./Dashboard.css";

interface StoredUser {
  id: number;
  name: string;
  email: string;
  phone: string | null;
  role: string;
}

function Dashboard() {
  const navigate = useNavigate();

  const token = localStorage.getItem("token");
  const storedUser = localStorage.getItem("user");

  const user: StoredUser | null = storedUser
    ? JSON.parse(storedUser)
    : null;

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");

    navigate("/login", { replace: true });
  };

  if (!token) {
    navigate("/login", { replace: true });
    return null;
  }

  return (
    <div className="dashboard-page">
      {/* Sidebar */}
      <aside className="dashboard-sidebar">
        <div className="sidebar-logo">
          <img
            src="/gemini-svg.svg"
            alt="DOTRIP"
            className="dashboard-logo"
          />
        </div>

        <nav className="sidebar-nav">
          <button className="nav-item active">
            <span>⌂</span>
            Dashboard
          </button>

          <button className="nav-item">
            <span>✈</span>
            Trips
          </button>

          <button className="nav-item">
            <span>▣</span>
            Bookings
          </button>

          <button className="nav-item">
            <span>♙</span>
            Users
          </button>

          <button className="nav-item">
            <span>⚙</span>
            Settings
          </button>
        </nav>

        <button
          className="logout-button"
          onClick={handleLogout}
        >
          <span>↪</span>
          Logout
        </button>
      </aside>

      {/* Main content */}
      <main className="dashboard-main">
        <header className="dashboard-header">
          <div>
            <span className="dashboard-eyebrow">
              DOTRIP DASHBOARD
            </span>

            <h1>Welcome back{user?.name ? `, ${user.name}` : ""}</h1>

            <p>
              Manage your DOTRIP operations from one place.
            </p>
          </div>

          <div className="user-profile">
            <div className="user-avatar">
              {user?.name
                ? user.name.charAt(0).toUpperCase()
                : "U"}
            </div>

            <div className="user-details">
              <strong>{user?.name || "User"}</strong>
              <span>{user?.role || "User"}</span>
            </div>
          </div>
        </header>

        {/* Overview cards */}
        <section className="dashboard-cards">
          <div className="dashboard-card">
            <div className="card-icon">✈</div>
            <span>Total Trips</span>
            <strong>—</strong>
            <small>Coming soon</small>
          </div>

          <div className="dashboard-card">
            <div className="card-icon">▣</div>
            <span>Bookings</span>
            <strong>—</strong>
            <small>Coming soon</small>
          </div>

          <div className="dashboard-card">
            <div className="card-icon">♙</div>
            <span>Users</span>
            <strong>—</strong>
            <small>Coming soon</small>
          </div>

          <div className="dashboard-card">
            <div className="card-icon">◷</div>
            <span>Activity</span>
            <strong>—</strong>
            <small>Coming soon</small>
          </div>
        </section>

        {/* Content area */}
        <section className="dashboard-content">
          <div className="content-header">
            <div>
              <span className="dashboard-eyebrow">
                OVERVIEW
              </span>

              <h2>Dashboard</h2>
            </div>
          </div>

          <div className="empty-dashboard">
            <div className="empty-icon">✦</div>

            <h3>Your dashboard is ready</h3>

            <p>
              DOTRIP modules will appear here as we migrate
              them from the existing application.
            </p>
          </div>
        </section>
      </main>
    </div>
  );
}

export default Dashboard;

