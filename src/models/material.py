#!./venv/Scripts/python.exe

import pandas as pd
import sys
import os

path = os.path.abspath(os.getcwd())
sys.path.append(path + '\\src')

from tools.reader import Reader
from tools.logs import add_log

class Material:
    def __init__(self, file_name='MV_relatorio'):
        self.__file_name = file_name

        self.__andador = 'ANDADOR'
        self.__cadeira_de_rodas = 'CADEIRA DE RODAS'
        self.__cadeira_de_rodas_obeso = 'CADEIRA DE RODAS P/ OBESO'
        self.__cadeira_de_banho = 'CADEIRA DE BANHO'
        self.__cadeira_de_banho_obeso = 'CADEIRA DE BANHO P/ OBESO'
        self.__muletas = 'MULETAS'
        self.__bota_ortopedica = 'BOTA ORTOPEDICA'
        self.__tipoia = 'TIPOIA'
        self.__tala_de_punho = 'TALA DE PUNHO'
        self.__cama_hospitalar = 'CAMA HOSPITALAR'
        self.__colchao_caixa_de_ovo = 'COLCHAO CAIXA DE OVO'
        self.__colchao_de_agua = 'COLCHAO D AGUA'
        self.__devolucao = ' - DEVOLUCAO'
        self.__all = [
            self.__andador,
            self.__cadeira_de_rodas,
            self.__cadeira_de_rodas_obeso,
            self.__cadeira_de_banho,
            self.__cadeira_de_banho_obeso,
            self.__muletas,
            self.__bota_ortopedica,
            self.__tipoia,
            self.__tala_de_punho,
            self.__cama_hospitalar,
            self.__colchao_caixa_de_ovo,
            self.__colchao_de_agua
        ]

    @property
    def andador(self):
        return self.__andador

    @property
    def cadeira_de_rodas(self):
        return self.__cadeira_de_rodas

    @property
    def cadeira_de_rodas_obeso(self):
        return self.__cadeira_de_rodas_obeso

    @property
    def cadeira_de_banho(self):
        return self.__cadeira_de_banho
    
    @property
    def cadeira_de_banho_obeso(self):
        return self.__cadeira_de_banho_obeso

    @property
    def muletas(self):
        return self.__muletas

    @property
    def bota_ortopedica(self):
        return self.__bota_ortopedica

    @property
    def tipoia(self):
        return self.__tipoia

    @property
    def tala_de_punho(self):
        return self.__tala_de_punho

    @property
    def cama_hospitalar(self):
        return self.__cama_hospitalar

    @property
    def colchao_caixa_de_ovo(self):
        return self.__colchao_caixa_de_ovo

    @property
    def colchao_de_agua(self):
        return self.__colchao_de_agua

    def devolucao(self, material=None):
        return material + self.__devolucao

    def verify(self, material) -> bool:
        if material in self.__all:
            return self.__devolucao in material # true
        return False

    def get_dataframe(self, verify=False, type='pdf'):
        if type == 'pdf':
            _df_aux = Reader().read_pdf(f'{self.__file_name}.pdf')
        elif type == 'xls':
            _df_aux = Reader().read_excel(f'{self.__file_name}.xls')

        df_material = pd.DataFrame(_df_aux)
        for index in range(len(_df_aux)):
            if self.verify(_df_aux.loc[index, "Benefício"]):
                df_material.drop(index, axis=0, inplace=True)

        df_material.reset_index(drop=True, inplace=True)
        add_log('material.py', 'get_dataframe', 'info', 'Devoluções removidas do DataFrame')
        return df_material


if __name__ == '__main__':
    for material in Material():
        print(material)