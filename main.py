from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()

amazon_products = []
wait = WebDriverWait(driver, 60)

def search_amazon():
    driver.get("https://www.amazon.com.br/")
    wait
    search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
    submit_button = driver.find_element(By.ID, 'nav-search-submit-button')

    search_box.send_keys('Robô Aspirador Kabum smart 700')
    wait
    submit_button.click()

    try:
        result = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.desktop-grid-content-view')))

        first_five = result[:5]

        for product in first_five:
            try:
                title = product.find_element(By.CSS_SELECTOR, 'h2.a-text-normal').text
                price = product.find_element(By.CSS_SELECTOR, 'span.a-price-whole').text
                link = product.find_element(By.CSS_SELECTOR, 'a.a-text-normal').get_attribute('href')

                amazon_products.append({
                    'title': title,
                    'price': price,
                    'link': link
                })
            except Exception as e:
                print("Erro ao extrair dados do produto:", e)

    except Exception as e:
        print(f"Não foi possível encontrar os resultados da busca: {e}")

    driver.quit()


search_amazon()
print("\n--- Resultados Finais ---")
for product in amazon_products:
    print(product)
