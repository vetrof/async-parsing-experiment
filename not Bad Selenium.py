import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

MAX_CONCURRENCY = 4  # Количество экземпляров веб-драйвера, работающих параллельно
semaphore = asyncio.Semaphore(MAX_CONCURRENCY)

async def get_all_links(driver, url):
    async with semaphore:
        # Используем Selenium для навигации и получения данных
        driver.get(url)

        try:
            wait = WebDriverWait(driver, 10)
            wait_info = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#ItemView > div.item > div > div.item__inner-right > div > div:nth-child(1) > div.item__price > div.item__price-left-side > div.item__price-once')))
            print(wait_info.text)

        except:
            pass

async def main():
    # Список URL-адресов, с которых вы хотите получить данные
    urls = [
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/',
        # Добавьте другие URL-адреса, которые вам нужны
    ]

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()
    # driver = webdriver.Firefox()

    # Выполняем предварительные действия перед итерацией по ссылкам
    # driver.get("https://kaspi.kz/shop/")
    # city_link = driver.find_element(By.CSS_SELECTOR, 'li.current-location__dialog-list-el a[data-city-id="710000000"]')
    # actions = ActionChains(driver)
    # actions.move_to_element(city_link).click().perform()

    # Используем asyncio.gather для параллельного выполнения запросов
    tasks = [get_all_links(driver, url) for url in urls]
    await asyncio.gather(*tasks)

    driver.quit()
    end = time.time()
    print('time: ', end - start)

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
