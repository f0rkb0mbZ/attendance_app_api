import pyqrcode
import base64
url = "cloud.google.com"

img = pyqrcode.create(url)

imtest = img.png("myqr.png", scale=16)
print(imtest)

with open('myqr.png', 'rb') as qr:
    imgstr = base64.b64encode(qr.read())
    qr.close()
with open('myqr1.png', 'wb') as qr1:
    writable = base64.b64decode(imgstr)
    qr1.write(writable)
    qr1.close()

