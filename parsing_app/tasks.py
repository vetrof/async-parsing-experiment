from celery import shared_task
import time

from selenium import webdriver
from selenium_async import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#   chrome
@shared_task()
def test1():
    time_start = time.time()
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()

    version = driver.capabilities['chrome']['chromedriverVersion']
    print(f"******************************************************    ChromeDriver version: {version}")

    driver.get("https://kaspi.kz/shop/")  # открываем магазин
    city_link = driver.find_element(By.CSS_SELECTOR,
                                    'li.current-location__dialog-list-el a[data-city-id="710000000"]')  # выбираем селектор с городом
    actions = ActionChains(driver)
    actions.move_to_element(
        city_link).click().perform()  # ActionChains для выполнения клика

    all_count_link = 0
    cards_info = []

    for _ in range(30):

        time_card_start = time.time()

        card_info = {}

        link = 'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/'

        name_card = None
        price_card = None
        description = None
        size = None
        color = None

        top_saller = None
        place_1 = None
        place_1_price = None
        delivery = None
        place_2 = None
        place_2_price = None
        place_3 = None
        place_3_price = None
        place_4 = None
        place_4_price = None
        place_5 = None
        place_5_price = None

        driver.get(link)  # загружаем карточку
        try:
            wait = WebDriverWait(driver, 10)
            wait_info = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'td.sellers-table__cell:nth-child(1)')))
        except:
            time.sleep(3)

        all_count_link += 1

        for _ in range(3):
            # get info
            try:
                name_card = driver.find_element(By.CSS_SELECTOR, '#ItemView > div.item > div > div.item__inner-right > div > div:nth-child(1) > h1').text
                card_info['name_card'] = name_card
            except:
                pass

            try:
                price_card = driver.find_element(By.CSS_SELECTOR, '#ItemView > div.item > div > div.item__inner-right > div > div:nth-child(1) > div.item__price > div.item__price-left-side > div.item__price-once').text
                card_info['price_card'] = price_card
            except:
                pass

            try:
                description = driver.find_element(By.CSS_SELECTOR, '#ItemView > div.item > div > div.item__inner-right > div > div.item__description-text').text
                card_info['price_card'] = price_card
            except:
                pass

            # try:
            #     color = driver.find_element(By.CSS_SELECTOR, '#ItemView > div.item > div > div.item__inner-right > div > div.item-configurator.undefined > div:nth-child(1) > div > div > div > label').text
            # except:
            #     pass
            #
            # try:
            #     size = driver.find_element(By.CSS_SELECTOR, '#ItemView > div.item > div > div.item__inner-right > div > div.item-configurator.undefined > div:nth-child(2) > div > div > div > label').text
            # except:
            #     pass

            # get sallers

            # try:
            #     top_saller = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr > td:nth-child(1) > a').text
            #     card_info['top_saller'] = top_saller
            # except:
            #     pass

            try:
                place_1 = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > a').text
                place_1_price = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(4) > div').text
                delivery = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > span > span').text
            except:
                pass

            try:
                place_2 = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > a').text
                place_2_price = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(2) > td:nth-child(4) > div').text
            except:
                pass

            # try:
            #     place_3 = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(3) > td:nth-child(1) > a').text
            #     place_3_price = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(3) > td:nth-child(4) > div').text
            # except:
            #     pass
            #
            # try:
            #     place_4 = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(4) > td:nth-child(1) > a').text
            #     place_4_price = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(4) > td:nth-child(4) > div').text
            # except:
            #     pass
            #
            # try:
            #     place_5 = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(5) > td:nth-child(1) > a').text
            #     place_5_price = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(5) > td:nth-child(4) > div').text
            # except:
            #     pass

            if place_1:
                print('ok', all_count_link, _)

                break

            else:
                driver.get(link)  # загружаем карточку
                print('второй круг', all_count_link, _, link)
                time.sleep(3)

        if place_1_price:
            place_1_price = place_1_price.rstrip('₸').replace(' ', '')
        if place_2_price:
            place_2_price = place_2_price.rstrip('₸').replace(' ', '')
        if place_3_price:
            place_3_price = place_3_price.rstrip('₸').replace(' ', '')
        if place_4_price:
            place_4_price = place_4_price.rstrip('₸').replace(' ', '')
        if place_5_price:
            place_5_price = place_5_price.rstrip('₸').replace(' ', '')

        cards_info.append(card_info)
        time_card_end = time.time()
        time_per_cards = time_card_start - time_card_end
        print(time_per_cards)

    driver.quit()
    print(cards_info)
    time_end = time.time()
    time_all = time_start - time_end
    print(all_count_link, time_all)
    return cards_info

