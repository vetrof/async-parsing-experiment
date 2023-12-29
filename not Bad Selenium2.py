import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

start = time.time()
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

for url in urls:
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    name_card = driver.find_element(By.CSS_SELECTOR, '#ItemView > div.item > div > div.item__inner-right > div > div:nth-child(1) > h1').text
    print(f"Item Name: {name_card}")
    driver.quit()

end = time.time()
print('time: ', end - start)
