import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import QRCodeGenerator from "./components/QRCodeGenerator.jsx";  // Correct path to the component
import reportWebVitals from "./reportWebVitals";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <QRCodeGenerator />  {/* Render the QRCodeGenerator component */}
  </React.StrictMode>
);

reportWebVitals();
