import CrudPage, { type Field, type Column } from "../components/CrudPage";

const fields: Field[] = [
  { name: "registrationNumber", label: "Registration Number", type: "text", required: true },
  { name: "chassisNumber", label: "Chassis Number", type: "text", required: false },
  { name: "status", label: "Status", type: "select", required: true, options: [{ label: "Available", value: "AVAILABLE" }, { label: "Assigned", value: "ASSIGNED" }, { label: "Inactive", value: "INACTIVE" }, { label: "Maintenance", value: "MAINTENANCE" }] },
  { name: "vehicleTypeId", label: "Vehicle Type ID", type: "number", required: true },
  { name: "vendorId", label: "Vendor ID", type: "number", required: false },
  { name: "driverOwnerId", label: "Driver Owner ID", type: "number", required: false },
  { name: "lastServicedDate", label: "Last Serviced Date", type: "date", required: false },
  { name: "vehicleExpiryDate", label: "Vehicle Expiry Date", type: "date", required: false },
  { name: "extraKmCharge", label: "Extra Km Charge", type: "number", required: false },
  { name: "earlyMorningCharges", label: "Early Morning Charges", type: "number", required: false },
  { name: "eveningCharges", label: "Evening Charges", type: "number", required: false },
  { name: "insurancePolicyNumber", label: "Insurance Policy Number", type: "text", required: false },
  { name: "insuranceStartDate", label: "Insurance Start Date", type: "date", required: false },
  { name: "insuranceEndDate", label: "Insurance End Date", type: "date", required: false },
  { name: "insuranceContactNumber", label: "Insurance Contact Number", type: "text", required: false },
  { name: "rtoCode", label: "RTO Code", type: "text", required: false },
  { name: "image", label: "Image URL", type: "text", required: false },
  { name: "videoUrl", label: "Video URL", type: "text", required: false },
];

const columns: Column[] = [
  { key: "registrationNumber", label: "Registration Number" },
  { key: "chassisNumber", label: "Chassis Number" },
  { key: "status", label: "Status" },
  { key: "vehicleTypeId", label: "Vehicle Type ID" },
  { key: "vendorId", label: "Vendor ID" },
  { key: "driverOwnerId", label: "Driver Owner ID" },
];

function Page() {
  return (
    <CrudPage title="Vehicles" description="Manage fleet vehicles and their assignments." endpoint="/vehicles/" fields={fields} columns={columns} />
  );
}

export default Page;