from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from db_commands import connect_to_db, add_to_db, close_connection, get_all


# браузер открывает страницу и сохраняет ее содержимое в файл
def get(url, filename='index.html'):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.maximize_window()
        driver.get(url)
        sleep(3)
        with open(filename, "w", encoding='UTF-8') as file:
            file.write(driver.page_source)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


# парсим страницу с новостями Озон
def parse_ozon(filename: str, connection):
    with open(filename, encoding='UTF-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")
    news = soup.find_all(class_="news-card", limit=10)
    for i, new in enumerate(news):
        dat = new.find('span').text
        url = 'https://seller.ozon.ru' + new.find("a").get("href")
        filename = f'ozon/{i}.html'
        get(url, filename=filename)
        parse_ozon_page(filename, connection, dat)


# парсим страницу с конкретной новостью Озон
def parse_ozon_page(filename, connection, dat):
    with open(filename, encoding='UTF-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")
    title = soup.find(class_="new-top__title title_Oebvj title_Oebvj title--h1-smaller_RUef6").text.strip().replace(
        '\xa0', ' ')
    try:
        tags = soup.find(class_="page-info__topic-value").text.strip().replace(', ', '')
    except Exception:
        tags = None
    text = soup.find(class_="new-section html-content_Ol8P9").text.strip().replace('\xa0', ' ')
    source = 'ozon'
    dat = parse_date(dat)
    add_to_db(title, source, tags, text, dat, connection)


# парсим страницу с новостями Яндекс
def parse_yandex(filename, connection):
    with open(filename, encoding='UTF-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")
    news = soup.find_all(class_="news-list__item", limit=10)
    for i, new in enumerate(news):
        url = 'https://market.yandex.ru/' + new.find("a").get("href")
        filename = f'yandex/{i}.html'
        get(url, filename=filename)
        parse_yandex_page(filename, connection)


# парсим страницу с конкретной новостью Яндекс
def parse_yandex_page(filename, connection):
    with open(filename, encoding='UTF-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")
    title = soup.find(class_="news-info__title").text.strip().replace('\xa0', ' ')
    tags = soup.find(class_="news-info__tags").text.strip().replace('\xa0', ' ')
    dat = soup.find(class_='news-info__published-date').text.strip()
    dat = parse_date(dat)
    text = soup.find(class_="news-info__post-body html-content page-content").text.strip().replace('\xa0', ' ')
    source = 'yandex'
    add_to_db(title, source, tags, text, dat, connection)


def parse_date(element: str) -> str:
    d = element.split()
    d_len = len(d)
    month_dict = {
        'января': '01',
        'февраля': '02',
        'марта': '03',
        'апреля': '04',
        'мая': '05',
        'июня': '06',
        'июля': '07',
        'августа': '08',
        'сентября': '09',
        'октября': '10',
        'ноября': '11',
        'декабря': '12',
    }
    d[1] = month_dict[d[1]]
    if int(d[0]) < 10:
        d[0] = '0' + d[0]
    d = d[::-1]
    dat = '-'.join(d)
    if d_len == 2:
        dat = '2022-' + dat
    return dat


def main():
    site_ozon = 'https://seller.ozon.ru/news/'
    site_yandex = 'https://market.yandex.ru/partners/news'
    connection = connect_to_db()
    get(site_ozon, filename='ozon.html')
    get(site_yandex, filename='yandex.html')
    parse_ozon('ozon.html', connection)
    parse_yandex('yandex.html', connection)
    get_all(connection)
    close_connection(connection)


if __name__ == '__main__':
    main()
