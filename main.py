from src.table_builder import convert_json_to_table
from src.txt_generator import save_table_to_txt
from src.url_utils import form_file_name
from src.json_loader import get_json_from_api

def main():
    url = input("Введите URL вашей API: ")
    json_data = get_json_from_api(url)
    filename = form_file_name(url)
    
    table_text = convert_json_to_table(json_data)
    save_table_to_txt(table_text,filename)
    print(f"Таблица сохранена в {filename}")

    
if __name__ == "__main__":
    main()