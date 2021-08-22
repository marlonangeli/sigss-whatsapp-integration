#!./venv/Scripts/python.exe

import sys
import os
import pandas as pd

path = os.path.abspath(os.getcwd())
sys.path.append(path + '\\src')

from whatsapp import WhatsApp
from services.sigss_mv import Sigss, MV
from tools.logs import add_log
from tools.reader import Reader

class Paciente:
    def __init__(self):
        self.sigss = Sigss()


    def get_dataframe(self, nome, data_emprestimo):
        self.nome = nome
        self.data_emprestimo = data_emprestimo
        _data = self.__get_data()

        # todo - ajustar numeros de telefone com uma funcao
        telefone = [
            _data['ddd1'] + _data['telefone1'],
            _data['ddd2'] + _data['telefone2'],
            _data['ddd3'] + _data['telefone3'],
        ]
        endereco = f"{_data['logradouro']} - {_data['bairro']} - {_data['numero']}"
        return pd.DataFrame([{
            'Cod': _data['codigo'],
            'Name': _data['nome'],
            'Phone': pd.Series(telefone).values,
            'Address': endereco,
            'Birthday': _data['data_nascimento'],
            'Mother': _data['nome_mae'],
            'Father': _data['nome_pai'],
            'Spouse': _data['nome_conjuge']
        }])


    def verify_phone(self, phone=None):
        pass

    def __get_data(self):
        # todo - ajustar para pegar dados do arquivo de configuracao
        
        self.sigss.search_patient({'nome': self.nome, 'data': self.data_emprestimo})
        return self.sigss.get_values()


if __name__ == '__main__':
    print('run module')
