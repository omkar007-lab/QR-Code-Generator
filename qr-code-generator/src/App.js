import React, { useState } from "react";
import { QRCodeCanvas } from "qrcode.react";
import jsPDF from "jspdf";
import { saveAs } from "file-saver";
import "./App.css";

const App = () => {
  const [input, setInput] = useState("");
  const [qrCode, setQrCode] = useState("");

  const generateQRCode = () => {
    if (input.trim()) {
      setQrCode(input);
    } else {
      alert("Please enter a valid URL or UPI ID.");
    }
  };

  const downloadQRCode = (format) => {
    const canvas = document.querySelector("canvas");
    if (format === "pdf") {
      const pdf = new jsPDF();
      const imgData = canvas.toDataURL("image/png");
      pdf.addImage(imgData, "PNG", 10, 10, 180, 180);
      pdf.save("QRCode.pdf");
    } else {
      canvas.toBlob((blob) => saveAs(blob, `QRCode.${format}`), `image/${format}`);
    }
  };

  return (
    <div className="app">
      <h1 className="title">QR Code Generator</h1>
      <div className="input-section">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Enter URL or UPI ID"
          className="input-field"
        />
        <button onClick={generateQRCode} className="btn-generate">
          Generate
        </button>
      </div>
      {qrCode && (
        <div className="qr-display">
          <div className="qr-animation">
            <QRCodeCanvas value={qrCode} size={200} />
          </div>
          <div className="qr-actions">
            <button onClick={() => downloadQRCode("png")} className="btn-download">
              Download PNG
            </button>
            <button onClick={() => downloadQRCode("jpeg")} className="btn-download">
              Download JPG
            </button>
            <button onClick={() => downloadQRCode("pdf")} className="btn-download">
              Download PDF
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default App;

