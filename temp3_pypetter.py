import asyncio
from pyppeteer import launch

async def get_data(url):
    browser = await launch()
    page = await browser.newPage()

    # Добавляем заголовки
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        # Добавьте любые другие нужные заголовки
    }
    await page.setExtraHTTPHeaders(headers)

    await page.goto(url)

    # Дождемся, пока данные загрузятся (это может потребовать дополнительных действий)
    # В данном случае, мы просто ждем 5 секунд, вы можете настроить это под вашу ситуацию.
    await asyncio.sleep(5)

    # Получим содержимое страницы
    data = await page.content()

    await browser.close()

    return data

async def main():
    url = 'https://kaspi.kz/shop/p/ekt-provod-shvvp-2x0-5-1-m-100983861/?c=710000000'
    result = await get_data(url)
    print(result)

if __name__ == '__main__':
    asyncio.run(main())
