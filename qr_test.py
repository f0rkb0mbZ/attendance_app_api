import qrcode
import base64
import os

img = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

img.add_data('Hello, World!')
img.make(fit=True)

qrimg = img.make_image()

qrimg.save(os.getcwd()+'/qrcode.bmp')

# encodedimage = base64.b64encode(qrimg)
# print(encodedimage)
qrimg.show()