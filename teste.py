"""def verify_number(phone: str) -> bool:
    string = ''
    for n in phone:
        if n.isnumeric():
            string += n

    if len(string) == 11:
        print(string)
        return True
    
    elif len(string) <= 10:
        if len(string) == 10:
            string = string[0:2] + f'9{string[2:]}'
            print(string)
            return True
        elif len(string) == 9:
            string = '45' + string
            print(string)
            return True
        elif len(string) == 8:
            string = '459' + string
            print(string)
            return True
        else:
            print(string)
            return False
    else:
        print(string)
        return False

print(verify_number('4512345678'))
"""

class Classe:
    def __init__(self, nome) -> None:
        self.nome = nome

    def metodo_principal(self):
        print(f'Método para mostrar nome da instância')
        
        def sub_metodo(self):
            for l in self.nome:
                print(l)

        sub_metodo(self)


# if __name__ == '__main__':
#     c = Classe('Classe')
#     c.metodo_principal()

import tabula as tb
import pandas as pd
import numpy as np

# tabelas = tb.read_pdf(input_path='src\downloads\MV_andador.pdf', pages='all')
tabelas = tb.read_pdf(input_path='src\downloads\MV_master.pdf', pages='all', guess=False, pandas_options={'header': None})
for tabela in tabelas:
    tabela = tabela.drop(columns=[3, 4], axis=1)
    tabela = tabela.drop(tabela.index[[0, 1, 2, -1, -2, -3]], axis=0)
    tabela = tabela.reset_index(drop=True)
    
    while 'Data:' not in tabela.iloc[0, 0]:
        print(tabela.iloc[0, 0])
        tabela = tabela.drop(tabela.index[[0]], axis=0)
        tabela = tabela.reset_index(drop=True)

    print(tabela)
    print('\n\n\n')
# * Ok
# tabela = tabelas[0]
# tabela = tabela.drop(columns=[3, 4], axis=1)
# tabela = tabela.drop(tabela.index[[0, 1, 2, -1, -2, -3]], axis=0)
# tabela = tabela.reset_index(drop=True)

# print(tabela)
# if 'Data:' in tabela.iloc[5, 0]:
#     print('ok')


# print(tabela.iloc[0, 0])
# while 'Data:' not in tabela.iloc[0, 0]:
#     print(tabela.iloc[0, 0])
#     tabela = tabela.drop(tabela.index[[0]], axis=0)
#     tabela = tabela.reset_index(drop=True)
# print(tabela)
