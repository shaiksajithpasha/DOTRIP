import CrudPage, { type Field, type Column } from "../components/CrudPage";

const fields: Field[] = [
  { name: "bookingId", label: "Booking ID", type: "number", required: true },
  { name: "riderId", label: "Rider ID", type: "number", required: true },
  { name: "driverId", label: "Driver ID", type: "number", required: true },
  { name: "vehicleId", label: "Vehicle ID", type: "number", required: true },
  { name: "vendorId", label: "Vendor ID", type: "number", required: true },
  { name: "startTime", label: "Start Time", type: "datetime-local", required: true },
  { name: "endTime", label: "End Time", type: "datetime-local", required: false },
  { name: "status", label: "Status", type: "select", required: true, options: [{ label: "Scheduled", value: "SCHEDULED" }, { label: "Ongoing", value: "ONGOING" }, { label: "Completed", value: "COMPLETED" }, { label: "Cancelled", value: "CANCELLED" }] },
  { name: "distance", label: "Distance", type: "number", required: false },
  { name: "fare", label: "Fare", type: "number", required: false },
  { name: "breakdownReported", label: "Breakdown Reported", type: "select", required: false, options: [{ label: "Yes", value: "true" }, { label: "No", value: "false" }] },
  { name: "breakdownNotes", label: "Breakdown Notes", type: "text", required: false },
];

const columns: Column[] = [
  { key: "bookingId", label: "Booking ID" },
  { key: "riderId", label: "Rider ID" },
  { key: "driverId", label: "Driver ID" },
  { key: "vehicleId", label: "Vehicle ID" },
  { key: "vendorId", label: "Vendor ID" },
  { key: "startTime", label: "Start Time" },
];

function Page() {
  return (
    <CrudPage title="Trips" description="Track active, completed and assigned trips." endpoint="/trips/" fields={fields} columns={columns} />
  );
}

export default Page;