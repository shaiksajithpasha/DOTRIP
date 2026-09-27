import {
  BrowserRouter,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";

import Login from "./pages/Login";

function Dashboard() {
  return (
    <div>
      <h1>DOTRIP Dashboard</h1>
      <p>You are successfully logged in.</p>
    </div>
  );
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />

        <Route path="/dashboard" element={<Dashboard />} />

        <Route
          path="/"
          element={<Navigate to="/login" replace />}
        />

        <Route
          path="*"
          element={<Navigate to="/login" replace />}
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;