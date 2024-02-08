from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuração das opções do Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Inicialização do WebDriver com as opções configuradas
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)



def fluxoCompra_Saucedemo():
    driver.get('https://www.saucedemo.com/')
    username = driver.find_element(By.NAME, 'user-name')
    username.send_keys("standard_user")
    password = driver.find_element(By.NAME, 'password')
    password.send_keys("secret_sauce")
    login_button = driver.find_element(By.NAME, 'login-button')
    login_button.click()
    produto01 = driver.find_element(By.NAME, 'add-to-cart-sauce-labs-backpack')
    produto01.click()
    produto02 = driver.find_element(By.NAME, 'add-to-cart-sauce-labs-bike-light')
    produto02.click()
    produto03 = driver.find_element(By.NAME, 'add-to-cart-sauce-labs-bolt-t-shirt')
    produto03.click()
    produto04 = driver.find_element(By.NAME, 'add-to-cart-sauce-labs-fleece-jacket')
    produto04.click()
    produto05 = driver.find_element(By.NAME, 'add-to-cart-sauce-labs-onesie')
    produto05.click()
    produto06 = driver.find_element(By.NAME, 'add-to-cart-test.allthethings()-t-shirt-(red)')
    produto06.click()
    click_car = driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link')
    click_car.click()
    checkout = driver.find_element(By.NAME, 'checkout')
    checkout.click()
    firstName = driver.find_element(By.NAME, 'firstName')
    firstName.send_keys('Maxwell')
    lastName = driver.find_element(By.NAME, 'lastName')
    lastName.send_keys('Viana')
    campoCEP = driver.find_element(By.NAME, 'postalCode')
    campoCEP.send_keys('31710515')
    btnContinue = driver.find_element(By.NAME, 'continue')
    btnContinue.click()
    btnFinish = driver.find_element(By.NAME, 'finish')
    btnFinish.click()
    btnBackhome = driver.find_element(By.NAME, 'back-to-products')
    btnBackhome.click()
    btnMenu = driver.find_element(By.ID, 'react-burger-menu-btn')
    btnMenu.click()
    time.sleep(1)
    btnLogout = driver.find_element(By.ID, 'logout_sidebar_link')
    btnLogout.click()
    print('Etapa de compra no Site Saucedemo realizada com Sucesso!')
    
    
def loginCaminhoFeliz():
    driver.get('https://www.saucedemo.com/')
    username = driver.find_element(By.NAME, 'user-name')
    username.send_keys("standard_user")
    password = driver.find_element(By.NAME, 'password')
    password.send_keys("secret_sauce")
    login_button = driver.find_element(By.NAME, 'login-button')
    login_button.click()
    app_logo_elements = driver.find_elements(By.CSS_SELECTOR, ".app_logo")
    if len(app_logo_elements) >  0:
        print("O elemento com a classe 'app_logo' foi encontrado.")
    else:
        print("O elemento com a classe 'app_logo' não foi encontrado.")

def loginUsuarioInexistente():
    driver.get('https://www.saucedemo.com/')
    username = driver.find_element(By.NAME, 'user-name')
    username.send_keys("standard_userinexistente")
    password = driver.find_element(By.NAME, 'password')
    password.send_keys("secret_sauce")
    login_button = driver.find_element(By.NAME, 'login-button')
    login_button.click()
    time.sleep(3)
    error_message_elements = driver.find_elements(By.XPATH, "//h3[@data-test='error']")
    if len(error_message_elements) >  0:
        error_message = error_message_elements[0].text
        if "Epic sadface: Username and password do not match any user in this service" in error_message:
            print("A mensagem de erro específica foi encontrada.")
        else:
            print("A mensagem de erro específica não foi encontrada.")
    else:
        print("A mensagem de erro não foi encontrada.")

def loginPassworInexistente():
    driver.get('https://www.saucedemo.com/')
    username = driver.find_element(By.NAME, 'user-name')
    username.send_keys("standard_user")
    password = driver.find_element(By.NAME, 'password')
    password.send_keys("secret_sauceidexistente")
    login_button = driver.find_element(By.NAME, 'login-button')
    login_button.click()
    time.sleep(3)
    error_message_elements = driver.find_elements(By.XPATH, "//h3[@data-test='error']")
    if len(error_message_elements) >  0:
        error_message = error_message_elements[0].text
        if "Epic sadface: Username and password do not match any user in this service" in error_message:
            print("A mensagem de erro específica foi encontrada.")
        else:
            print("A mensagem de erro específica não foi encontrada.")
    else:
        print("A mensagem de erro não foi encontrada.")
    
    
            
        
    
    

fluxoCompra_Saucedemo()
loginCaminhoFeliz()
loginUsuarioInexistente()
loginPassworInexistente()
