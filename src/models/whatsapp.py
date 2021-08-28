#!./venv/Scripts/python.exe

import sys
import os

path = os.path.abspath(os.getcwd())
sys.path.append(path + '\\src')

from services.selenium_core import *
from time import sleep
from urllib import parse, request
from thread import KillableThread

from tools.logs import add_log

class WhatsApp:
    def __init__(self):
        self.__nome = None
        self.__numero = None
        self.__login = False
        self.__verify_number = False
        self.__webdriver_path = '.\\src\\services\\chromedriver.exe'
        options = Options()
        # options.add_argument('--headless')
        self.__driver = webdriver.Chrome(self.__webdriver_path, options=options)
        self.__wdw = WebDriverWait(self.__driver, 30)

        self.__cancel = False

    @property
    def is_logged(self):
        return self.__login

    @property
    def numero(self):
        return self.__numero

    @property
    def nome(self):
        return self.__nome

    @property
    def cancel(self):
        return self.__cancel

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @numero.setter
    def numero(self, numero: str):
        self.__numero = numero

    @cancel.setter
    def cancel(self, val: bool):
        self.__cancel = val


    def login(self) -> bool:
        if not self.__login:
            self.__driver.get('https://web.whatsapp.com/')
            
            if os.path.exists('src\\tmp\\qr_code.png'):
                os.remove('src\\tmp\\qr_code.png')
            # faz a verificação de leitura do qr code
            count = 0
            while len(self.__driver.find_elements_by_class_name('_3OvU8')) < 1:
                # limita a execução do programa até que o qr code esteja disponível
                if self.__cancel:
                    print('CANCELANDO A OPERACAO DENTRO DA CLASSE WHATSAPP')
                    self.__login = False
                    self.__cancel_login()
                    # !Não deve retornar, mas é melhor prevenir pela utilização de threads
                    return self.__login

                if count > 20: # TODO - criar um temporizador melhor
                    add_log('whatsapp', 'login', 'erro', f'Tempo de espera de login excedido')
                    self.__login = False
                    return self.__login

                try:
                    # obtém a captura do qr code para colocá-lo na interface gráfica do sistema
                    qr_code = self.__driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[2]/div/canvas')
                    qr_code.screenshot('src\\tmp\\qrcode.png')
                    add_log('whatsapp.py', 'login', 'info', f'Capturando qr code ==> {qr_code}')

                except:
                    print('ocorreu um erro ao obter o qr code')
                # caso ocorra algum erro, adiciona ao log e retorna False
                # except Exception as e:
                #     add_log('whatsapp.py', 'login', 'erro', f'Não foi possível achar o QRCode, erro: {e} ==> {self.nome}')
                #     self.__login = False
                #     return self.__login

                # incrementa o contador
                finally:
                    sleep(5)
                    count += 1

            if len(self.__driver.find_elements_by_class_name('_3OvU8')) > 0:
                #! add_log('whatsapp.py', 'login', 'login', f'Login efetuado com sucesso :{username}')
                self.__login = True

                # navega no perfil para coletar os dados do usuário do whatsapp
                sleep(5)
                self.__driver.find_element_by_xpath('//*[@id="side"]/header/div[1]/div/img').click()
                sleep(3)
                username = self.__driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/div/div/div[2]/div[2]/div[1]/div/div[2]'
                    ).text
                url_img = self.__driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/div/div/div[1]/div/div/div/div/div/img'
                    ).get_attribute('src')

                # adiciona a foto de perfil a pasta tmp
                self.__driver.get(url_img)
                img_user = self.__driver.find_element_by_xpath('/html/body/img')
                img_user.screenshot('src\\tmp\\img_user.png')
                # img_user = open('src\\tmp\\img_user.png', 'wb')
                # img_user.write(request.urlopen(url_img).read())
                # img_user.close()

        return self.__login


    def logout(self) -> bool:
        if not self.__login:
            return True

        # navega no menu para realizar logout
        try:
            self.__driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/div').click()
            self.__driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[6]/div[1]').click()
            self.__login = False
            add_log('whatsapp.py', 'logout', 'logout', f'Logout efetuado com sucesso')
        
        except Exception as e:
            add_log('whatsapp.py', 'logout', 'erro', f'Não foi possível deslogar, Erro: {e}')
            return False

        # remove o qr code e a imagem do usuário da pasta tmp
        # os.remove('src\\tmp\\img_user.png')
        # os.remove('src\\tmp\\qr_code.png')
        return True


    def send_message(self, message: str) -> bool:
        if not self.login():
            add_log('whatsapp.py', 'send_message', 'erro', f'Não foi possível enviar a mensagem, erro no login')
            return False

        if not self.verify_number():
            add_log('whatsapp.py', 'send_message', 'erro', f'Não foi possível enviar a mensagem, erro ao verificar o número')
            return False

        # converte a mensagem para formato de url
        message = parse.quote(message)
        try: # TODO - verificar se a mensagem foi enviada
            self.__driver.get(f'https://web.whatsapp.com/send?phone=55{self.numero}&text={message}')
            sleep(5)
            self.__driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]/button').click()
            sleep(5)
            return True
        except Exception as e:
            add_log('whatsapp.py', 'send_message', 'erro', f'Não foi possível enviar a mensagem, erro: {e} ==> {self.nome}')
            return False

    
    def verify_number(self) -> bool:
        if not self.login():
            add_log('whatsapp.py', 'verify_number', 'erro', f'Não foi possível verificar o número, erro no login ==> {self.nome}')
            self.__verify_number = False
            return self.__verify_number
        
        if not self.__verify_number:
            self.__driver.get(f'https://web.whatsapp.com/search?q=55{self.numero}')
            sleep(5)
            
            while len(self.__driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]')) < 1:
                try:
                    self.__driver.find_element_by_xpath('//*[@id="app"]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div[2]/div').click()
                    self.__verify_number = False
                    return self.__verify_number
                except:
                    pass
                finally:
                    sleep(3)
                    

            # wait = WebDriverWait(self.__driver, 15)
            # try:
            #     wait.until(
            #         self.__driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').click()
            #     )
            #     add_log('whatsapp.py', 'verify_number', 'sucesso', f'Número verificado com sucesso ==> {self.nome}')
            #     self.__verify_number = True
            # except NoSuchElementException:
            #     wait.until(
            #         self.__driver.find_element_by_xpath('//*[@id="app"]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div[2]/div/div/div').click()
            #     )
            #     add_log('whatsapp.py', 'verify_number', 'falha', f'Número inválido ==> {self.nome}')
            #     self.__verify_number = False

            # except TimeoutException:
            #     add_log('whatsapp.py', 'verify_number', 'erro', f'Tempo de espera excedido ==> {self.nome}')
            #     self.__verify_number = False
    
        self.__verify_number = True
        return self.__verify_number


    def __cancel_login(self):
        self.delete()


    def delete(self):
        if self.__login:
            self.logout()
        if os.path.exists('src\\tmp\\qrcode.png'):
            os.remove('src\\tmp\\qrcode.png')
        if os.path.exists('src\\tmp\\img_user.png'):
            os.remove('src\\tmp\\img_user.png')
        self.__driver.quit()


if __name__ == '__main__':
    wpp = WhatsApp()
    wpp.login()
