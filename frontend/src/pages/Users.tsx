import CrudPage, { type Field, type Column } from "../components/CrudPage";

const fields: Field[] = [
  { name: "name", label: "Name", type: "text", required: true },
  { name: "email", label: "Email", type: "email", required: true },
  { name: "phone", label: "Phone", type: "text", required: true },
  { name: "password", label: "Password", type: "password", required: true },
  { name: "age", label: "Age", type: "number", required: false },
  { name: "gender", label: "Gender", type: "select", required: false, options: [{ label: "Male", value: "MALE" }, { label: "Female", value: "FEMALE" }, { label: "Other", value: "OTHER" }] },
  { name: "role", label: "Role", type: "select", required: true, options: [{ label: "Rider", value: "RIDER" }, { label: "Vendor", value: "VENDOR" }, { label: "Driver", value: "DRIVER" }, { label: "Admin", value: "ADMIN" }, { label: "Support Agent", value: "SUPPORT_AGENT" }, { label: "Super Admin", value: "SUPER_ADMIN" }] },
];

const columns: Column[] = [
  { key: "name", label: "Name" },
  { key: "email", label: "Email" },
  { key: "phone", label: "Phone" },
  { key: "password", label: "Password" },
  { key: "age", label: "Age" },
  { key: "gender", label: "Gender" },
];

function Page() {
  return (
    <CrudPage title="Users" description="Manage DOTRIP users and roles." endpoint="/users/" fields={fields} columns={columns} />
  );
}

export default Page;