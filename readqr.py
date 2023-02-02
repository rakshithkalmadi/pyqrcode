# create qr code
import qrcode
img=qrcode.make("https://www.towardtechno.com")
img.save("qr.png")
print("QR code created")

# Path: readqr.py
import cv2
detect=cv2.QRCodeDetector()
val,_,_=detect.detectAndDecode(cv2.imread("qr.png"))
print(val)
print("QR code read")
