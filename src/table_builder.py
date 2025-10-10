
def convert_json_to_table(data: list[dict]) -> str:
    """_summary_
    Конвертирует JSON в текст

    Args:
        data (list[dict]): Список словарей в JSON

    Returns:
        str: таблица с данными
    """
    if not data:
        return "Нет данных\n"
    
    json_keys = set()
    for item in data:
        if isinstance(item, dict):
            json_keys.update(item.keys())
    
    json_keys = sorted(json_keys, key=len)
            
    def format_value(value):
        if isinstance(value,(str, int, bool, float)):
            return str(value)
        return type(value).__name__
    
    title = ["\t".join(json_keys)]
    for item in data:
        row = [format_value(item.get(key)) for key in json_keys]
        title.append("\t".join(row))
    
    return "\n".join(title)