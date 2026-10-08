import CrudPage, { type Field, type Column } from "../components/CrudPage";

const fields: Field[] = [
  { name: "invoiceNumber", label: "Invoice Number", type: "text", required: true },
  { name: "subtotal", label: "Subtotal", type: "number", required: true },
  { name: "vendorCommission", label: "Vendor Commission", type: "number", required: true },
  { name: "adminCommission", label: "Admin Commission", type: "number", required: true },
  { name: "totalAmount", label: "Total Amount", type: "number", required: true },
  { name: "pdfUrl", label: "PDF URL", type: "text", required: false },
  { name: "tripId", label: "Trip ID", type: "number", required: true },
  { name: "vendorId", label: "Vendor ID", type: "number", required: true },
  { name: "userId", label: "User ID", type: "number", required: true },
];

const columns: Column[] = [
  { key: "invoiceNumber", label: "Invoice Number" },
  { key: "subtotal", label: "Subtotal" },
  { key: "vendorCommission", label: "Vendor Commission" },
  { key: "adminCommission", label: "Admin Commission" },
  { key: "totalAmount", label: "Total Amount" },
  { key: "pdfUrl", label: "PDF URL" },
];

function Page() {
  return (
    <CrudPage title="Invoices" description="Manage trip invoices and commission details." endpoint="/invoices/" fields={fields} columns={columns} />
  );
}

export default Page;