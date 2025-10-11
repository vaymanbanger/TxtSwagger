import requests

def get_json_from_api(url: str):
    """_summary_
    Получить JSON-данные по указанному URL через HTTP GET запрос.
    
    Args:
        url (str): Адрес API, откуда нужно получить JSON.

    Raises:
        SystemExit: Адрес API, откуда нужно получить JSON.

    Returns:
        dict: Распарсенный JSON-ответ от API.
    """
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status
        return response.json()
    except requests.exceptions.RequestException as exc:
        raise SystemExit(exc)
    