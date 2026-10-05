
import { useEffect, useState } from "react";
import "./Drivers.css";

interface Driver {
  id: number;
  fullName: string;
  phone: string;
  email: string;
  licenseNumber: string;
  licenseExpiry: string;
  isPartTime: boolean;
  isAvailable: boolean;
  licenseImage?: string | null;
  rcImage?: string | null;
  profileImage?: string | null;
  whatsappPhone?: string | null;
  altPhone?: string | null;
  licenseIssueDate?: string | null;
  dob?: string | null;
  gender?: string | null;
  bloodGroup?: string | null;
  aadhaarNumber?: string | null;
  panNumber?: string | null;
  voterId?: string | null;
  address?: string | null;
  assignedVehicleId?: number | null;
  vendorId?: number | null;
  userId?: number | null;
}

interface DriverForm {
  fullName: string;
  phone: string;
  email: string;
  password: string;
  licenseNumber: string;
  licenseExpiry: string;
  isPartTime: boolean;
  isAvailable: boolean;
  whatsappPhone: string;
  altPhone: string;
  licenseIssueDate: string;
  dob: string;
  gender: string;
  bloodGroup: string;
  aadhaarNumber: string;
  panNumber: string;
  voterId: string;
  address: string;
  assignedVehicleId: string;
  vendorId: string;
}

const emptyForm: DriverForm = {
  fullName: "",
  phone: "",
  email: "",
  password: "",
  licenseNumber: "",
  licenseExpiry: "",
  isPartTime: false,
  isAvailable: true,
  whatsappPhone: "",
  altPhone: "",
  licenseIssueDate: "",
  dob: "",
  gender: "",
  bloodGroup: "",
  aadhaarNumber: "",
  panNumber: "",
  voterId: "",
  address: "",
  assignedVehicleId: "",
  vendorId: "",
};

