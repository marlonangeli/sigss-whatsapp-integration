from functools import partial
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.common.exceptions import NoSuchElementException
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait


def __wait_element(by, element, driver):
    print(f'Aguardando elemento: {by}: {element}')
    if driver.find_element(by, element):
        return True
    return False

driver = webdriver.Chrome(executable_path=r'src\\services\\chromedriver.exe')
driver.get("https://web.whatsapp.com/")
# wdv = WebDriverWait(driver, 30, poll_frequency=5, ignored_exceptions=NoSuchElementException)y
driver.get("https://web.whatsapp.com/send?phone=5545912345678")

while True:
    try:
        if partial(__wait_element, By.ID, 'pane-side'):
            print('numero valido')
            break
    except:
        if partial(__wait_element, By.XPATH, '//*[@id="app"]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div[2]/div'):
            print('numero invalido')
            break
    finally:
        print('finally')
