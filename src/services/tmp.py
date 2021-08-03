# Modulo com a classe dos sistemas onde será coletado os dados dos pacientes

from bs4.element import CharsetMetaAttributeValue
import pandas as pd
from bs4 import BeautifulSoup
import urllib3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

class Sigss:
    # TODO - adicionar chromedriver na pasta do projeto
    def __init__(
        self,
        webdriver_path = '.\\src\\services\\chromedriver.exe',
        show_webdriver = True,
        webdriver_options = None
    ):
        if not show_webdriver:
            webdriver_options = Options()
            webdriver_options.add_argument('--headless')
        self.__url_sigss = 'http://c3100prd.cloudmv.com.br/sigss/login'
        self.chromedriver = webdriver.Chrome(
            executable_path=webdriver_path,
            options=webdriver_options
        )

    def login(self):
        self.username = str(input("Username: ")).split().upper()
        self.password = str(input("Password: ")).split()
        # TODO - fazer validacao

        # Insere os valores nos campos de usuario e senha
        self.chromedriver.get(url=self.__url_sigss)
        self.chromedriver.find_element_by_name("login.login").send_keys(self.username)
        self.chromedriver.find_element_by_name("login.senha").send_keys(self.password + Keys.ENTER)

    def searchUser(self, **kwargs): # utiliza kwargs pois os filtros de pesquisa sao variaveis
        if kwargs == None:
            return None
            # TODO - Colocar o erro no log
        
        else:
            self.chromedriver.get('http://c3100prd.cloudmv.com.br/sigss/cadastroPaciente.jsp')
            sleep(5)
            for key, value in kwargs.items():
                if key == 'codigo':
                    self.chromedriver.find_element_by_xpath(
                        '//*[@id="searchFieldBusca_chzn"]'
                    ).click()
                    self.chromedriver.find_element_by_xpath(
                        '//*[@id="searchFieldBusca_chzn_o_1"]'
                        ).click()
                    self.chromedriver.find_element_by_xpath(
                        '//*[@id="searchStringBusca"]'
                        ).send_keys(value)

                if key == 'nome':
                    self.chromedriver.find_element_by_xpath(
                        '//*[@id="searchStringBuscaUsuServico"]'
                    ).send_keys(value)

                if key == 'nome_da_mae':
                    self.chromedriver.find_element_by_xpath(
                        '//*[@id="enti.entfNomeMaePesquisa"]'
                    ).send_keys(value)

                if key == 'CPF':
                    self.chromedriver.find_element_by_xpath(
                        '//*[@id="entf.entfCPFPesquisa"]'
                    ).send_keys(value)

                if key == 'data_de_nascimento':
                    self.chromedriver.find_element_by_xpath(
                        '//*[@id="isFiltrarDataNasc"]'
                    ).click()
                    self.chromedriver.find_element_by_xpath(
                        '//*[@id="dataNascInicial"]'
                    ).send_keys(value + Keys.TAB + value)

        self.chromedriver.find_element_by_xpath('//*[@id="btnBuscar"]').click()
        sleep(3)
        
        df_usuario = self.chromedriver.find_elements_by_xpath('//*[@id="grid_busca"]')

        print(df_usuario)
        self.chromedriver.find_element_by_xpath(
            '//*[@class="ui-widget-content jqgrow ui-row-ltr"]/td[12]'
        ).click()

        self.chromedriver.find_element_by_xpath('//*[@id="btnVisualizar"]').click()
        sleep(5)
        self.chromedriver.find_element_by_xpath('//*[@id="btnAlterar"]').click()
        sleep(2)
        
        usuario_de_servico = self.chromedriver.find_element_by_xpath(
            '//*[@id="enti.entiNome"]').click()
        usuario_de_servico = self.chromedriver.find_element_by_xpath(
            '//*[@id="enti.entiNome"]').send_keys(Keys.CONTROL + 'A')

        print(usuario_de_servico)
    def __del__(self):
        sleep(5)       
        self.chromedriver.quit()
                

class MV:
    def __init__(self, url_mv, username, password):
        pass

    # todo link relatorio http://c3100prd.cloudmv.com.br/tmp/analiticoBeneficioUnidadeDetT_RESO_3326-1.xls
