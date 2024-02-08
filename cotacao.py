from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Configuração das opções do Chrome
chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Inicialização do WebDriver com as opções configuradas
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


def auto_extract_dolar(moeda, query):
    try:
        driver.get("https://www.google.com")
        textarea = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
        textarea.send_keys(query)
        textarea.send_keys(Keys.RETURN)
        elemento_moeda = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')))
        time.sleep(4)
        valor_moeda = elemento_moeda.text
        return print('A cotação do Dolar Hoje é de: R$', valor_moeda) 
    except Exception as e:
        print(f"Erro ao extrair cotação da {moeda}: {str(e)}")
    finally:
        driver.quit()
        



valor_do_dolar = auto_extract_dolar("Dólar Americano", "cotação do dólar americano hoje")
print(valor_do_dolar)

# Não esqueça de fechar o driver no final do script
driver.quit()      