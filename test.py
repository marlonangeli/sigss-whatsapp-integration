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
print(dataframe)
"""
dataframe['WhatsApp Phones'] = 1
print(dataframe)
for index in range(len(dataframe)):
    range_phones = dataframe.loc[index, 'Phones'][1:-1].split(' ')
    range_phones = [x[1:-1] for x in range_phones if x != 'False']

    phones = [phone for phone in range_phones if randint(0, 2) != 0]
    # print(index, pd.Series(phones).values, dataframe.loc[index, 'Phones'])
    if phones:
        print(index, phones, dataframe.loc[index, 'Phones'], end=' ')
        print(dataframe.loc[index, 'WhatsApp Phones'])
        dataframe.loc[index, 'WhatsApp Phones'] = f'{pd.Series(phones).values}'
        print(dataframe.loc[index, 'WhatsApp Phones'])
    else:
        dataframe.loc[index, 'WhatsApp Phones'] = pd.Series([False]).values
    # print(index, phones)

print(dataframe)"""