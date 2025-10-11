
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
    
    rows = [list(json_keys)]
    for item in data:
        row = [format_value(item.get(key)) for key in json_keys]
        rows.append(row)
    
    column_width = []
    for index in range(len(json_keys)):
        max_width = max(len(row[index]) for row in rows)
        column_width.append(max_width)
    
    def format_row(row):
        return "| " + " | ".join(f"{value:<{column_width[idx]}}"
                                 for idx, value in enumerate(row)) + " |"
    
    separator = "|".join("-" * width for width in column_width) + "|"

    result = [separator, format_row(rows[0]), separator]
    for row in rows[1:]:
        result.append(format_row(row))
    result.append(separator)
    
    return "\n".join(result)