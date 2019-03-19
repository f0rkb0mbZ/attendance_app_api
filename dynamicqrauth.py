import hmac
import hashlib
import time
from datetime import datetime
import pyqrcode
import json
import base64

def tokengen(baseurl):
    isotimestamp = datetime.now().isoformat()
    bytemsg = str.encode(baseurl)
    bytekey = str.encode(isotimestamp)
    digest_maker = hmac.new(bytekey, bytemsg, hashlib.sha256)
    authtoken = digest_maker.hexdigest()
    data = {}
    data['token'] = authtoken
    with open('auth.json', 'w') as authfile:
        json.dump(data, authfile)
        authfile.close()
    return authtoken

def createbase64QR(baseurl, authtoken):
    url = baseurl +'/' + authtoken + '/'
    img = pyqrcode.create(url)
    img.png('authQR.png', scale=8)
    with open('authQR.png', 'rb') as qr:
        encodedqr = base64.b64encode(qr.read())
        qr.close()
    strqr = str(encodedqr)
    return strqr[1:].strip("'")