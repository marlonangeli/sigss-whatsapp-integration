import sys
import os

path = os.path.abspath(os.getcwd())
sys.path.append(path + '\\src')

from src.models.paciente import Paciente
from src.models.material import Material
from src.tools.reader import Reader
from src.tools.logs import add_log
from src.services.sigss_mv import Sigss, MV
import pandas as pd
import numpy as np

class Emprestimo:
    def __init__(self, remove_material=True, file_name='MV_relatorio'):
        __mv = MV()
        __mv.get_request()
        __mv.close()
        self.__reader = Reader()
        # self._df_excel = self.__reader.read_excel('MV_relatorio.xls')
        if remove_material:
            self._df_aux = Material().get_dataframe(verify=True, type='pdf')
        else:    
            self._df_aux = self.__reader.read_pdf(f'{self._file_name}.pdf')

        self.__whatsapp_is_open = False


    def get_dataframe(self):
        self.__paciente = Paciente()
        df_paciente = pd.DataFrame()
        for index in range(len(self._df_aux)):
            df = self.__paciente.get_dataframe(
                self._df_aux.loc[index, 'Usuário de Serviço'],
                self._df_aux.loc[index, 'Data'],
            )
            df_paciente = df_paciente.append(df, ignore_index=True)
            with open(path + '/src/tmp/tmp.txt', 'w') as aux:
                aux.write(f"{index};{len(self._df_aux)}")

        self.__paciente.sigss.close()
        df_paciente.insert(8, 'Benefit', self._df_aux['Benefício'])    
        df_paciente.insert(9, 'Qtd', self._df_aux['Qtd'])    
        df_paciente.reset_index(drop=True, inplace=True)
        
        return df_paciente


    def save_dataframe(self, dataframe=None):
        df = self.get_dataframe() if dataframe is None else dataframe
        df.to_excel(path + '/docs/relatorio.xlsx', index=False)

        
    def _dataframe_exists(self):
        return os.path.exists(path + '/docs/relatorio.xlsx')


if __name__ == '__main__':
    emprestimo = Emprestimo(remove_material=True)
    df = emprestimo.get_dataframe()
    print(df)
    emprestimo.save_dataframe(df)
    add_log('emprestimo', '__main__', 'DEBUG', f'DataFrame:\n{df}')
