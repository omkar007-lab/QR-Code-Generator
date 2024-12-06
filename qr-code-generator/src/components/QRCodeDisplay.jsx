import React from "react";
import QRCode from "qrcode.react";

const QRCodeDisplay = ({ qrCode, downloadQRCode, shareQRCode }) => {
  return (
    <div className="qr-display">
      <QRCode value={qrCode} size={256} />
      <div className="qr-actions">
        <button onClick={() => downloadQRCode("png")} className="btn-download">
          Download as PNG
        </button>
        <button onClick={() => downloadQRCode("jpeg")} className="btn-download">
          Download as JPG
        </button>
        <button onClick={shareQRCode} className="btn-share">
          Share QR Code
        </button>
      </div>
    </div>
  );
};

export default QRCodeDisplay;
