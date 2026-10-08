import { useCallback, useState } from "react";
import { Outlet } from "react-router-dom";
import Sidebar from "./Sidebar";
import Header from "./Header";
import "./Layout.css";

const STORAGE_KEY = "sidebar:collapsed";

function Layout() {
  const [collapsed, setCollapsed] = useState<boolean>(() => localStorage.getItem(STORAGE_KEY) === "1");
  const toggleSidebar = useCallback(() => {
    setCollapsed((previous) => {
      const next = !previous;
      localStorage.setItem(STORAGE_KEY, next ? "1" : "0");
      return next;
    });
  }, []);

  return <div className="app-layout">
    <Sidebar collapsed={collapsed} onToggleSidebar={toggleSidebar} />
    <div className="app-main">
      <Header onToggleSidebar={toggleSidebar} />
      <main className="page-content"><Outlet /></main>
    </div>
  </div>;
}
export default Layout;
