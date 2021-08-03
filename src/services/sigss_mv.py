#!./venv/Scripts/python.exe

import sys
import os

path = os.path.abspath(os.getcwd())
sys.path.append(path + '\\src')

from json.decoder import JSONDecoder
from time import sleep

from selenium_core import *

from tools.logs import add_log


class Sistema:
    __credentials = JSONDecoder().decode(open(r"src/services/.credentials.json").read())
    def __init__(self):
        self.__username = self.__credentials["username"]
        self.__password = self.__credentials["password"]
        self.__login = False
        self.sistema = self.__class__.__name__.upper()
        options = Options()
        # options.add_argument("--headless")
        self.__driver = webdriver.Chrome(executable_path=WEBDRIVER_PATH, options=options)
        self.__wdw = WebDriverWait(self.__driver, 10)

        if self.sistema == 'SIGSS':
            self.__url = "http://c3100prd.cloudmv.com.br/sigss/login"
        elif self.sistema == 'MV':
            self.__url = "http://c3100prd.cloudmv.com.br/login"
        else:
            raise Exception('Sistema inválido')


    def _login(self) -> bool:
        if not self.__login:
            # acessa a pagina de login
            self.__driver.get(self.__url)
            
            # seleciona o sistema e aguarda o carregamento
            if self.sistema == 'MV':
                self.__wdw.until(
                    EC.presence_of_element_located((By.NAME, "usuario"))
                ).send_keys(self.__username)
                self.__driver.find_element_by_name("senha").send_keys(self.__password)
                self.__driver.find_element_by_id("btnEntrar").click()
            
            if self.sistema == 'SIGSS':
                self.__wdw.until(
                    EC.presence_of_element_located((By.ID, "login.login"))
                ).send_keys(self.__username)
                self.__driver.find_element_by_id("login.senha").send_keys(self.__password)
                self.__driver.find_element_by_id("entrar").click()
                
            # adiciona evento no log
            add_log(
                'sigss_mv.py',
                "Sistema._login",
                "INFO",
                f'Login no sistema {self.sistema} efetuado com sucesso: {self.__username}'
            )
            self.__login = True
        
        return self.__login


    def _logout(self) -> bool:
        if self.__login:
            # seleciona o sistema e clica no botao de sair
            if self.sistema == 'MV':
                self.__driver.find_element_by_id("sair").click()
                button = self.__wdw.until(EC.presence_of_element_located((By.NAME, "sim")))
                button.click()

            if self.sistema == 'SIGSS':
                self.__driver.find_element_by_xpath("/html/body/header/div[3]/i[2]").click()
                self.__driver.switch_to.active_element.send_keys(Keys.ENTER)

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


    def __del__(self):
        self._logout()
        self.__driver.quit()
        # self.__driver.close()


class Sigss(Sistema):
    pass


class MV(Sistema):
    pass


if __name__ == "__main__":
    sigss = Sigss()
    sigss._login()
    sleep(5)
    del sigss


    mv = MV()
    mv._login()
    sleep(5)
    del mv
