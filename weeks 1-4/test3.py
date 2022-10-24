# my_list = ['Real', ' Python']
# x=my_list

# func = lambda x: ''.join(i for i in x)
# print(func(my_list))

import qrcode

qr = qrcode.QRCode(
  version=1,
  error_correction=qrcode.constants.ERROR_CORRECT_L,
  box_size=10,
  border=4,
)
qr.add_data("https://www.youtube.com/channel/UCDiSrTPJ4xaw8BP3nQj7c4Q")

img = qr.make_image(fill_color="black", back_color="white")

print(type(img.save("qrcode.jpg")))