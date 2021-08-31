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
            self._driver.get(self.__url)
            # seleciona o sistema e clica no botao de sair
            if self.sistema == 'MV':
                self._driver.find_element_by_id("sair").click()
                button = self._wdw.until(EC.presence_of_element_located((By.NAME, "sim")))
                button.click()

            if self.sistema == 'SIGSS':
                self._driver.find_element_by_xpath("/html/body/header/div[3]/i[2]").click()
                self._driver.switch_to.active_element.send_keys(Keys.ENTER)

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

    def _wait_and_click(self, locator):
        sleep(0.5)
        while len(self._driver.find_elements(*locator)) < 0:
            sleep(1)
        self._driver.find_element(*locator).click()
        sleep(0.5)

    def close(self):
        if self.__login:
            self._logout()
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
        
        def select_filter(self):
            self.fill_date_form((By.ID, 'dataInicial'), filter['data'])
            self.fill_date_form((By.ID, 'dataFinal'), filter['data'])
            sleep(2)
            self._driver.find_element(By.ID, 'btnBuscar').click()
            sleep(2)
            self._wait_and_click(locator=(
                By.XPATH,
                '/html/body/div[5]/div[2]/main/div[2]/div[1]/form/div[3]/div/div[3]/div[3]/div/table/tbody/tr[2]/td[6]'
            ))
            self._driver.find_element(By.ID, 'btnVisualizar').click()
            sleep(3)
            self._wait_and_click(locator=(By.ID, 'btnAlterar'))
            sleep(3)
            self._driver.find_element(
                By.XPATH, '//*[@id="form-manutencao"]/div[1]/div[1]/div[4]/div[1]/button'
            ).click()
            sleep(5)

        select_filter(self)
    
    def get_values(self):
        self._driver.switch_to.frame(self._driver.find_element(By.ID, 'TB_iframeContent'))
        def find_fields(self, field):
            if field == self.FIELDS['bairro']:
                sleep(2)
                self._driver.find_element(By.ID, 'ui-id-4').click()
                sleep(5)

            if field in [self.FIELDS['bairro'], self.FIELDS['logradouro']]:
                return self._driver.find_element(By.XPATH, field).text
            return self._driver.find_element(By.ID, field).get_attribute('value')

        for field, element in self.FIELDS.items():
            sleep(0.3)
            self.data[field] = find_fields(self, element)
        
        add_log(
            'sigss_mv.py',
            'get_values',
            'INFO',
            f'Dados do usuário {self.data["codigo"]} coletados com sucesso.'
        )
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
            if filter['data_final'] is not None
            else None
        )

        beneficio = filter['beneficio'] if filter['beneficio'] != None else None
        fornecedor = filter['fornecedor'] if filter['fornecedor'] != None else self.FORNECEDOR

        self.fill_date_form((By.NAME, 'data_ini'), data_inicial)
        if data_final != None:
            self.fill_date_form((By.NAME, 'data_fim'), data_final)
        
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

        add_log("siggs_mv.py", "MV.__download_request", "info", "Download dos relatórios efetuado com sucesso.")
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
    # mv = MV()
    # mv.get_request()
    # mv._logout()
    # mv.close()
    # sleep(5)


    siggs = Sigss()
    siggs.search_patient(filter={'nome': 'MARLON DANIEL ANGELI', 'data': '19/08/2021'})
    print(siggs.get_values())