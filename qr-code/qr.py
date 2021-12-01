import pyqrcode
from pyqrcode import QRCode

url = '' # insert url here

qr = pyqrcode.create(url)

qr.svg('url.svg', scale=8)
