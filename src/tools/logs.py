
# TODO - Registro de logs
# TODO - Manipulacao do registro
# TODO - Leitura dos relatorios do SIGSS
# TODO - limpeza dos dados
# TODO - adicionar ao registro

from datetime import datetime
import os, sys

def reset_logs():
    arq = open('src\\logs\\logs.txt', 'w')
    arq.write(f'{str(datetime.now().replace(microsecond=0))} - Novo arquivo de log\n\n{"-"*80}\n\n')
    arq.close()


def add_log(module_file, function, log_type, log_text):
    with open('.\\src\\logs\\logs.txt', 'a+') as arq:
        arq.write(f'{str(datetime.now().replace(microsecond=0))} - [{str(module_file)}]>[{str(function)}] {str(log_type).upper()}: {str(log_text)}\n')
        arq.close()


if __name__ == '__main__':
    reset_logs()
    add_log('teste', 'teste', 'teste', 'teste')
