import json
import uuid

import pandas as pd

XLSX_NAME = '../HTC_EN_Component name_v1_31082020.xlsx'
JSON_NAME = 'default_components.json'

xlsx = pd.read_excel(XLSX_NAME, None)

data = []

for sheet_name in xlsx.keys():
    df = pd.DataFrame(xlsx[sheet_name])

    df = df[3:]
    old_component = ""
    for index, rows in df.iterrows():
        component = rows[0]
        if str(rows[0]) == "nan":
            component = old_component
        row = {
            "id": str(uuid.uuid1()),
            "component": component,
            "dms_name": rows[1],
            "component_name": rows[2],
            "title": rows[3] if str(rows[3]) != 'nan' else None
        }
        if str(rows[0]) != "nan":
            old_component = rows[0]
        data.append(row)

with open(JSON_NAME, 'w', encoding="UTF-8") as file:
    json.dump(data, file, indent=4)
