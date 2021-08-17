import tabula as tb
import pandas as pd
import numpy as np
import os
import sys

path = os.path.abspath(os.getcwd())
sys.path.append(path + '\\src')


class Reader:
    def __init__(self):
        self.__download_path = path + '\\src\\downloads\\'
        self.__docs_path = path + '\\docs\\'


    def read_pdf(self, file_name):
        tables = tb.read_pdf(self.__download_path + file_name, pages="all", guess=False, pandas_options={'header': None})
        df_table_formatted = pd.DataFrame(columns=[
            'Data',
            'Usuário de Serviço',
            'Telefone',
            'Endereço',
            'Benefício',
            'Observação',
            'Qtd'
        ])
        index = 0
        for df_table in tables:
            df_table = df_table.drop(columns=[3, 4], axis=1)
            df_table = df_table.drop(df_table.index[[0, 1, 2, -1, -2, -3]], axis=0)
            df_table = df_table.reset_index(drop=True)
            while 'Data:' not in df_table.loc[0, 0]:
                df_table = df_table.drop(df_table.index[[0]], axis=0)
                df_table = df_table.reset_index(drop=True)

            for i in range(len(df_table)):            
                if 'Data:' in df_table.iloc[i, 0]:
                    index += 1
                    df_table_formatted.loc[index, "Data"] = df_table.iloc[i, 0][6:]
                    df_table_formatted.loc[index, "Usuário de Serviço"] = df_table.iloc[i, 1][9:]
                elif 'Fone:' in df_table.iloc[i, 0]:
                    df_table_formatted.loc[index, "Telefone"] = df_table.iloc[i, 0][6:]
                    df_table_formatted.loc[index, "Endereço"] = df_table.iloc[i, 1][10:]
                    df_table_formatted.loc[index, "Qtd"] = df_table.iloc[i, 2]
                elif "NIS:" in df_table.iloc[i, 0]:
                    df_table_formatted.loc[index, "Benefício"] = df_table.iloc[i, 1][11:]
                
                elif 'Obs:' in df_table.iloc[i, 0]:
                    df_table_formatted.loc[index, "Observação"] = f'{df_table.iloc[i, 0][5:]}'
                
                else:
                    df_table_formatted.loc[index, "Observação"] = ''.join(df_table.iloc[i, 0])

        return df_table_formatted


    def read_excel(self, file_name):
        df_table = pd.read_excel(self.__download_path + file_name)
        df_table = df_table.drop(columns=['Unnamed: 0', 'Unidade', 'Valor Total'])
        df_table = df_table.drop(df_table.index[[-1]], axis=0)
        df_table.dropna(axis=0, how='all', inplace=True)
        df_table = df_table.reset_index(drop=True)

        return df_table

if __name__ == '__main__':
    reader = Reader()
    pdf_table = reader.read_pdf('MV_master.pdf')
    for i in range(len(pdf_table)):
        print(f'{pdf_table.iloc[i, 0]} - {pdf_table.iloc[i, 1]} - {pdf_table.iloc[i, 2]} -  - {pdf_table.iloc[i, 4]} - {pdf_table.iloc[i, 5]}')
    print('\n\n' + '-'*80 + '\n\n')
    # print(reader.read_excel('MV_master.xls'))
