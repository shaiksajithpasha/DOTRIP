import { Activity, Car, ChevronLeft, ChevronRight, ClipboardList, FileText, LayoutDashboard, LogOut, MapPin, MessageSquare, Settings, UserCog, UserRound, Users, Warehouse } from "lucide-react";
import { NavLink, useNavigate } from "react-router-dom";
import "./Sidebar.css";

interface SidebarProps { collapsed?: boolean; onToggleSidebar: () => void; }
interface MenuItem { label:string; path:string; icon:React.ComponentType<{size?:number;strokeWidth?:number}>; }

function Sidebar({collapsed=false,onToggleSidebar}:SidebarProps){
  const navigate=useNavigate();
  const userData=localStorage.getItem("user");
  const user=(()=>{try{return userData?JSON.parse(userData):null}catch{return null}})();
  const role=user?.role||"";
  const adminMenu:MenuItem[]=[{label:"Dashboard",path:"/dashboard",icon:LayoutDashboard},{label:"Users",path:"/users",icon:Users},{label:"Drivers",path:"/drivers",icon:UserCog},{label:"Vehicle Types",path:"/vehicle-types",icon:Car},{label:"Vehicles",path:"/vehicles",icon:Car},{label:"Vendors",path:"/vendors",icon:Warehouse},{label:"Bookings",path:"/bookings",icon:ClipboardList},{label:"Trips",path:"/trips",icon:MapPin},{label:"Invoices",path:"/invoices",icon:FileText}];
  const vendorMenu:MenuItem[]=[{label:"Dashboard",path:"/dashboard",icon:LayoutDashboard},{label:"My Vehicles",path:"/vehicles",icon:Car},{label:"My Drivers",path:"/drivers",icon:UserCog},{label:"Bookings",path:"/bookings",icon:ClipboardList},{label:"Trips",path:"/trips",icon:MapPin},{label:"Invoices",path:"/invoices",icon:FileText}];
  const driverMenu:MenuItem[]=[{label:"Dashboard",path:"/dashboard",icon:LayoutDashboard},{label:"My Trips",path:"/trips",icon:MapPin},{label:"My Vehicle",path:"/vehicles",icon:Car},{label:"Trip Assistance",path:"/trip-assistance",icon:Activity}];
  const riderMenu:MenuItem[]=[{label:"Dashboard",path:"/dashboard",icon:LayoutDashboard},{label:"My Bookings",path:"/bookings",icon:ClipboardList},{label:"My Trips",path:"/trips",icon:MapPin},{label:"Invoices",path:"/invoices",icon:FileText},{label:"Feedback",path:"/feedback",icon:MessageSquare}];
  const supportMenu:MenuItem[]=[{label:"Dashboard",path:"/dashboard",icon:LayoutDashboard},{label:"Customers",path:"/users",icon:Users},{label:"Bookings",path:"/bookings",icon:ClipboardList},{label:"Trips",path:"/trips",icon:MapPin},{label:"Trip Assistance",path:"/trip-assistance",icon:Activity},{label:"Feedback",path:"/feedback",icon:MessageSquare}];
  let menuItems=adminMenu; let portalName="Admin Portal";
  switch(role){case "SUPER_ADMIN":portalName="Super Admin Portal";break;case "VENDOR":menuItems=vendorMenu;portalName="Vendor Portal";break;case "DRIVER":menuItems=driverMenu;portalName="Driver Portal";break;case "RIDER":menuItems=riderMenu;portalName="Rider Portal";break;case "SUPPORT_AGENT":menuItems=supportMenu;portalName="Support Portal";break;default:break;}
  const accountItems:MenuItem[]=[{label:"Profile",path:"/profile",icon:UserRound},{label:"Change Password",path:"/change-password",icon:Settings},{label:"Address Book",path:"/address-book",icon:MapPin}];
  const handleLogout=()=>{localStorage.removeItem("token");localStorage.removeItem("user");navigate("/login",{replace:true})};
  const renderMenu=(items:MenuItem[])=>items.map(item=>{const Icon=item.icon;return <NavLink key={item.path} to={item.path} title={collapsed?item.label:undefined} className={({isActive})=>`sidebar-link ${isActive?"active":""}`}><Icon size={18}/>{!collapsed&&<span>{item.label}</span>}</NavLink>});
  return <aside className={`sidebar ${collapsed?"sidebar-collapsed":""}`}>
    <div className="sidebar-brand"><div className="brand-logo"><img src="/gemini-svg.svg" alt="DOTRIP"/></div>{!collapsed&&<div className="brand-text"><strong>DOTRIP</strong><span>{portalName}</span></div>}</div>
    <div className="sidebar-scroll"><nav className="sidebar-nav">{renderMenu(menuItems)}</nav><section className="account-section">{!collapsed&&<h3 className="account-title">ACCOUNT</h3>}<nav className="sidebar-nav">{renderMenu(accountItems)}</nav></section></div>
    <div className="sidebar-bottom"><button type="button" className="logout-button" onClick={handleLogout} title={collapsed?"Logout":undefined}><LogOut size={18}/>{!collapsed&&<span>Logout</span>}</button></div>
    <button type="button" className="sidebar-collapse-button" onClick={onToggleSidebar} title={collapsed?"Expand sidebar":"Collapse sidebar"} aria-label={collapsed?"Expand sidebar":"Collapse sidebar"}>{collapsed?<ChevronRight size={17}/>:<ChevronLeft size={17}/>}</button>
  </aside>;
}
export default Sidebar;
