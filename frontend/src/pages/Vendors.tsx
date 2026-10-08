import CrudPage, { type Field, type Column } from "../components/CrudPage";

const fields: Field[] = [
  { name: "name", label: "Name", type: "text", required: true },
  { name: "companyReg", label: "Company Registration", type: "text", required: false },
  { name: "email", label: "Email", type: "email", required: false },
  { name: "primaryMobile", label: "Primary Mobile", type: "text", required: false },
  { name: "altMobile", label: "Alternative Mobile", type: "text", required: false },
  { name: "otherNumber", label: "Other Number", type: "text", required: false },
  { name: "country", label: "Country", type: "text", required: false },
  { name: "state", label: "State", type: "text", required: false },
  { name: "city", label: "City", type: "text", required: false },
  { name: "pincode", label: "Pincode", type: "text", required: false },
  { name: "address", label: "Address", type: "text", required: false },
  { name: "userId", label: "User ID", type: "number", required: false },
  { name: "invoiceCompanyName", label: "Invoice Company Name", type: "text", required: false },
  { name: "invoiceGstin", label: "Invoice GSTIN", type: "text", required: false },
  { name: "invoicePan", label: "Invoice PAN", type: "text", required: false },
  { name: "vendorMarginPercent", label: "Vendor Margin %", type: "number", required: false },
  { name: "vendorMarginGstType", label: "Margin GST Type", type: "select", required: false, options: [{ label: "Included", value: "Included" }, { label: "Excluded", value: "Excluded" }] },
];

const columns: Column[] = [
  { key: "name", label: "Name" },
  { key: "companyReg", label: "Company Registration" },
  { key: "email", label: "Email" },
  { key: "primaryMobile", label: "Primary Mobile" },
  { key: "altMobile", label: "Alternative Mobile" },
  { key: "otherNumber", label: "Other Number" },
];

function Page() {
  return (
    <CrudPage title="Vendors" description="Manage DOTRIP vendor partners and contact information." endpoint="/vendors/" fields={fields} columns={columns} />
  );
}

export default Page;