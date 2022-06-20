
import pyqrcode
import png
from pyqrcode import QRCode
s = input("enter the link:-  ")
url = pyqrcode.create(s)
url.png('myqr.png', scale=6)