#  firefox
@shared_task()
def test2():
    time_start = time.time()

    options = FirefoxOptions()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Firefox(options=options)

    driver.get("https://kaspi.kz/shop/")  # открываем магазин
    city_link = driver.find_element(By.CSS_SELECTOR,
                                    'li.current-location__dialog-list-el a[data-city-id="710000000"]')  # выбираем селектор с городом
    actions = ActionChains(driver)
    actions.move_to_element(
        city_link).click().perform()  # ActionChains для выполнения клика

    all_count_link = 0
    cards_info = []

    for _ in range(30):

        time_card_start = time.time()

        card_info = {}

        link = 'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/'

        name_card = None
        price_card = None
        description = None
        size = None
        color = None

        top_saller = None
        place_1 = None
        place_1_price = None
        delivery = None
        place_2 = None
        place_2_price = None
        place_3 = None
        place_3_price = None
        place_4 = None
        place_4_price = None
        place_5 = None
        place_5_price = None

        driver.get(link)  # загружаем карточку
        try:
            wait = WebDriverWait(driver, 10)
            wait_info = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'td.sellers-table__cell:nth-child(1)')))
        except:
            time.sleep(3)

        all_count_link += 1

        for _ in range(3):
            # get info
            try:
                name_card = driver.find_element(By.CSS_SELECTOR, '#ItemView > div.item > div > div.item__inner-right > div > div:nth-child(1) > h1').text
                card_info['name_card'] = name_card
            except:
                pass

            try:
                price_card = driver.find_element(By.CSS_SELECTOR, '#ItemView > div.item > div > div.item__inner-right > div > div:nth-child(1) > div.item__price > div.item__price-left-side > div.item__price-once').text
                card_info['price_card'] = price_card
            except:
                pass

            try:
                description = driver.find_element(By.CSS_SELECTOR, '#ItemView > div.item > div > div.item__inner-right > div > div.item__description-text').text
                card_info['price_card'] = price_card
            except:
                pass

            # try:
            #     color = driver.find_element(By.CSS_SELECTOR, '#ItemView > div.item > div > div.item__inner-right > div > div.item-configurator.undefined > div:nth-child(1) > div > div > div > label').text
            # except:
            #     pass
            #
            # try:
            #     size = driver.find_element(By.CSS_SELECTOR, '#ItemView > div.item > div > div.item__inner-right > div > div.item-configurator.undefined > div:nth-child(2) > div > div > div > label').text
            # except:
            #     pass

            # get sallers

            # try:
            #     top_saller = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr > td:nth-child(1) > a').text
            #     card_info['top_saller'] = top_saller
            # except:
            #     pass

            try:
                place_1 = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > a').text
                place_1_price = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(4) > div').text
                delivery = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > span > span').text
            except:
                pass

            try:
                place_2 = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > a').text
                place_2_price = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(2) > td:nth-child(4) > div').text
            except:
                pass

            # try:
            #     place_3 = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(3) > td:nth-child(1) > a').text
            #     place_3_price = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(3) > td:nth-child(4) > div').text
            # except:
            #     pass
            #
            # try:
            #     place_4 = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(4) > td:nth-child(1) > a').text
            #     place_4_price = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(4) > td:nth-child(4) > div').text
            # except:
            #     pass
            #
            # try:
            #     place_5 = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(5) > td:nth-child(1) > a').text
            #     place_5_price = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(5) > td:nth-child(4) > div').text
            # except:
            #     pass

            if place_1:
                print('ok', all_count_link, _)

                break

            else:
                driver.get(link)  # загружаем карточку
                print('второй круг', all_count_link, _, link)
                time.sleep(3)

        if place_1_price:
            place_1_price = place_1_price.rstrip('₸').replace(' ', '')
        if place_2_price:
            place_2_price = place_2_price.rstrip('₸').replace(' ', '')
        if place_3_price:
            place_3_price = place_3_price.rstrip('₸').replace(' ', '')
        if place_4_price:
            place_4_price = place_4_price.rstrip('₸').replace(' ', '')
        if place_5_price:
            place_5_price = place_5_price.rstrip('₸').replace(' ', '')

        cards_info.append(card_info)
        time_card_end = time.time()
        time_per_cards = time_card_start - time_card_end
        print(time_per_cards)

    driver.quit()
    print(cards_info)
    time_end = time.time()
    time_all = time_start - time_end
    print(all_count_link, time_all)
    return cards_info


