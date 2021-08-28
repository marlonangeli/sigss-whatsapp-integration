#!./venv/Scripts/python.exe

import sys
import os

path = os.path.abspath(os.getcwd())
sys.path.append(path + '\\src')

from json.decoder import JSONDecoder
from time import sleep
from urllib import request

from services.selenium_core import *

from tools.logs import add_log


class Sistema:
    FORNECEDOR = 'NASF'
    __credentials = JSONDecoder().decode(open(r"src/config/credentials.json").read())
    def __init__(self):
        self.__username = self.__credentials["username"]
        self.__password = self.__credentials["password"]
        self.__login = False
        self.sistema = self.__class__.__name__.upper()
        options = Options()
        # options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1280x720")
        options.add_argument("--no-sandbox")
        options.add_experimental_option("prefs", {
            "download.default_directory": path + '\\src\\downloads',
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        self._driver = webdriver.Chrome(executable_path=WEBDRIVER_PATH, options=options)
        self._wdw = WebDriverWait(self._driver, 10)

        if self.sistema == 'SIGSS':
            self.__url = "http://c3100prd.cloudmv.com.br/sigss/login"
        elif self.sistema == 'MV':
            self.__url = "http://c3100prd.cloudmv.com.br/login"
        else:
            raise Exception('Sistema inválido')


    def login(self) -> bool:
        if not self.__login:
            # acessa a pagina de login
            self._driver.get(self.__url)
            
            # seleciona o sistema e aguarda o carregamento
            if self.sistema == 'MV':
                self._wdw.until(
                    EC.presence_of_element_located((By.NAME, "usuario"))
                ).send_keys(self.__username)
                self._driver.find_element_by_name("senha").send_keys(self.__password)
                self._driver.find_element_by_id("btnEntrar").click()
            
            if self.sistema == 'SIGSS':
                self._wdw.until(
                    EC.presence_of_element_located((By.ID, "login.login"))
                ).send_keys(self.__username)
                self._driver.find_element_by_id("login.senha").send_keys(self.__password)
                self._driver.find_element_by_id("entrar").click()
                
            # adiciona evento no log
            add_log(
                'sigss_mv.py',
                "Sistema.login",
                "INFO",
                f'Login no sistema {self.sistema} efetuado com sucesso: {self.__username}'
            )
            self.__login = True
        
        return self.__login

    def fill_date_form(self, locator, date):
            d = self._driver.find_element(*locator)
            d.send_keys(Keys.CONTROL, 'a')
            d.send_keys(date)

    def _logout(self) -> bool:
        if self.__login:
            # seleciona o sistema e clica no botao de sair
            if self.sistema == 'MV':
                self._driver.find_element_by_id("sair").click()
                button = self._wdw.until(EC.presence_of_element_located((By.NAME, "sim")))
                button.click()

            if self.sistema == 'SIGSS':
                self._driver.find_element_by_xpath("/html/body/header/div[3]/i[2]").click()
                self._driver.switch_to.active_element.send_keys(Keys.ENTER)

            # adiciona evento no log
            add_log(
                'sigss_mv.py',
                "Sistema._logout",
                "INFO",
                f'Logout no sistema {self.sistema} efetuado com sucesso: {self.__username}'
            )
            self.__login = False
            return True

        else:
            # !ERRO: nao é possível sair se não estiver logado
            add_log(
                'sigss_mv.py',
                "Sistema._logout",
                "ERRO",
                f'Ocorreu algum erro no sistema {self.sistema}: {self.__username}'
            )
            return False

    def close(self):
        # if self.__login:
        #     self._logout()
        self._driver.close()
        self._driver.quit()


class Sigss(Sistema):
    def __init__(self):
        super().__init__()
        self.__URL_CADASTRO = 'http://c3100prd.cloudmv.com.br/sigss/controleBeneficios.jsp'
        # self.__URL_CADASTRO = 'http://c3100prd.cloudmv.com.br/sigss/cadastroPaciente.jsp'
        self.data = {}
        self.FIELDS = {
            'nome': 'enti.entiNome',
            'codigo': 'isen.isenCod',
            'ddd1': 'enti.entiTel1Pre',
            'telefone1': 'enti.entiTel1',
            'ddd2': 'enti.entiTel2Pre',
            'telefone2': 'enti.entiTel2',
            'ddd3': 'enti.entiTelCelularPre',
            'telefone3': 'enti.entiTelCelular',
            'data_nascimento': 'entf.entfDtNasc',
            'nome_mae': 'entf.entfNomeMae',
            'nome_pai': 'entf.entfNomePai',
            'nome_conjuge': 'entf.entfNomeConjugue',
            # 'bairro': '//*[@id="enti.localidade.locaPK"]/option[2]',
            'bairro': '//*[@id="enti_localidade_locaPK_chzn"]/a/span',
            # 'logradouro': '//*[@id="enti.logradouro.logrPK"]/option[2]',
            'logradouro': '//*[@id="enti_logradouro_logrPK_chzn"]/a/span',
            'numero': 'enti.entiEndeNumero'
        }

        
    def search_patient(self, filter: dict):
        if not self.login():
            return False

        self._driver.get(self.__URL_CADASTRO)
        self._driver.find_element(By.ID, 'searchString').send_keys(filter['nome'])
        # self._driver.find_element(By.ID, 'searchStringBuscaUsuServico').send_keys(filter['nome'])
        
        def select_filter(self):
            # self._driver.find_element(By.ID, 'searchFieldBusca_chzn').click()
            self.fill_date_form((By.ID, 'dataInicial'), filter['data'])
            self.fill_date_form((By.ID, 'dataFinal'), filter['data'])
            sleep(2)
            # self._driver.find_element(By.ID, 'searchFieldBusca_chzn_o_1').click()
            # self._driver.find_element(By.ID, 'searchStringBusca').send_keys(filter['codigo'])
            # self._wdw.until(EC.element_to_be_clickable((By.ID, 'btnBusca')))
            self._driver.find_element(By.ID, 'btnBuscar').click()
            sleep(5)
            # !not working
            # self._wdw.until(EC.element_located_to_be_selected((
            #     By.XPATH,
            #     '/html/body/div[5]/div[2]/main/div[2]/div[1]/form/div[4]/div/div[3]/div[3]/div/table/tbody/tr[2]/td[12]'
            # )))
            
            # * works
            # self._driver.find_element(
            #     By.XPATH,
            #     '/html/body/div[5]/div[2]/main/div[2]/div[1]/form/div[4]/div/div[3]/div[3]/div/table/tbody/tr[2]/td[12]'
            # ).click()
            self._driver.find_element(
                By.XPATH, '/html/body/div[5]/div[2]/main/div[2]/div[1]/form/div[3]/div/div[3]/div[3]/div/table/tbody/tr[2]/td[6]'
            ).click()
            self._driver.find_element(By.ID, 'btnVisualizar').click()
            sleep(5)
            self._driver.find_element(By.ID, 'btnAlterar').click()
            sleep(5)
            self._driver.find_element(
                By.XPATH, '//*[@id="form-manutencao"]/div[1]/div[1]/div[4]/div[1]/button'
            ).click()
            sleep(5)
            # self._wdw.until(EC.element_located_to_be_selected((
            #     By.ID,
            #     'aba-cadastro'
            # )))

        select_filter(self)
    
    def get_values(self):
        self._driver.switch_to.frame(self._driver.find_element(By.ID, 'TB_iframeContent'))
        def find_fields(self, field):
            if field == self.FIELDS['bairro']:
                sleep(2)
                self._driver.find_element(By.ID, 'ui-id-4').click()
                # self._wdw.until(EC.element_to_be_selected((By.ID, 'aba-endereco')))
                sleep(5)

            if field in [self.FIELDS['bairro'], self.FIELDS['logradouro']]:
                return self._driver.find_element(By.XPATH, field).text
            return self._driver.find_element(By.ID, field).get_attribute('value')

        for field, element in self.FIELDS.items():
            self.data[field] = find_fields(self, element)
        
        add_log(
            'sigss_mv.py',
            'get_values',
            'INFO',
            f'Dados do usuário {self.data["codigo"]} coletados com sucesso.'
        )
        print(self.data)
        return self.data


class MV(Sistema):
    def __init__(self):
        super().__init__()


    def get_request(self) -> bool:
        if self.login() is False:
            add_log('sigss_mv.py', 'get_request', 'ERRO', f'Não foi possível realizar o login no sistema {self.sistema}')
            return False
        
        filter = JSONDecoder().decode(open(r"src/config/filter_request.json").read())

        self._driver.get('http://c3100prd.cloudmv.com.br/relatorioSocial.jsp')
        self._driver.find_element(By.XPATH, '//*[@id="tipoRelatorio"]/option[5]').click()

        data_inicial = (
            '01/01/2021'
            if filter['data_inicial'] is None
            else filter['data_inicial']
        )
        data_final = (
            filter['data_final']
            if filter['data_final'] is None
            else None
        )
        # TODO - Atribuir propriedade da classe Material
        # beneficio = filter['beneficio'] if filter['beneficio'] in self.BENEFICIO else None
        beneficio = filter['beneficio'] if filter['beneficio'] != None else None
        fornecedor = filter['fornecedor'] if filter['fornecedor'] != None else self.FORNECEDOR

        # def fill_date_form(self, locator, date):
        #     d = self._driver.find_element(*locator)
        #     d.send_keys(Keys.CONTROL, 'a')
        #     d.send_keys(date)

        self.fill_date_form((By.NAME, 'data_ini'), data_inicial)
        # fill_date_form(self, (By.NAME, 'data_ini'), data_inicial)
        if data_final != None:
            self.fill_date_form((By.NAME, 'data_fim'), data_final)
            # fill_date_form(self, (By.NAME, 'data_fim'), data_final)

        # form_page = self._driver.current_window_handle
        
        if beneficio != None:
            self.__fill_form(
                (By.XPATH, '//*[@id="divBeneficio"]/a'),
                beneficio
            )

        self.__fill_form(
            (By.XPATH, '//*[@id="divFornecedor"]/a'),
            fornecedor
        )

        self.__download_request(type='xls')
        self.__download_request(type='pdf')
        return True

    def __split_keys(self, key):
        if key is None:
            return ''
        return key.split(' - ')

    def __download_request(self, type):
        file_name = f'MV_relatorio.{type}'
        if os.path.exists(path + f'/src/downloads/{file_name}'):
            os.remove(path + f'/src/downloads/{file_name}')
        
        self._driver.find_element(By.NAME, f'btnPrint{type.upper()}').click()
        sleep(3)

        main_window = self._driver.current_window_handle
        self._driver.switch_to.window(self._driver.window_handles[1])
        
        if type == 'pdf':
            url = self._driver.current_url
            request.urlopen(url)
            request.urlretrieve(url, path + f'/src/downloads/{file_name}')
        elif type == 'xls':
            while os.path.exists(path + '/src/downloads/analiticoBeneficioUnidadeDetT_RESO_3326-1.xls') is False:
                sleep(1)
            os.rename(
                path + '/src/downloads/analiticoBeneficioUnidadeDetT_RESO_3326-1.xls',
                path + f'/src/downloads/{file_name}'
            )

        self._driver.close()
        self._driver.switch_to.window(main_window)


    def __fill_form(self, locator, keys):
        self._driver.find_element(*locator).click()
        sleep(0.75)
        self._wdw.until(EC.frame_to_be_available_and_switch_to_it((
            By.ID,
            'TB_iframeContent'
        )))

        element = 'ed_busca' if self.__split_keys(keys)[0] == self.FORNECEDOR else 'busca'
        self._driver.find_element(By.NAME, element).send_keys(self.__split_keys(keys)[0])
        self._driver.find_element(By.ID, 'btnBuscar').click()
        sleep(0.3)
        
        result_search = 2 if "DEVOLUCAO" in self.__split_keys(keys) else 1
        self._wdw.until(
            EC.element_to_be_clickable((
                By.XPATH,
                f'//*[@id="tabela"]/table/tbody/tr/td[{result_search}]/input'
            ))
        ).click()

        self._driver.find_element(By.ID, 'btnSelecionar').click()
        self._driver.switch_to.default_content
        sleep(0.75)


if __name__ == "__main__":
    # sigss = Sigss()
    # sigss.login()
    # sigss.search_patient({'nome': 'ANTONIO GREGORIO', 'codigo': ''})
    # sigss.get_values()

    # args = {
    #     'data_inicial': '01/05/2021',
    #     'data_final': None,
    #     # 'beneficio': 'ANDADOR',
    #     'beneficio': None,
    #     'fornecedor': None
    # }
    mv = MV()
    # mv.login()
    mv.get_request()
    mv._logout()
    sleep(5)
