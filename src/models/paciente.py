#!./venv/Scripts/python.exe

import sys
import os

path = os.path.abspath(os.getcwd())
sys.path.append(path + '\\src')

from whatsapp import WhatsApp
from tools.logs import add_log

class Paciente:
    def __init__(self, numero):
        self.numero = numero
        pass



if __name__ == '__main__':
    pass