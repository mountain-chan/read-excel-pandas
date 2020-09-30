import json
from datetime import datetime
import pandas as pd

XLSX_NAME = '../HTC_Event-Fault-Screen_2020_07_25.xlsx'
JSON_NAME = 'mock_data_batch.json'

xlsx = pd.read_excel(XLSX_NAME, None)

data = []

df = pd.DataFrame(xlsx["Batch history_Batch"])

for i in range(2, 8):
    date_time = df.loc[i][0]
    tt = date_time.timestamp()
    row = {
        df.loc[0][0]: tt,
        df.loc[0][1]: df.loc[i][1],
        df.loc[0][2]: df.loc[i][2],
        df.loc[0][3]: df.loc[i][3],
        df.loc[0][4]: df.loc[i][4],
        df.loc[0][5]: df.loc[i][5]
    }
    data.append(row)

for i in range(12, 18):
    date_time = df.loc[i][0]
    tt = date_time.timestamp()
    row = {
        df.loc[0][0]: tt,
        df.loc[0][1]: df.loc[i][1],
        df.loc[0][2]: df.loc[i][2],
        df.loc[0][3]: df.loc[i][3],
        df.loc[0][4]: df.loc[i][4],
        df.loc[0][5]: df.loc[i][5]
    }
    data.append(row)


with open(JSON_NAME, 'w') as file:
    json.dump(data, file, indent=4)

