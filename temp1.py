import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

async def get_all_links(driver, url):
    # Используем Selenium для навигации и получения данных
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, lambda: driver.get(url))

    try:
        wait = WebDriverWait(driver, 10)
        wait_info = await loop.run_in_executor(None, lambda: wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#ItemView > div.item > div > div.item__inner-right > div > div:nth-child(1) > div.item__price > div.item__price-left-side > div.item__price-once'))))
        print(wait_info.text)

    except Exception as e:
        print("Произошла ошибка:", str(e))

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

    # Используем asyncio.gather для параллельного выполнения запросов
    tasks = [get_all_links(driver, url) for url in urls]
    await asyncio.gather(*tasks)

    driver.quit()

if __name__ == "__main__":
    asyncio.run(main())
