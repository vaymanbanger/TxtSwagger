from requests import Response
import pandas as pd
from pandas import json_normalize
import io
from io import StringIO

def convert_json_to_table(data: list) -> str:
    if not data:
        return "Нет данных\n"
    
    #keys = set()
    #for item in data:
       # if isinstance(item,dict):
        #    keys.update(item.keys)
    dataframe = pd.DataFrame(data)
    return dataframe.to_csv(path_or_buf=None, sep='\t', index=False, na_rep='')