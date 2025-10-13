from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def search_amazon(driver, search_term):

    amazon_products = []
    wait = WebDriverWait(driver, 20)

    try:    
        driver.get("https://www.amazon.com.br/")
        
        search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
        submit_button = driver.find_element(By.ID, 'nav-search-submit-button')
        search_box.clear()
        search_box.send_keys(search_term)
        submit_button.click()

        result = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.desktop-grid-content-view')))
        products = result[:5]

        for product in products:
            try:
                title = product.find_element(By.CSS_SELECTOR, 'h2.a-text-normal').text
                try:
                    price_whole = product.find_element(By.CSS_SELECTOR, 'span.a-price-whole').text
                    price_fraction = product.find_element(By.CSS_SELECTOR, 'span.a-price-fraction').text
                    price = f"{price_whole},{price_fraction}"
                except:
                    price = "Indisponível"
                link = product.find_element(By.CSS_SELECTOR, 'a.a-text-normal').get_attribute('href')

                amazon_products.append({
                    'data_hora_busca': pd.Timestamp.now(),
                    'termo_busca': search_term,
                    'loja': 'Amazon',
                    'titulo_produto': title,
                    'preco': price,
                    'link': link
                })
                print("produto adicionado:", title, price, link)
            except Exception as e:
                print("Erro ao extrair dados do produto:", e)

    except Exception as e:
        print(f"Não foi possível encontrar os resultados da busca: {e}")
        return []
    
    try:
        df = pd.DataFrame(amazon_products)
        df.to_csv('./data/analise_produtos.csv', mode='a', header=False, index=False)
    except Exception as e:
        print(f"Erro ao salvar os dados em CSV: {e}")

    return amazon_products

