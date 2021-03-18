import pyqrcode
import png
from pyqrcode import QRCode
QRstring = "https://emasomo.cuk.ac.ke/my/"#paste your url here
url = pyqrcode.create(QRstring)
url.png('Desktop\\qr.png', scale=8)