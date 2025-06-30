from __future__ import print_function
import time
import cloudmersive_barcode_api_client
from cloudmersive_barcode_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_barcode_api_client.Configuration()
configuration.api_key['Apikey'] = '9fa74e71-bc0c-40df-9593-ef8d9c661d68'

# create an instance of the API class
api_instance = cloudmersive_barcode_api_client.BarcodeScanApi(cloudmersive_barcode_api_client.ApiClient(configuration))
image_file = r'C:\Users\shlom\AppData\Roaming\JetBrains\PyCharmCE2022.2\scratches\clcoding_barcode.png'  # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.
image_2 = r"C:\Users\shlom\OneDrive\תמונות\סרט צילום\WIN_20250630_08_47_54_Pro.jpg"
try:
    # Scan and recognize an image of a barcode
    api_response = api_instance.barcode_scan_image(image_2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BarcodeScanApi->barcode_scan_image: %s\n" % e)
