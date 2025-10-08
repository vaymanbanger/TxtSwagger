import requests
import urllib.parse

url = input("Введите URL вашей API: ")
response = requests.get(url, verify=False)
response.json()
print(response)