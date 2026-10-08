import { Bell, Menu, UserCircle } from "lucide-react";
import { useLocation } from "react-router-dom";
import "./Header.css";

interface HeaderProps { onToggleSidebar: () => void; }
const pageTitles: Record<string,string> = {"/dashboard":"Dashboard","/users":"Users","/drivers":"Drivers","/vehicle-types":"Vehicle Types","/vehicles":"Vehicles","/vendors":"Vendors","/bookings":"Bookings","/trips":"Trips","/invoices":"Invoices","/feedback":"Feedback","/trip-assistance":"Trip Assistance","/profile":"Profile","/change-password":"Change Password","/address-book":"Address Book"};

function Header({onToggleSidebar}: HeaderProps){
  const location=useLocation();
  const userData=localStorage.getItem("user");
  const user=(()=>{try{return userData?JSON.parse(userData):null}catch{return null}})();
  const userName=user?.name||"User";
  const role=user?.role||"";
  const formattedRole=role.toLowerCase().replaceAll("_"," ").replace(/\b\w/g,(letter:string)=>letter.toUpperCase());
  const pageTitle=pageTitles[location.pathname]||"DOTRIP";
  return <header className="app-header">
    <div className="header-left"><button type="button" className="sidebar-toggle" onClick={onToggleSidebar} aria-label="Toggle sidebar"><Menu size={20}/></button><div className="header-title"><span>DOTRIP</span><h2>{pageTitle}</h2></div></div>
    <div className="header-right"><button type="button" className="notification-button" aria-label="Notifications"><Bell size={19}/><span className="notification-dot"/></button><div className="header-divider"/><div className="header-user"><div className="user-avatar"><UserCircle size={32}/></div><div className="user-info"><strong>{userName}</strong><span>{formattedRole||"User"}</span></div></div></div>
  </header>;
}
export default Header;
