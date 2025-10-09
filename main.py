from src.url_utils import form_file_name
from src.json_loader import get_json_from_api

def main():
    url = input("Введите URL вашей API: ")
    json_data = get_json_from_api(url)
    file_name = form_file_name(url)
    print(file_name)
    print(json_data)
    
if __name__ == "__main__":
    main()