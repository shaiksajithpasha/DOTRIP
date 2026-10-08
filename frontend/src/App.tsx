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
import Users from "./pages/Users";
import VehicleTypes from "./pages/VehicleTypes";
import Vehicles from "./pages/Vehicles";
import Vendors from "./pages/Vendors";
import Bookings from "./pages/Bookings";
import Trips from "./pages/Trips";
import Invoices from "./pages/Invoices";

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
            <Route 
              path="/users" 
              element={<Users />} 
            />
              <Route 
              path="/vehicle-types" 
              element={<VehicleTypes />} 
            />
              <Route 
              path="/vehicles" 
              element={<Vehicles />} 
            />
              <Route 
              path="/vendors" 
              element={<Vendors />} 
            />
              <Route 
              path="/bookings" 
              element={<Bookings />} 
            />
              <Route 
              path="/trips" 
              element={<Trips />} 
            />
              <Route 
              path="/invoices" 
              element={<Invoices />} 
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