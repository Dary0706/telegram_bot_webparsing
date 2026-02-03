import requests
from bs4 import BeautifulSoup
import time


def get_h1_hr(news_url):
    url = news_url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    r = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(r.content, "lxml")

    h1 = soup.h1.text[21:][:-17]
    return h1


def get_div_hr(news_url):
    url = news_url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    r = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(r.content, "lxml")

    a = soup.find('div', 'article__text')
    if a == None:
        return None
    else:
        div = a.getText()
        c = div.replace("rbc.group", "")
        return c


def get_img_hr(news_url):
    url = news_url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    r = requests.get(url, headers=headers, timeout=10)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, "lxml")

    pic = soup.find('div', {'class': 'article__text'})
    if pic:
        # Внутри этого div ищем тег img
        img_tag = pic.find('img')
        if img_tag and 'src' in img_tag.attrs:
            return img_tag['src']
    else:
        return None


# print(get_h1_hr('https://www.rbc.ru/politics/02/02/2026/6980715f9a7947842d201087?from=short_news'))
# print(get_div_hr('https://www.rbc.ru/education/02/02/2026/69788fc09a7947ce394ffb20?from=short_news'))
# print(get_img_hr('https://www.rbc.ru/rbcfreenews/698099409a7947249771c0d9?from=short_news'))
