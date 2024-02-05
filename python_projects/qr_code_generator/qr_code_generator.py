import qrcode as qr

# Create a QR code instance with the YouTube link
qr_img = qr.make("this is ajeet singh")

# Save the QR code as an image file
qr_img.save("ajeet.png")
