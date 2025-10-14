from scraper import search_amazon
from selenium import webdriver
from time import sleep

products = ['Fone de ouvido QCY MeloBuds N70', 'Redragon Teclado mecânico para jogos 60% sem fio', 'Fritadeira Philco Air Fryer Oven 12L', 'BOLA BASQUETE NBA DRV PRO 7', 'Liquidificador Turbo Full, Mondial, Preto, 900W, 110V - L-900 FB']

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage") 
driver = None

try: 
    driver = webdriver.Chrome(options=options)
    for product in products:
        search_amazon(driver, product)
        sleep(30)
except Exception as e:
    print(f"Ocorreu um erro durante a execução do monitor: {e}")

finally:
    if driver:
        driver.quit()