@shared_task()
def test3():
    time_start = time.time()
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()

    driver.get("https://kaspi.kz/shop/")  # открываем магазин
    city_link = driver.find_element(By.CSS_SELECTOR,
                                    'li.current-location__dialog-list-el a[data-city-id="710000000"]')  # выбираем селектор с городом
    actions = ActionChains(driver)
    actions.move_to_element(
        city_link).click().perform()  # ActionChains для выполнения клика

    all_count_link = 0
    cards_info = []

    for _ in range(30):

        time_card_start = time.time()

        card_info = {}

        link = 'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/'

        name_card = None
        price_card = None
        description = None
        size = None
        color = None

        top_saller = None
        place_1 = None
        place_1_price = None
        delivery = None
        place_2 = None
        place_2_price = None
        place_3 = None
        place_3_price = None
        place_4 = None
        place_4_price = None
        place_5 = None
        place_5_price = None

        driver.get(link)  # загружаем карточку
        try:
            wait = WebDriverWait(driver, 10)
            wait_info = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'td.sellers-table__cell:nth-child(1)')))
        except:
            time.sleep(3)

        all_count_link += 1

        for _ in range(3):
            # get info
            try:
                name_card = driver.find_element(By.CSS_SELECTOR, '#ItemView > div.item > div > div.item__inner-right > div > div:nth-child(1) > h1').text
                card_info['name_card'] = name_card
            except:
                pass

            try:
                price_card = driver.find_element(By.CSS_SELECTOR, '#ItemView > div.item > div > div.item__inner-right > div > div:nth-child(1) > div.item__price > div.item__price-left-side > div.item__price-once').text
                card_info['price_card'] = price_card
            except:
                pass

            try:
                description = driver.find_element(By.CSS_SELECTOR, '#ItemView > div.item > div > div.item__inner-right > div > div.item__description-text').text
                card_info['price_card'] = price_card
            except:
                pass

            # try:
            #     color = driver.find_element(By.CSS_SELECTOR, '#ItemView > div.item > div > div.item__inner-right > div > div.item-configurator.undefined > div:nth-child(1) > div > div > div > label').text
            # except:
            #     pass
            #
            # try:
            #     size = driver.find_element(By.CSS_SELECTOR, '#ItemView > div.item > div > div.item__inner-right > div > div.item-configurator.undefined > div:nth-child(2) > div > div > div > label').text
            # except:
            #     pass

            # get sallers

            # try:
            #     top_saller = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr > td:nth-child(1) > a').text
            #     card_info['top_saller'] = top_saller
            # except:
            #     pass

            try:
                place_1 = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > a').text
                place_1_price = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(4) > div').text
                delivery = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > span > span').text
            except:
                pass

            try:
                place_2 = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > a').text
                place_2_price = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(2) > td:nth-child(4) > div').text
            except:
                pass

            # try:
            #     place_3 = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(3) > td:nth-child(1) > a').text
            #     place_3_price = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(3) > td:nth-child(4) > div').text
            # except:
            #     pass
            #
            # try:
            #     place_4 = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(4) > td:nth-child(1) > a').text
            #     place_4_price = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(4) > td:nth-child(4) > div').text
            # except:
            #     pass
            #
            # try:
            #     place_5 = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(5) > td:nth-child(1) > a').text
            #     place_5_price = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(5) > td:nth-child(4) > div').text
            # except:
            #     pass

            if place_1:
                print('ok', all_count_link, _)

                break

            else:
                driver.get(link)  # загружаем карточку
                print('второй круг', all_count_link, _, link)
                time.sleep(3)

        if place_1_price:
            place_1_price = place_1_price.rstrip('₸').replace(' ', '')
        if place_2_price:
            place_2_price = place_2_price.rstrip('₸').replace(' ', '')
        if place_3_price:
            place_3_price = place_3_price.rstrip('₸').replace(' ', '')
        if place_4_price:
            place_4_price = place_4_price.rstrip('₸').replace(' ', '')
        if place_5_price:
            place_5_price = place_5_price.rstrip('₸').replace(' ', '')

        cards_info.append(card_info)
        time_card_end = time.time()
        time_per_cards = time_card_start - time_card_end
        print(time_per_cards)

    driver.quit()
    print(cards_info)
    time_end = time.time()
    time_all = time_start - time_end
    print(all_count_link, time_all)
    return cards_info


