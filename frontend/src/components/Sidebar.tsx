import { NavLink, useNavigate } from "react-router-dom";
import {
  LayoutDashboard,
  Users,
  CarFront,
  Car,
  Building2,
  CalendarCheck,
  Route,
  Receipt,
  LogOut,
  Settings,
  ChevronRight,
  MessageSquare,
} from "lucide-react";

import "./Sidebar.css";

function Sidebar() {
  const navigate = useNavigate();

const userData = localStorage.getItem("user");

const role = (() => {
  try {
    const parsedUser = userData
      ? JSON.parse(userData)
      : null;

    return parsedUser?.role || "";
  } catch {
    return "";
  }
})();

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    navigate("/login");
  };

  const adminMenu = [
    {
      name: "Dashboard",
      path: "/dashboard",
      icon: LayoutDashboard,
    },
    {
      name: "Users",
      path: "/users",
      icon: Users,
    },
    {
      name: "Drivers",
      path: "/drivers",
      icon: CarFront,
    },
    {
      name: "Vehicle Types",
      path: "/vehicle-types",
      icon: Car,
    },
    {
      name: "Vehicles",
      path: "/vehicles",
      icon: CarFront,
    },
    {
      name: "Vendors",
      path: "/vendors",
      icon: Building2,
    },
    {
      name: "Bookings",
      path: "/bookings",
      icon: CalendarCheck,
    },
    {
      name: "Trips",
      path: "/trips",
      icon: Route,
    },
    {
      name: "Invoices",
      path: "/invoices",
      icon: Receipt,
    },
  ];

  const vendorMenu = [
    {
      name: "Dashboard",
      path: "/dashboard",
      icon: LayoutDashboard,
    },
    {
      name: "My Vehicles",
      path: "/vehicles",
      icon: Car,
    },
    {
      name: "My Drivers",
      path: "/drivers",
      icon: CarFront,
    },
    {
      name: "Bookings",
      path: "/bookings",
      icon: CalendarCheck,
    },
    {
      name: "Trips",
      path: "/trips",
      icon: Route,
    },
    {
      name: "Invoices",
      path: "/invoices",
      icon: Receipt,
    },
  ];

  const driverMenu = [
    {
      name: "Dashboard",
      path: "/dashboard",
      icon: LayoutDashboard,
    },
    {
      name: "My Trips",
      path: "/trips",
      icon: Route,
    },
    {
      name: "My Vehicle",
      path: "/vehicles",
      icon: Car,
    },
    {
      name: "Trip Assistance",
      path: "/trip-assistance",
      icon: MessageSquare,
    },
  ];

  const riderMenu = [
    {
      name: "Dashboard",
      path: "/dashboard",
      icon: LayoutDashboard,
    },
    {
      name: "My Bookings",
      path: "/bookings",
      icon: CalendarCheck,
    },
    {
      name: "My Trips",
      path: "/trips",
      icon: Route,
    },
    {
      name: "Invoices",
      path: "/invoices",
      icon: Receipt,
    },
    {
      name: "Feedback",
      path: "/feedback",
      icon: MessageSquare,
    },
  ];

  const supportMenu = [
    {
      name: "Dashboard",
      path: "/dashboard",
      icon: LayoutDashboard,
    },
    {
      name: "Customers",
      path: "/users",
      icon: Users,
    },
    {
      name: "Bookings",
      path: "/bookings",
      icon: CalendarCheck,
    },
    {
      name: "Trips",
      path: "/trips",
      icon: Route,
    },
    {
      name: "Trip Assistance",
      path: "/trip-assistance",
      icon: MessageSquare,
    },
    {
      name: "Feedback",
      path: "/feedback",
      icon: MessageSquare,
    },
  ];

  let menuItems = adminMenu;
  let portalName = "Admin Portal";

  if (role === "VENDOR") {
    menuItems = vendorMenu;
    portalName = "Vendor Portal";
  } else if (role === "DRIVER") {
    menuItems = driverMenu;
    portalName = "Driver Portal";
  } else if (role === "RIDER") {
    menuItems = riderMenu;
    portalName = "Rider Portal";
  } else if (role === "SUPPORT_AGENT") {
    menuItems = supportMenu;
    portalName = "Support Portal";
  } else if (
    role === "ADMIN" ||
    role === "SUPER_ADMIN"
  ) {
    menuItems = adminMenu;
    portalName =
      role === "SUPER_ADMIN"
        ? "Super Admin Portal"
        : "Admin Portal";
  }

  return (
    <aside className="sidebar">
      {/* Logo */}
      <div className="sidebar-brand">
        <div className="brand-logo">
          <img
            src="/gemini-svg.svg"
            alt="DOTRIP Logo"
          />
        </div>

        <div className="brand-text">
          <h1>DOTRIP</h1>
          <span>{portalName}</span>
        </div>
      </div>

      {/* Navigation */}
      <div className="sidebar-section">
        <p className="sidebar-section-title">
          MAIN MENU
        </p>

        <nav className="sidebar-nav">
          {menuItems.map((item) => {
            const Icon = item.icon;

            return (
              <NavLink
                key={item.path}
                to={item.path}
                className={({ isActive }) =>
                  isActive
                    ? "sidebar-link active"
                    : "sidebar-link"
                }
              >
                <Icon
                  size={19}
                  strokeWidth={1.8}
                />

                <span>{item.name}</span>

                <ChevronRight
                  className="sidebar-arrow"
                  size={15}
                  strokeWidth={1.8}
                />
              </NavLink>
            );
          })}
        </nav>
      </div>

      {/* Bottom */}
      <div className="sidebar-bottom">
        <NavLink
          to="/settings"
          className={({ isActive }) =>
            isActive
              ? "sidebar-link active"
              : "sidebar-link"
          }
        >
          <Settings
            size={19}
            strokeWidth={1.8}
          />

          <span>Settings</span>

          <ChevronRight
            className="sidebar-arrow"
            size={15}
            strokeWidth={1.8}
          />
        </NavLink>

        <button
          className="logout-button"
          onClick={handleLogout}
        >
          <LogOut
            size={19}
            strokeWidth={1.8}
          />

          <span>Logout</span>
        </button>
      </div>
    </aside>
  );
}

export default Sidebar;