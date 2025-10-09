from urllib.parse import urlparse
import urllib3
import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
def form_file_name(url: str) -> str:
    parsed_name = urlparse(url)
    resource_name = parsed_name.path.replace("/","_")
    date = datetime.date.today().isoformat()
    return f"{resource_name}_{date}.txt"