from PIL import Image

from pyzbar.pyzbar import decode

import requests
from io import BytesIO


url = ""

response = requests.get(url)
img = Image.open(BytesIO(response.content))
qr_decoded = decode(img)
data = str(qr_decoded[0].data).strip("'")[2:]

print(data)
