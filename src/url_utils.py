from urllib.parse import urlparse
import urllib3
import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
def form_file_name(url: str) -> str:
    """_summary_
    Сформировать имя файла на основе URL и текущей даты.

    Args:
        url (str): URL, из которого извлекается имя ресурса.

    Returns:
        str: Строка с именем файла
    """
    parsed_name = urlparse(url)
    
    path = parsed_name.path.lstrip("/")
    resource_name = path.replace("/","_")
    date = datetime.date.today().isoformat()
    
    return f"{resource_name}_{date}.txt"