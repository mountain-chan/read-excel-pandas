import json

import pandas as pd

XLSX_NAME = '../HTC_Document_Logging_2020_07_15.xlsx'
JSON_NAME = 'output_component.json'

xlsx = pd.read_excel(XLSX_NAME, None)

data = []

for sheet_name in xlsx.keys():
    df = pd.DataFrame(xlsx[sheet_name])

    if df.loc[0][1] == 'Component':
        df = df[1:]
        components = []
        data_row = []
        component = None
        old_name = ''
        for index, rows in df.iterrows():
            row = {
                "DMS Name": rows[2],
                "Title": rows[7],
                "Content": rows[8]
            }

            current_component = rows[1]
            if type(current_component) is str:
                if component:
                    if len(component['data']) > 0:
                        components.append(component)
                else:
                    old_name = current_component
                component = {
                    'name': old_name,
                    'data': data_row
                }
                old_name = current_component
                data_row = []

            data_row.append(row)

        sheet = {
            'sheet_name': sheet_name,
            'components': components
        }
        data.append(sheet)

with open(JSON_NAME, 'w') as file:
    json.dump(data, file, indent=4)

'''========================='''
JSON_NAME = 'output_group.json'
data = []
for sheet_name in xlsx.keys():
    df = pd.DataFrame(xlsx[sheet_name])

    if df.loc[0][1] == 'Group':
        df = df[1:]
        components = []
        data_row = []
        component = None
        old_name = ''
        for index, rows in df.iterrows():
            row = {
                "DMS Name": rows[2],
                "Title": rows[5],
                "Content": rows[6]
            }

            current_component = rows[1]
            if type(current_component) is str:
                if component:
                    if len(component['data']) > 0:
                        components.append(component)
                else:
                    old_name = current_component
                component = {
                    'name': old_name,
                    'data': data_row
                }
                old_name = current_component
                data_row = []

            data_row.append(row)

        sheet = {
            'sheet_name': sheet_name,
            'components': components
        }
        data.append(sheet)

with open(JSON_NAME, 'w') as file:
    json.dump(data, file, indent=4)
