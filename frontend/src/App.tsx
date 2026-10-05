import {
  BrowserRouter,
  Navigate,
  Route,
  Routes,
} from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Drivers from "./pages/Drivers";

import Layout from "./components/Layout";
import ProtectedRoute from "./components/ProtectedRoute";
import PublicRoute from "./components/PublicRoute";

function App() {
  return (
    <BrowserRouter>
      <Routes>

        {/* Public routes */}
        <Route element={<PublicRoute />}>
          <Route
            path="/login"
            element={<Login />}
          />
        </Route>

        {/* Protected routes */}
        <Route element={<ProtectedRoute />}>
          <Route element={<Layout />}>

            <Route
              path="/dashboard"
              element={<Dashboard />}
            />

            <Route
              path="/drivers"
              element={<Drivers />}
            />

            {/* Coming modules */}
            <Route
              path="/vehicle-types"
              element={<div>Vehicle Types</div>}
            />

            <Route
              path="/vehicles"
              element={<div>Vehicles</div>}
            />

            <Route
              path="/vendors"
              element={<div>Vendors</div>}
            />

            <Route
              path="/bookings"
              element={<div>Bookings</div>}
            />

            <Route
              path="/trips"
              element={<div>Trips</div>}
            />

            <Route
              path="/invoices"
              element={<div>Invoices</div>}
            />

          </Route>
        </Route>

        {/* Default route */}
        <Route
          path="*"
          element={
            <Navigate
              to="/login"
              replace
            />
          }
        />

      </Routes>
    </BrowserRouter>
  );
}

export default App;