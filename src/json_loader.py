import requests

def get_json_from_api(url: str):
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status
        return response.json()
    except requests.exceptions.RequestException as exc:
        raise SystemExit(exc)
    