function Drivers() {
  const [drivers, setDrivers] = useState<Driver[]>([]);
  const [form, setForm] = useState<DriverForm>(emptyForm);
  const [showForm, setShowForm] = useState(false);
  const [editingDriver, setEditingDriver] = useState<Driver | null>(null);

  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const token = localStorage.getItem("token");

const loadDrivers = async () => {
  try {
    const token = localStorage.getItem("token");

    const response = await fetch(
      `${import.meta.env.VITE_API_URL}/drivers/`,
      {
        method: "GET",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );

    if (!response.ok) {
      throw new Error("Failed to load drivers");
    }

    const data: Driver[] = await response.json();

    setDrivers(data);
    setError("");
  } catch (err) {
    console.error(err);
    setError("Unable to load drivers");
  } finally {
    setLoading(false);
  }
};

useEffect(() => {
  let cancelled = false;

  const fetchDrivers = async () => {
    try {
      const token = localStorage.getItem("token");

      const response = await fetch(
        `${import.meta.env.VITE_API_URL}/drivers/`,
        {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      if (!response.ok) {
        throw new Error("Failed to load drivers");
      }

      const data: Driver[] = await response.json();

      if (!cancelled) {
        setDrivers(data);
        setError("");
        setLoading(false);
      }
    } catch (err) {
      console.error(err);

      if (!cancelled) {
        setError("Unable to load drivers");
        setLoading(false);
      }
    }
  };

  fetchDrivers();

  return () => {
    cancelled = true;
  };
}, []);

  const handleChange = (
    event: React.ChangeEvent<
      HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement
    >
  ) => {
    const { name, value, type } = event.target;

    setForm((previous) => ({
      ...previous,
      [name]:
        type === "checkbox"
          ? (event.target as HTMLInputElement).checked
          : value,
    }));
  };

  const resetForm = () => {
    setForm(emptyForm);
    setEditingDriver(null);
    setShowForm(false);
  };

  const handleAddDriver = () => {
    setEditingDriver(null);
    setForm(emptyForm);
    setError("");
    setSuccess("");
    setShowForm(true);
  };

  const handleEditDriver = (driver: Driver) => {
    setEditingDriver(driver);

    setForm({
      fullName: driver.fullName || "",
      phone: driver.phone || "",
      email: driver.email || "",
      password: "",
      licenseNumber: driver.licenseNumber || "",
      licenseExpiry: driver.licenseExpiry || "",
      isPartTime: driver.isPartTime ?? false,
      isAvailable: driver.isAvailable ?? true,
      whatsappPhone: driver.whatsappPhone || "",
      altPhone: driver.altPhone || "",
      licenseIssueDate: driver.licenseIssueDate || "",
      dob: driver.dob || "",
      gender: driver.gender || "",
      bloodGroup: driver.bloodGroup || "",
      aadhaarNumber: driver.aadhaarNumber || "",
      panNumber: driver.panNumber || "",
      voterId: driver.voterId || "",
      address: driver.address || "",
      assignedVehicleId:
        driver.assignedVehicleId !== null &&
        driver.assignedVehicleId !== undefined
          ? String(driver.assignedVehicleId)
          : "",
      vendorId:
        driver.vendorId !== null && driver.vendorId !== undefined
          ? String(driver.vendorId)
          : "",
    });

    setError("");
    setSuccess("");
    setShowForm(true);
  };

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    setSaving(true);
    setError("");
    setSuccess("");

    try {
      const payload: Record<string, unknown> = {
        fullName: form.fullName,
        phone: form.phone,
        email: form.email,
        licenseNumber: form.licenseNumber,
        licenseExpiry: form.licenseExpiry,
        isPartTime: form.isPartTime,
        isAvailable: form.isAvailable,
        whatsappPhone: form.whatsappPhone || null,
        altPhone: form.altPhone || null,
        licenseIssueDate: form.licenseIssueDate || null,
        dob: form.dob || null,
        gender: form.gender || null,
        bloodGroup: form.bloodGroup || null,
        aadhaarNumber: form.aadhaarNumber || null,
        panNumber: form.panNumber || null,
        voterId: form.voterId || null,
        address: form.address || null,
        assignedVehicleId: form.assignedVehicleId
          ? Number(form.assignedVehicleId)
          : null,
        vendorId: form.vendorId ? Number(form.vendorId) : null,
      };

      // Password is required only when creating a driver.
      if (!editingDriver) {
        payload.password = form.password;
      }

      const url = editingDriver
        ? `${import.meta.env.VITE_API_URL}/drivers/${editingDriver.id}`
        : `${import.meta.env.VITE_API_URL}/drivers/`;

      const method = editingDriver ? "PUT" : "POST";

      const response = await fetch(url, {
        method,
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(payload),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Failed to save driver");
      }

      setSuccess(
        editingDriver
          ? "Driver updated successfully"
          : "Driver created successfully"
      );

      resetForm();
      await loadDrivers();
    } catch (err) {
      console.error(err);

      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError("Unable to save driver");
      }
    } finally {
      setSaving(false);
    }
  };

  const handleDeleteDriver = async (driverId: number) => {
    const confirmed = window.confirm(
      "Are you sure you want to delete this driver?"
    );

    if (!confirmed) {
      return;
    }

    try {
      setError("");
      setSuccess("");

      const response = await fetch(
        `${import.meta.env.VITE_API_URL}/drivers/${driverId}`,
        {
          method: "DELETE",
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Failed to delete driver");
      }

      setSuccess("Driver deleted successfully");
      await loadDrivers();
    } catch (err) {
      console.error(err);

      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError("Unable to delete driver");
      }
    }
  };

  return (
    <div className="drivers-page">
      <div className="drivers-header">
        <div>
          <h1>Drivers</h1>
          <p>Manage DOTRIP drivers</p>
        </div>

        <button className="add-driver-button" onClick={handleAddDriver}>
          + Add Driver
        </button>
      </div>

      {success && <div className="success-message">{success}</div>}

      {error && <div className="error-message">{error}</div>}

      {showForm && (
        <div className="driver-form-card">
          <div className="form-header">
            <h2>{editingDriver ? "Edit Driver" : "Add Driver"}</h2>

            <button
              type="button"
              className="close-button"
              onClick={resetForm}
            >
              ×
            </button>
          </div>

          <form onSubmit={handleSubmit}>
            <div className="form-section">
              <h3>Basic Information</h3>

              <div className="form-grid">
                <div className="form-group">
                  <label>Full Name *</label>
                  <input
                    name="fullName"
                    value={form.fullName}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="form-group">
                  <label>Phone *</label>
                  <input
                    name="phone"
                    value={form.phone}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="form-group">
                  <label>Email *</label>
                  <input
                    type="email"
                    name="email"
                    value={form.email}
                    onChange={handleChange}
                    required
                  />
                </div>

                {!editingDriver && (
                  <div className="form-group">
                    <label>Password *</label>
                    <input
                      type="password"
                      name="password"
                      value={form.password}
                      onChange={handleChange}
                      minLength={6}
                      required
                    />
                  </div>
                )}

                <div className="form-group">
                  <label>Gender</label>
                  <select
                    name="gender"
                    value={form.gender}
                    onChange={handleChange}
                  >
                    <option value="">Select Gender</option>
                    <option value="MALE">Male</option>
                    <option value="FEMALE">Female</option>
                    <option value="OTHER">Other</option>
                  </select>
                </div>

                <div className="form-group">
                  <label>Date of Birth</label>
                  <input
                    type="date"
                    name="dob"
                    value={form.dob}
                    onChange={handleChange}
                  />
                </div>

                <div className="form-group">
                  <label>Blood Group</label>
                  <input
                    name="bloodGroup"
                    value={form.bloodGroup}
                    onChange={handleChange}
                    placeholder="e.g. O+"
                  />
                </div>

                <div className="form-group">
                  <label>WhatsApp Phone</label>
                  <input
                    name="whatsappPhone"
                    value={form.whatsappPhone}
                    onChange={handleChange}
                  />
                </div>

                <div className="form-group">
                  <label>Alternative Phone</label>
                  <input
                    name="altPhone"
                    value={form.altPhone}
                    onChange={handleChange}
                  />
                </div>
              </div>
            </div>

            <div className="form-section">
              <h3>License Information</h3>

              <div className="form-grid">
                <div className="form-group">
                  <label>License Number *</label>
                  <input
                    name="licenseNumber"
                    value={form.licenseNumber}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="form-group">
                  <label>License Issue Date</label>
                  <input
                    type="date"
                    name="licenseIssueDate"
                    value={form.licenseIssueDate}
                    onChange={handleChange}
                  />
                </div>

                <div className="form-group">
                  <label>License Expiry *</label>
                  <input
                    type="date"
                    name="licenseExpiry"
                    value={form.licenseExpiry}
                    onChange={handleChange}
                    required
                  />
                </div>
              </div>
            </div>

            <div className="form-section">
              <h3>Identity Information</h3>

              <div className="form-grid">
                <div className="form-group">
                  <label>Aadhaar Number</label>
                  <input
                    name="aadhaarNumber"
                    value={form.aadhaarNumber}
                    onChange={handleChange}
                  />
                </div>

                <div className="form-group">
                  <label>PAN Number</label>
                  <input
                    name="panNumber"
                    value={form.panNumber}
                    onChange={handleChange}
                  />
                </div>

                <div className="form-group">
                  <label>Voter ID</label>
                  <input
                    name="voterId"
                    value={form.voterId}
                    onChange={handleChange}
                  />
                </div>
              </div>
            </div>

            <div className="form-section">
              <h3>Assignment</h3>

              <div className="form-grid">
                <div className="form-group">
                  <label>Vehicle ID</label>
                  <input
                    type="number"
                    name="assignedVehicleId"
                    value={form.assignedVehicleId}
                    onChange={handleChange}
                    placeholder="Leave empty if not assigned"
                  />
                </div>

                <div className="form-group">
                  <label>Vendor ID</label>
                  <input
                    type="number"
                    name="vendorId"
                    value={form.vendorId}
                    onChange={handleChange}
                    placeholder="Leave empty if not assigned"
                  />
                </div>
              </div>
            </div>

            <div className="form-section">
              <h3>Address</h3>

              <div className="form-group">
                <label>Address</label>
                <textarea
                  name="address"
                  value={form.address}
                  onChange={handleChange}
                  rows={3}
                />
              </div>
            </div>

            <div className="form-section">
              <h3>Status</h3>

              <div className="checkbox-row">
                <label>
                  <input
                    type="checkbox"
                    name="isPartTime"
                    checked={form.isPartTime}
                    onChange={handleChange}
                  />
                  Part-time Driver
                </label>

                <label>
                  <input
                    type="checkbox"
                    name="isAvailable"
                    checked={form.isAvailable}
                    onChange={handleChange}
                  />
                  Available
                </label>
              </div>
            </div>

            <div className="form-actions">
              <button
                type="button"
                className="cancel-button"
                onClick={resetForm}
              >
                Cancel
              </button>

              <button
                type="submit"
                className="save-button"
                disabled={saving}
              >
                {saving
                  ? "Saving..."
                  : editingDriver
                    ? "Update Driver"
                    : "Create Driver"}
              </button>
            </div>
          </form>
        </div>
      )}

      <div className="drivers-card">
        {loading ? (
          <div className="loading">Loading drivers...</div>
        ) : drivers.length === 0 ? (
          <div className="empty-state">No drivers found.</div>
        ) : (
          <div className="table-wrapper">
            <table className="drivers-table">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Name</th>
                  <th>Phone</th>
                  <th>Email</th>
                  <th>License</th>
                  <th>Availability</th>
                  <th>Type</th>
                  <th>User ID</th>
                  <th>Actions</th>
                </tr>
              </thead>

              <tbody>
                {drivers.map((driver) => (
                  <tr key={driver.id}>
                    <td>{driver.id}</td>

                    <td>
                      <strong>{driver.fullName}</strong>
                    </td>

                    <td>{driver.phone}</td>

                    <td>{driver.email}</td>

                    <td>
                      <div>{driver.licenseNumber}</div>
                      <small>{driver.licenseExpiry}</small>
                    </td>

                    <td>
                      <span
                        className={
                          driver.isAvailable
                            ? "status available"
                            : "status unavailable"
                        }
                      >
                        {driver.isAvailable ? "Available" : "Unavailable"}
                      </span>
                    </td>

                    <td>
                      {driver.isPartTime ? "Part-time" : "Full-time"}
                    </td>

                    <td>{driver.userId ?? "-"}</td>

                    <td>
                      <div className="action-buttons">
                        <button
                          className="edit-button"
                          onClick={() => handleEditDriver(driver)}
                        >
                          Edit
                        </button>

                        <button
                          className="delete-button"
                          onClick={() => handleDeleteDriver(driver.id)}
                        >
                          Delete
                        </button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}

export default Drivers;