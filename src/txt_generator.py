import os

def save_table_to_txt(table_text: str, filename: str) -> None:
    """_summary_
    Сохранить таблицу как текстовый файл
    
    Args:
        table_text (str): Данные в таблице
        filename (str): Имя файла
    """
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, filename)
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(table_text)