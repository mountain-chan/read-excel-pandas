import json

import pandas as pd

XLSX_NAME = '../HTC_EN_Locking list (Chapter 7)_v1_28042020.xlsx'
JSON_NAME = 'output_data2.json'

xlsx = pd.read_excel(XLSX_NAME, None)

data = []

df = pd.DataFrame(xlsx["Sheet1"])

for i in range(0, 25):
    list_disable = []
    for j in range(1, 26):
        if df.loc[i][j] == "x":
            list_disable.append(df.columns[j])
    function = {
        df.loc[i][0]: list_disable
    }
    data.append(function)

with open(JSON_NAME, 'w') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

