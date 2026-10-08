import CrudPage, { type Field, type Column } from "../components/CrudPage";

const fields: Field[] = [
  { name: "name", label: "Name", type: "text", required: true },
  { name: "estimatedRatePerKm", label: "Estimated Rate / Km", type: "number", required: true },
  { name: "baseFare", label: "Base Fare", type: "number", required: true },
  { name: "seatingCapacity", label: "Seating Capacity", type: "number", required: true },
  { name: "image", label: "Image URL", type: "text", required: false },
];

const columns: Column[] = [
  { key: "name", label: "Name" },
  { key: "estimatedRatePerKm", label: "Estimated Rate / Km" },
  { key: "baseFare", label: "Base Fare" },
  { key: "seatingCapacity", label: "Seating Capacity" },
  { key: "image", label: "Image URL" },
];

function Page() {
  return (
    <CrudPage title="Vehicle Types" description="Manage vehicle categories, fares and seating capacity." endpoint="/vehicle-types/" fields={fields} columns={columns} />
  );
}

export default Page;