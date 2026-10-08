import CrudPage, { type Field, type Column } from "../components/CrudPage";

const fields: Field[] = [
  { name: "userId", label: "User ID", type: "number", required: true },
  { name: "vehicleTypeId", label: "Vehicle Type ID", type: "number", required: true },
  { name: "pickupAddressId", label: "Pickup Address ID", type: "number", required: true },
  { name: "dropAddressId", label: "Drop Address ID", type: "number", required: true },
  { name: "pickupDate", label: "Pickup Date", type: "date", required: false },
  { name: "returnDate", label: "Return Date", type: "date", required: false },
  { name: "fromCityId", label: "From City ID", type: "number", required: true },
  { name: "toCityId", label: "To City ID", type: "number", required: true },
  { name: "tripTypeId", label: "Trip Type ID", type: "number", required: true },
  { name: "fare", label: "Fare", type: "number", required: true },
  { name: "numPersons", label: "Number of Persons", type: "number", required: true },
  { name: "numVehicles", label: "Number of Vehicles", type: "number", required: true },
  { name: "bookingType", label: "Booking Type", type: "text", required: true },
  { name: "status", label: "Status", type: "select", required: true, options: [{ label: "Pending", value: "PENDING" }, { label: "Confirmed", value: "CONFIRMED" }, { label: "Cancelled", value: "CANCELLED" }, { label: "Completed", value: "COMPLETED" }] },
  { name: "vendorId", label: "Vendor ID", type: "number", required: false },
];

const columns: Column[] = [
  { key: "userId", label: "User ID" },
  { key: "vehicleTypeId", label: "Vehicle Type ID" },
  { key: "pickupAddressId", label: "Pickup Address ID" },
  { key: "dropAddressId", label: "Drop Address ID" },
  { key: "pickupDate", label: "Pickup Date" },
  { key: "returnDate", label: "Return Date" },
];

function Page() {
  return (
    <CrudPage title="Bookings" description="Manage rider bookings and booking status." endpoint="/bookings/" fields={fields} columns={columns} />
  );
}

export default Page;