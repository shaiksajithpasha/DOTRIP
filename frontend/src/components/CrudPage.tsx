import { useEffect, useMemo, useState } from "react";
import { Pencil, Plus, RefreshCw, Search, Trash2, X } from "lucide-react";
import "./CrudPage.css";

export type Field = {
  name: string;
  label: string;
  type?: "text" | "number" | "email" | "password" | "date" | "datetime-local" | "select";
  required?: boolean;
  options?: { label: string; value: string }[];
};

export type Column = {
  key: string;
  label: string;
};

interface CrudPageProps {
  title: string;
  description: string;
  endpoint: string;
  fields: Field[];
  columns: Column[];
  idKey?: string;
  createOnly?: boolean;
}

function CrudPage({
  title,
  description,
  endpoint,
  fields,
  columns,
  idKey = "id",
  createOnly = false,
}: CrudPageProps) {
  const [items, setItems] = useState<Record<string, unknown>[]>([]);
  const [form, setForm] = useState<Record<string, string>>({});
  const [editingId, setEditingId] = useState<number | string | null>(null);
  const [showForm, setShowForm] = useState(false);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const apiUrl = import.meta.env.VITE_API_URL;

  const emptyForm = useMemo(
    () =>
      fields.reduce<Record<string, string>>((result, field) => {
        result[field.name] = "";
        return result;
      }, {}),
    [fields]
  );

  const loadItems = async () => {
    setLoading(true);
    setError("");

    try {
      const token = localStorage.getItem("token");

      const response = await fetch(`${apiUrl}${endpoint}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || `Failed to load ${title.toLowerCase()}`);
      }

      setItems(Array.isArray(data) ? data : []);
    } catch (err) {
      setError(err instanceof Error ? err.message : `Unable to load ${title.toLowerCase()}`);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    let cancelled = false;

    const run = async () => {
      try {
        const token = localStorage.getItem("token");
        const response = await fetch(`${apiUrl}${endpoint}`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        const data = await response.json();

        if (!response.ok) {
          throw new Error(data.detail || `Failed to load ${title.toLowerCase()}`);
        }

        if (!cancelled) {
          setItems(Array.isArray(data) ? data : []);
          setError("");
          setLoading(false);
        }
      } catch (err) {
        if (!cancelled) {
          setError(
            err instanceof Error
              ? err.message
              : `Unable to load ${title.toLowerCase()}`
          );
          setLoading(false);
        }
      }
    };

    run();

    return () => {
      cancelled = true;
    };
  }, [apiUrl, endpoint, title]);

  const openAdd = () => {
    setForm(emptyForm);
    setEditingId(null);
    setError("");
    setSuccess("");
    setShowForm(true);
  };

  const openEdit = (item: Record<string, unknown>) => {
    const next = { ...emptyForm };

    fields.forEach((field) => {
      const value = item[field.name];
      if (value !== null && value !== undefined) {
        next[field.name] =
          field.type === "datetime-local"
            ? String(value).slice(0, 16)
            : String(value);
      }
    });

    setForm(next);
    setEditingId((item[idKey] as number | string) ?? null);
    setError("");
    setSuccess("");
    setShowForm(true);
  };

  const closeForm = () => {
    setShowForm(false);
    setEditingId(null);
    setForm(emptyForm);
  };

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setSaving(true);
    setError("");
    setSuccess("");

    try {
      const payload: Record<string, unknown> = {};

      fields.forEach((field) => {
        const value = form[field.name];

        if (value === "" || value === undefined) {
          if (field.required) {
            payload[field.name] = value;
          } else {
            payload[field.name] = null;
          }
          return;
        }

        if (field.type === "number") {
          payload[field.name] = Number(value);
        } else {
          payload[field.name] = value;
        }
      });

      const url =
        editingId === null
          ? `${apiUrl}${endpoint}`
          : `${apiUrl}${endpoint}${editingId}`;

      const response = await fetch(url, {
        method: editingId === null ? "POST" : "PUT",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
        body: JSON.stringify(payload),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || `Failed to save ${title.toLowerCase()}`);
      }

      setSuccess(
        editingId === null
          ? `${title.slice(0, -1)} created successfully`
          : `${title.slice(0, -1)} updated successfully`
      );

      closeForm();
      await loadItems();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Unable to save");
    } finally {
      setSaving(false);
    }
  };

  const handleDelete = async (id: number | string) => {
    if (!window.confirm(`Delete this ${title.slice(0, -1).toLowerCase()}?`)) {
      return;
    }

    try {
      const response = await fetch(`${apiUrl}${endpoint}${id}`, {
        method: "DELETE",
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Delete failed");
      }

      setSuccess(`${title.slice(0, -1)} deleted successfully`);
      await loadItems();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Unable to delete");
    }
  };

  const filteredItems = items.filter((item) =>
    JSON.stringify(item).toLowerCase().includes(search.toLowerCase())
  );

  const formatValue = (value: unknown) => {
    if (value === null || value === undefined || value === "") return "—";
    if (typeof value === "boolean") return value ? "Yes" : "No";
    return String(value);
  };

  return (
    <div className="crud-page">
      <div className="crud-header">
        <div>
          <h1>{title}</h1>
          <p>{description}</p>
        </div>

        <button className="crud-primary-button" onClick={openAdd}>
          <Plus size={17} />
          Add {title.endsWith("s") ? title.slice(0, -1) : title}
        </button>
      </div>

      {success && <div className="crud-message success">{success}</div>}
      {error && <div className="crud-message error">{error}</div>}

      <div className="crud-toolbar">
        <div className="crud-search">
          <Search size={17} />
          <input
            value={search}
            onChange={(event) => setSearch(event.target.value)}
            placeholder={`Search ${title.toLowerCase()}...`}
          />
        </div>

        <button className="crud-refresh" onClick={loadItems} title="Refresh">
          <RefreshCw size={17} />
          Refresh
        </button>
      </div>

      <div className="crud-card">
        {loading ? (
          <div className="crud-state">Loading {title.toLowerCase()}...</div>
        ) : filteredItems.length === 0 ? (
          <div className="crud-state">
            <h3>No {title.toLowerCase()} found</h3>
            <p>Add your first record to get started.</p>
          </div>
        ) : (
          <div className="crud-table-wrap">
            <table className="crud-table">
              <thead>
                <tr>
                  {columns.map((column) => (
                    <th key={column.key}>{column.label}</th>
                  ))}
                  {!createOnly && <th>Actions</th>}
                </tr>
              </thead>

              <tbody>
                {filteredItems.map((item, index) => (
                  <tr key={String(item[idKey] ?? index)}>
                    {columns.map((column) => (
                      <td key={column.key}>
                        {formatValue(item[column.key])}
                      </td>
                    ))}

                    {!createOnly && (
                      <td>
                        <div className="crud-actions">
                          <button
                            className="icon-button edit"
                            onClick={() => openEdit(item)}
                            title="Edit"
                          >
                            <Pencil size={15} />
                          </button>

                          <button
                            className="icon-button delete"
                            onClick={() =>
                              handleDelete(item[idKey] as number | string)
                            }
                            title="Delete"
                          >
                            <Trash2 size={15} />
                          </button>
                        </div>
                      </td>
                    )}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>

      {showForm && (
        <div className="crud-modal-backdrop">
          <div className="crud-modal">
            <div className="crud-modal-header">
              <div>
                <h2>
                  {editingId === null ? "Add" : "Edit"}{" "}
                  {title.endsWith("s") ? title.slice(0, -1) : title}
                </h2>
                <p>Enter the required information below.</p>
              </div>

              <button className="crud-close" onClick={closeForm}>
                <X size={19} />
              </button>
            </div>

            <form onSubmit={handleSubmit}>
              <div className="crud-form-grid">
                {fields.map((field) => (
                  <label className="crud-field" key={field.name}>
                    <span>
                      {field.label}
                      {field.required && " *"}
                    </span>

                    {field.type === "select" ? (
                      <select
                        value={form[field.name] ?? ""}
                        onChange={(event) =>
                          setForm((previous) => ({
                            ...previous,
                            [field.name]: event.target.value,
                          }))
                        }
                        required={field.required}
                      >
                        <option value="">Select</option>
                        {field.options?.map((option) => (
                          <option key={option.value} value={option.value}>
                            {option.label}
                          </option>
                        ))}
                      </select>
                    ) : (
                      <input
                        type={field.type ?? "text"}
                        value={form[field.name] ?? ""}
                        onChange={(event) =>
                          setForm((previous) => ({
                            ...previous,
                            [field.name]: event.target.value,
                          }))
                        }
                        required={field.required}
                      />
                    )}
                  </label>
                ))}
              </div>

              <div className="crud-form-actions">
                <button type="button" className="crud-secondary" onClick={closeForm}>
                  Cancel
                </button>

                <button type="submit" className="crud-primary-button" disabled={saving}>
                  {saving ? "Saving..." : "Save"}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}

export default CrudPage;
