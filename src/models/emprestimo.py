from src.services.os_path_core import *
from src.services.functions_core import *
from src.services.models_core import *
from src.services.pandas_core import *
from src.services.sigss_mv import *

MESSAGE = """Olá, esta é uma _mensagem automática_ de um sistema do *NASF Itaipulândia*.
Informamos que o/a paciente *{0}* tem como registro, um empréstimo de *{1}* em nosso sistema.

Solicitamos que CASO O PACIENTE NÃO ESTEJA UTILIZANDO ESTE MATERIAL, para que seja devolvido ao Posto de Saúde.
Temos poucos materiais em estoque, estando em constante falta, seja consciente e colabore com a saúde do município.


Caso já tenha devolvido o material, entre em contato para que seja retirado do nosso sistema.

_Contatos:_
E-mail: nasfitaipulandiapr@gmail.com
Coordenadora do NASF: Camila Fernanda de Souza - (45) 99143-2728 / (45) 3559-1731"""

class Emprestimo:
    def __init__(self, remove_material=True, file_name='MV_relatorio'):
        with open(path + '/src/tmp/tmp.txt', 'w') as aux:
            aux.write("0;15")
        __mv = MV()
        __mv.get_request()
        __mv.close()
        self.__reader = Reader()
        # self._df_excel = self.__reader.read_excel('MV_relatorio.xls')
        if remove_material:
            self._df_aux = Material().get_dataframe(verify=True, type='pdf')
        else:    
            self._df_aux = self.__reader.read_pdf(f'{self._file_name}.pdf')
        self.finished = False
        self.__whatsapp_is_open = False


    def get_dataframe(self):
        self.__paciente = Paciente()
        self.df_paciente = pd.DataFrame()
        for index in range(len(self._df_aux)):
            df = self.__paciente.get_dataframe(
                self._df_aux.loc[index, 'Usuário de Serviço'],
                self._df_aux.loc[index, 'Data'],
            )
            self.df_paciente = self.df_paciente.append(df, ignore_index=True)
            with open(path + '/src/tmp/tmp.txt', 'w') as aux:
                aux.write(f"{index};{len(self._df_aux)}")

        self.__paciente.sigss.close()
        self.df_paciente.insert(3, "Date", self._df_aux['Data'])
        self.df_paciente.insert(4, "Date Devolution", self._generate_date_devolution())
        self.df_paciente.insert(5, 'Benefit', self._df_aux['Benefício'])    
        self.df_paciente.insert(6, 'Qtd', self._df_aux['Qtd'])
        self.df_paciente.insert(7, "WhatsApp Phones", None)
        self.df_paciente.insert(8, "Message", self._get_message())
        self.df_paciente.insert(9, "Date Message Send", None)
        self.df_paciente.reset_index(drop=True, inplace=True)
        add_log("emprestimo.py", "get_dataframe", "info", f"Dados do DataFrame atualizados.")
        self.finished = True
        return self.df_paciente


    def save_dataframe(self, dataframe=None):
        df = self.df_paciente if dataframe is None else dataframe
        df.to_excel(path + '/docs/relatorio.xlsx', index=False)
        add_log("emprestimo.py", "save_dataframe", "info", f"Dados do DataFrame salvo em: {path + '/docs/relatorio.xlsx'}")

    def _generate_date_devolution(self):
        return [
            (datetime.strptime(self.df_paciente.loc[index, "Date"], "%d/%m/%Y")
            + timedelta(days=60)).strftime("%d/%m/%Y")
            for index in range(len(self.df_paciente))
        ]

    def _get_message(self):
        return [
            MESSAGE.format(
                self.df_paciente.loc[index, 'Name'],
                self.df_paciente.loc[index, 'Benefit']
            ) for index in range(len(self.df_paciente))
        ]


if __name__ == '__main__':
    emprestimo = Emprestimo(remove_material=True)
    df = emprestimo.get_dataframe()
    print(df)
    emprestimo.save_dataframe(df)
    add_log('emprestimo', '__main__', 'DEBUG', f'DataFrame:\n{df}')
