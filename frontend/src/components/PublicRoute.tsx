
import { Navigate, Outlet } from "react-router-dom";

function PublicRoute() {
  const token = localStorage.getItem("token");
  const userData = localStorage.getItem("user");

  if (token && userData) {
    return <Navigate to="/dashboard" replace />;
  }

  return <Outlet />;
}

export default PublicRoute;