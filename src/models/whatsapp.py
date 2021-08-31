import os
import sys
path = os.path.abspath(os.getcwd())
sys.path.append(path)

from src.services.selenium_core import *
from src.services.functions_core import *

class WhatsApp:
    def __init__(self):
        self.__nome = None
        self.__numero = None
        self.__login = False
        self.__verify_number = False
        self.__username = None
        self.__webdriver_path = WEBDRIVER_PATH
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

    @property
    def username(self):
        return self.__username

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
            sleep(3)
            if os.path.exists('./src/tmp/qr_code.png'):
                os.remove('./src/tmp/qr_code.png')
            # faz a verificação de leitura do qr code
            count = 0
            print(self.__driver.find_elements(By.CLASS_NAME, '_3OvU8'))
            while len(self.__driver.find_elements(By.CLASS_NAME, '_3OvU8')) < 1:
                # limita a execução do programa até que o qr code esteja disponível
                if self.__cancel:
                    add_log("whatsapp.py", 'login', 'info', 'Login cancelado')
                    self.__login = False
                    self.__cancel_login()
                    # !Não deve retornar, mas é melhor prevenir pela utilização de threads
                    # return self.__login

                if count > 20:
                    add_log('whatsapp', 'login', 'erro', f'Tempo de espera de login excedido')
                    self.__login = False
                    return self.__login

                try:
                    # obtém a captura do qr code para colocá-lo na interface gráfica do sistema
                    qr_code = self.__driver.find_element(
                        By.XPATH,
                        '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[2]/div/canvas'
                    )
                    qr_code.screenshot('./src/tmp/qr_code.png')

                except Exception as e:
                    if count > 1:
                        add_log('whatsapp.py', 'login', 'debug', f'Não foi possível capturar o QR Code ==> {e}')
               
                finally:
                    sleep(5)
                    count += 1

            print('saí do while')

            if len(self.__driver.find_elements(By.CLASS_NAME, '_3OvU8')) > 0:
                self.__login = True
                
                sleep(3)
                self._wait_and_click(locator=(By.XPATH, '//*[@id="side"]/header/div[1]/div/img'))
                sleep(3) # carrega animacao
                # url_img = self.__driver.find_element_by_xpath(
                #     '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/div/div/div[1]/div/div/div/div/div/img'
                #     ).get_attribute('src')

                try:
                    self.__username = self.__driver.find_element_by_xpath(
                        '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]'
                        ).text
                    self.__version = "Business"
                except:
                    self.__username = self.__driver.find_element_by_xpath(
                        '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/div/div/div[2]/div[2]/div[1]/div/div[2]'
                        ).text
                    self.__version = "Normal"
                
                # get screenshot of the profile photo
                # self.__driver.get(url_img)
                # img_user = self.__driver.find_element_by_xpath('/html/body/img')
                # img_user.screenshot('src\\tmp\\img_user.png')


                add_log('whatsapp.py', 'login', 'login', f'Login efetuado com sucesso :{self.__username}')

        return self.__login


    def logout(self) -> bool:
        if not self.__login:
            return True

        # navega no menu para realizar logout
        try:
            self._wait_and_click(locator=(By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[3]/div'))
            xpath_btn = (
                '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[6]/div[1]'
                if self.__version == "Normal"
                else '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[8]/div[1]'
            )
            self._wait_and_click(locator=(By.XPATH, xpath_btn))
            self.__login = False
            add_log('whatsapp.py', 'logout', 'logout', f'Logout efetuado com sucesso')
        
        except Exception as e:
            add_log('whatsapp.py', 'logout', 'erro', f'Não foi possível deslogar, Erro: {e}')
            return False

        # remove o qr code e a imagem do usuário da pasta tmp
        if os.path.exists('./src/tmp/qr_code.png'):
            os.remove('./src/tmp/qr_code.png')
        if os.path.exists('./src/tmp/img_user.png'):
            os.remove('./src/tmp/img_user.png')

        return True


    def send_message(self, message: str, verify: bool = False) -> bool:
        if not self.login():
            add_log('whatsapp.py', 'send_message', 'erro', f'Não foi possível enviar a mensagem, erro no login')
            return False

        if verify:
            if not self.verify_number():
                add_log('whatsapp.py', 'send_message', 'erro', f'Não foi possível enviar a mensagem, erro ao verificar o número')
                return False

        # converte a mensagem para formato de url
        message = parse.quote(message)
        try:
            self.__driver.get(f'https://web.whatsapp.com/send?phone=55{self.numero}&text={message}')
            sleep(5)
            self._wait_and_click(locator=(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]/button'))
            sleep(5)
            add_log('whatsapp.py', 'send_message', 'info', f'Mensagem enviada para {self.numero} em {get_date()}')
            return True
        except Exception as e:
            add_log('whatsapp.py', 'send_message', 'erro', f'Não foi possível enviar a mensagem, erro: {e} ==> {self.nome}')
            return False

    
    def verify_number(self) -> bool:
        if not self.login():
            add_log('whatsapp.py', 'verify_number', 'erro', f'Não foi possível verificar o número, erro no login ==> {self.nome}')
            self.__verify_number = False
            return self.__verify_number
        
        self.__driver.get(f'https://web.whatsapp.com/send?phone=55{self.numero}')
        sleep(5)
        
        while len(self.__driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]')) < 1:
            try:
                self.__driver.find_element_by_xpath('//*[@id="app"]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div[2]/div').click()
                self.__verify_number = False
                add_log('whatsapp.py', 'verify_number', 'info', f'Número não é válido ==> {self.numero}')
                return self.__verify_number
            except:
                pass
            finally:
                sleep(3)
                
        if len(self.__driver.find_elements(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]')) > 0:
            self.__verify_number = True
            add_log('whatsapp.py', 'verify_number', 'info', f'Número válido ==> {self.numero}')
            return self.__verify_number


    def __cancel_login(self):
        self.delete()


    def delete(self):
        if self.__login:
            self.logout()
        if os.path.exists('./src/tmp/qr_code.png'):
            os.remove('./src/tmp/qr_code.png')
        if os.path.exists('./src/tmp/img_user.png'):
            os.remove('./src/tmp/img_user.png')
        self.__driver.quit()


    def _wait_and_click(self, locator):
        sleep(0.5)
        while len(self.__driver.find_elements(*locator)) < 0:
            sleep(1)
        self.__driver.find_element(*locator).click()
        sleep(0.5)


if __name__ == '__main__':
    wpp = WhatsApp()
    wpp.login()
    lista = [
        "4584214127",
        "4512345678",
        "4591121567",
    ]
    for numero in lista:
        wpp.numero = numero
        print(numero)
        wpp.verify_number()
