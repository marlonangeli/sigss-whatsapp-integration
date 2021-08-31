import pandas as pd
import numpy as np
from random import randint

dataframe = pd.read_excel('./docs/relatorio.xlsx')
dataframe.drop(
    [
        'Cod',
        'Date',
        'Date Devolution',
        'Benefit',
        'Qtd',
        'Message',
        'Date Message Send',
        'Address',
        'Birthday',
        'Mother',
        'Father',
        'Spouse'
    ],
    axis=1,
    inplace=True
)
def get_phone_from_string(string: str):
    range_phones = string[1:-1].split(' ')
    return [x[1:-1] for x in range_phones]

df_check = dataframe.isnull()
for index in range(len(dataframe)):
    if not df_check.loc[index, 'WhatsApp Phones']:
        phones = get_phone_from_string(dataframe.loc[index, 'WhatsApp Phones'])
        print(phones)
