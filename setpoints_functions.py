import json
import uuid

import pandas as pd

XLSX_NAME = '../HTC_Recipe_v1_27082020.xlsx'
JSON_NAME = 'setpoints_function.json'

xlsx = pd.read_excel(XLSX_NAME, None)

data = []

df = pd.DataFrame(xlsx["Steps_Parameters"])
df = df[3:]

parameters = []
old_function = ""

for index, rows in df.iterrows():

    if str(rows[1]) != "nan" or index == 96:
        row = {
            "function": old_function,
            "function_id": old_function.split(" ")[0],
            "parameters": parameters
        }
        data.append(row)
        parameters = []

    parameter = {
        "name": rows[2].strip().lower().replace(" ", "_").replace("-", "_") if str(rows[2]) != "nan" else None,
        "range": rows[4] if str(rows[4]) != "nan" else None
    }
    parameters.append(parameter)

    if str(rows[1]) != "nan":
        old_function = rows[1]

with open(JSON_NAME, 'w', encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)


# print("aA a b c-STD".strip().lower().replace(" ", "_").replace("-", "_"))
