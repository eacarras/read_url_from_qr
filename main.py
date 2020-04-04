import argparse

from PIL import Image
from io import BytesIO

from pyzbar.pyzbar import decode
import json

import requests
from datetime import datetime


NAME_JSON_FILE = "example_data_to_sort.json"
DATE_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
KEY_OF_DATE = "created_at"


parser = argparse.ArgumentParser(description='Cli Tool for different utils functions', formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-u',  '--url', action='store', help='URL for download QR code.')
parser.add_argument('-j',  '--json', action='store', help='Json file name.', type=str, default=NAME_JSON_FILE)

args = parser.parse_args()

if args.url:
    response = requests.get(args.url)
    img = Image.open(BytesIO(response.content))
    qr_decoded = decode(img)
    data = str(qr_decoded[0].data)

    print(data)
    exit(0)

def convert_str_to_date_time(list_obj):
    for value in list_obj:
        value.update({KEY_OF_DATE: datetime.strptime(value[KEY_OF_DATE], DATE_TIME_FORMAT)})


with open(args.json) as file:
    json_dump = json.load(file)
    list_of_dates = list(json_dump["data"])
    
    convert_str_to_date_time(list_of_dates)
    sorted_list = sorted(list_of_dates, key=lambda x: x[KEY_OF_DATE])

    print(f"Min value is {sorted_list[0][KEY_OF_DATE]}")
    print(f"Min value is {sorted_list[-1][KEY_OF_DATE]}")
