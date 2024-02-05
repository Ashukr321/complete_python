import qrcode
from qrcode import constants
from PIL import Image

# Create a QRCode instance
q = qrcode.QRCode(
    version=1,
    error_correction=constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

data = "Hello, QR Code!"
q.add_data(data);
q.make(fit=True);

img = q.make_image(fill_color="orange", back_color="white");

# Save the image
img.save("qrcode.png")
img.show();

