import React, { useState } from "react";
import { QRCodeCanvas } from "qrcode.react";
import { saveAs } from "file-saver";
import jsPDF from "jspdf";
import "../App.css";  // Correct path to App.css

const QRCodeGenerator = () => {
  const [input, setInput] = useState("");
  const [qrCode, setQrCode] = useState("");
  const [showDropdown, setShowDropdown] = useState(false);

  // Generate QR Code
  const generateQRCode = () => {
    if (input.trim()) {
      setQrCode(input);
    } else {
      alert("Please enter a valid URL or UPI ID.");
    }
  };

  // Download QR Code
  const downloadQRCode = (format) => {
    const canvas = document.querySelector("canvas");
    if (format === "pdf") {
      const pdf = new jsPDF();
      const imgData = canvas.toDataURL("image/png");
      pdf.addImage(imgData, "PNG", 10, 10, 180, 180); // Adjust position and size
      pdf.save("qrcode.pdf");
    } else {
      canvas.toBlob((blob) => saveAs(blob, `qrcode.${format}`), `image/${format}`);
    }
  };

  // Share QR Code
  const shareQRCode = () => {
    const canvas = document.querySelector("canvas");
    const dataUrl = canvas.toDataURL("image/png");  // Getting the QR code image data
    if (navigator.share) {
      navigator
        .share({
          title: "QR Code",
          text: "Scan this QR Code",
          url: dataUrl,  // Sharing the image URL directly (data URL)
        })
        .then(() => console.log("Shared successfully"))
        .catch((err) => console.error("Error sharing", err));
    } else {
      alert("Sharing is not supported on this device.");
    }
  };

  return (
    <div className="qr-generator">
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
          Generate QR Code
        </button>
      </div>

      {qrCode && (
        <div className="qr-display">
          <QRCodeCanvas value={qrCode} size={256} className="qr-animation" />
          <div className="qr-actions">
            {/* Dropdown for Download Options */}
            <div className="dropdown">
              <button
                onClick={() => setShowDropdown(!showDropdown)}
                className="btn-download"
              >
                Download QR Code ▼
              </button>
              {showDropdown && (
                <ul className="dropdown-menu">
                  <li onClick={() => downloadQRCode("png")}>Download as PNG</li>
                  <li onClick={() => downloadQRCode("jpeg")}>Download as JPG</li>
                  <li onClick={() => downloadQRCode("pdf")}>Download as PDF</li>
                </ul>
              )}
            </div>

            {/* Share Button */}
            <button onClick={shareQRCode} className="btn-share">
              Share QR Code
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default QRCodeGenerator;
