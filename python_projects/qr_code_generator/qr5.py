import qrcode as qr

data = qr.QRCode(
  version=1,error_correction=qr.ERROR_CORRECT_H,
  border=1,
  box_size= 12
);

# data 
data.add_data("https://youtu.be/l9oeYIJVycA?si=1d-ZQ048BKzEGZDU");
data.make(fit=True);
img  = data.make_image(fill_color= "red",black_color="white");
img.save("red.png");

img.show();