@shared_task()
def test4():
    time_start = time.time()
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()

    driver.get("https://kaspi.kz/shop/")  # открываем магазин
    city_link = driver.find_element(By.CSS_SELECTOR,
                                    'li.current-location__dialog-list-el a[data-city-id="710000000"]')  # выбираем селектор с городом
    actions = ActionChains(driver)
    actions.move_to_element(
        city_link).click().perform()  # ActionChains для выполнения клика

    all_count_link = 0
    cards_info = []

    for _ in range(30):

        time_card_start = time.time()

        card_info = {}

        link = 'https://kaspi.kz/shop/p/batik-2004-k-18-kostjum-pirat-spaik-2004-k-18-mul-tikolor-122-64-114711293/'

        name_card = None
        price_card = None
        description = None
        size = None
        color = None

        top_saller = None
        place_1 = None
        place_1_price = None
        delivery = None
        place_2 = None
        place_2_price = None
        place_3 = None
        place_3_price = None
        place_4 = None
        place_4_price = None
        place_5 = None
        place_5_price = None

        driver.get(link)  # загружаем карточку
        try:
            wait = WebDriverWait(driver, 10)
            wait_info = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'td.sellers-table__cell:nth-child(1)')))
        except:
            time.sleep(3)

        all_count_link += 1

        for _ in range(3):
            # get info
            try:
                name_card = driver.find_element(By.CSS_SELECTOR, '#ItemView > div.item > div > div.item__inner-right > div > div:nth-child(1) > h1').text
                card_info['name_card'] = name_card
            except:
                pass

            try:
                price_card = driver.find_element(By.CSS_SELECTOR, '#ItemView > div.item > div > div.item__inner-right > div > div:nth-child(1) > div.item__price > div.item__price-left-side > div.item__price-once').text
                card_info['price_card'] = price_card
            except:
                pass

            try:
                description = driver.find_element(By.CSS_SELECTOR, '#ItemView > div.item > div > div.item__inner-right > div > div.item__description-text').text
                card_info['price_card'] = price_card
            except:
                pass

            # try:
            #     color = driver.find_element(By.CSS_SELECTOR, '#ItemView > div.item > div > div.item__inner-right > div > div.item-configurator.undefined > div:nth-child(1) > div > div > div > label').text
            # except:
            #     pass
            #
            # try:
            #     size = driver.find_element(By.CSS_SELECTOR, '#ItemView > div.item > div > div.item__inner-right > div > div.item-configurator.undefined > div:nth-child(2) > div > div > div > label').text
            # except:
            #     pass

            # get sallers

            # try:
            #     top_saller = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr > td:nth-child(1) > a').text
            #     card_info['top_saller'] = top_saller
            # except:
            #     pass

            try:
                place_1 = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > a').text
                place_1_price = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(4) > div').text
                delivery = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > span > span').text
            except:
                pass

            try:
                place_2 = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > a').text
                place_2_price = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(2) > td:nth-child(4) > div').text
            except:
                pass

            # try:
            #     place_3 = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(3) > td:nth-child(1) > a').text
            #     place_3_price = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(3) > td:nth-child(4) > div').text
            # except:
            #     pass
            #
            # try:
            #     place_4 = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(4) > td:nth-child(1) > a').text
            #     place_4_price = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(4) > td:nth-child(4) > div').text
            # except:
            #     pass
            #
            # try:
            #     place_5 = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(5) > td:nth-child(1) > a').text
            #     place_5_price = driver.find_element(By.CSS_SELECTOR, '#offers > div > div > div > table > tbody > tr:nth-child(5) > td:nth-child(4) > div').text
            # except:
            #     pass

            if place_1:
                print('ok', all_count_link, _)

                break

            else:
                driver.get(link)  # загружаем карточку
                print('второй круг', all_count_link, _, link)
                time.sleep(3)

        if place_1_price:
            place_1_price = place_1_price.rstrip('₸').replace(' ', '')
        if place_2_price:
            place_2_price = place_2_price.rstrip('₸').replace(' ', '')
        if place_3_price:
            place_3_price = place_3_price.rstrip('₸').replace(' ', '')
        if place_4_price:
            place_4_price = place_4_price.rstrip('₸').replace(' ', '')
        if place_5_price:
            place_5_price = place_5_price.rstrip('₸').replace(' ', '')

        cards_info.append(card_info)
        time_card_end = time.time()
        time_per_cards = time_card_start - time_card_end
        print(time_per_cards)

    driver.quit()
    print(cards_info)
    time_end = time.time()
    time_all = time_start - time_end
    print(all_count_link, time_all)
    return cards_info


def test_gecko():
    options = FirefoxOptions()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')

    browser = webdriver.Firefox(options=options)
    # browser = webdriver.Firefox()

    browser.get('http://selenium.dev/')

    browser.quit()


def test_chrome():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    options.add_argument('--start-maximized')

    browser = webdriver.Chrome(options=options)
    browser.get('http://selenium.dev/')

    version = browser.capabilities['chrome']['chromedriverVersion']
    print(f"******************************************************    ChromeDriver version: {version}")

    browser.quit()












