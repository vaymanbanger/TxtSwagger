from requests import Response
import pandas as pd
from pandas import json_normalize


def convert_json_to_table(data: list) -> str:
    if not data:
        return "Нет данных\n"
    
    #keys = set()
    #for item in data:
       # if isinstance(item,dict):
        #    keys.update(item.keys)
    table = pd.DataFrame(data)
    return table.to_csv('\t', False,'')