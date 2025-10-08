import requests
from urllib.parse import urlparse
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def extract_name_from_url(url: str):
    split = urlparse(url)
    return split.path

#response = requests.get(url, verify=False)
#response.json()
#print(response)