import asyncio
from pyppeteer import launch

async def get_all_links(url):
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto(url)

    try:
        wait_info = await page.waitForSelector('#ItemView > div.item > div > div.item__inner-right > div > div:nth-child(1) > div.item__price > div.item__price-left-side > div.item__price-once')
        print(await page.evaluate('(element) => element.textContent', wait_info))

    except Exception as e:
        print("Произошла ошибка:", str(e))

    finally:
        await browser.close()

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

    # Используем asyncio.gather для параллельного выполнения запросов
    tasks = [get_all_links(url) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
