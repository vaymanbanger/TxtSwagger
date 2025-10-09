def save_table_to_txt(table_text: str, filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(table_text)