from urllib.parse import urlparse
import urllib3
import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
def form_file_name(url: str) -> str:
    resource_name = urlparse(url)
    date = datetime.date.today().isoformat()
    return f"{resource_name.path}_{date}.txt"