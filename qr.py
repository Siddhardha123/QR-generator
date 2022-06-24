import pyqrcode
from pyqrcode import QRCode
s = "www.youtube.com"
url = pyqrcode.create(s)
url.png('myqr.png')
