#!./venv/Scripts/python.exe

import sys
import os
import pandas as pd

path = os.path.abspath(os.getcwd())
sys.path.append(path + '\\src')

# from whatsapp import WhatsApp
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
        phone_numbers = [
            _data['ddd1'] + _data['telefone1'],
            _data['ddd2'] + _data['telefone2'],
            _data['ddd3'] + _data['telefone3'],
        ]

        telefone = [self.__validate_phone(phone) for phone in phone_numbers]
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


    def __validate_phone(self, phone: str):
        tam = len(phone)
        if tam == 10:
            return phone
        elif tam == 11:
            return phone[:2] + phone[3:]
        elif tam == 9:
            return "45" + phone[1:]
        elif tam == 8:
            return "45" + phone
        return False


    def __get_data(self):
        self.sigss.search_patient({'nome': self.nome, 'data': self.data_emprestimo})
        return self.sigss.get_values()
