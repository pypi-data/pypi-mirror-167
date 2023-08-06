import os

def install():
    os.system('pip install instabase==0.0.1')

install()

from instabase import SDK

app_name, app_version = 'US Bank Statements', '3.0.0'
file_url = 'https://apps.instabase.com/static/assets/images/cloud-developers/us-bs/sample-us-bs-1.jpeg'

sdk = SDK()
resp = sdk.extract_from_input_url(file_url, app_name, app_version)
print(resp)
