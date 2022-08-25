from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# браузер открывает страницу и сохраняет ее содержимое в файл
def get(url, filename='index.html'):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.maximize_window()
        driver.get(url)
        sleep(3)
        with open(filename, "w") as file:
            file.write(driver.page_source)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


# парсим страницу с новостями Озон
def parse_ozon(filename: str):
    with open(filename) as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")
    news = soup.find_all(class_="news-card", limit=10)
    for i, new in enumerate(news):
        items = new.find(class_="news-card__content")
        raw = list(map(str.strip, items.text.strip().split('\n')))
        title = raw[0]
        if len(raw) == 2:
            tags = raw[1]
        else:
            tags = None
        url = 'https://seller.ozon.ru' + new.find("a").get("href")
        filename = f'{i}ozon.html'
        get(url, filename=filename)
        text_of_new = parse_ozon_page(filename)


# парсим страницу с конкретной новостью Озон
def parse_ozon_page(filename):
    with open(filename) as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")
    new = soup.find(class_="new-section html-content_Ol8P9")
    return new.text


# парсим страницу с новостями Яндекс
def parse_yandex(filename):
    with open(filename) as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")
    news = soup.find_all(class_="news-list__item", limit=10)
    for i, new in enumerate(news):
        url = 'https://market.yandex.ru/' + new.find("a").get("href")
        filename = f'{i}yandex.html'
        get(url, filename=filename)
        parse_yandex_page(filename)


# парсим страницу с конкретной новостью Яндекс
def parse_yandex_page(filename):
    with open(filename) as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")
    title = soup.find(class_="news-info__title").text
    tags = soup.find(class_="news-info__tags").text
    text = soup.find(class_="news-info__post-body html-content page-content").text
    return title, tags, text


def main():
    site_ozon = 'https://seller.ozon.ru/news/'
    site_yandex = 'https://market.yandex.ru/partners/news'
    get(site_ozon, filename='ozon.html')
    get(site_yandex, filename='yandex.html')
    parse_ozon('ozon.html')
    parse_yandex('yandex.html')


if __name__ == '__main__':
    main()