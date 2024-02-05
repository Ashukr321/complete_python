import qrcode  

# add more funcntionaly the qr code 
qr = qrcode.QRCode(
  version=1,
  error_correction=qrcode.constants.ERROR_CORRECT_H,
  box_size=10,
  border=1
)

# 
data = "https://youtu.be/zHu2xead8CA?si=0o47A2n1UbFGH5Eg";

qr.add_data(data);
qr.make(fit=True);
img = qr.make_image(fill_color="orange",back_color="white");
img.save("ashu.png");
img.show();