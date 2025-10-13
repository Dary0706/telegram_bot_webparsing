import requests
from bs4 import BeautifulSoup
import time


def get_h1_hr(news_url):
    url = news_url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "lxml")

    h1 = soup.h1.string
    return h1


def get_div_hr(news_url):
    url = news_url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "lxml")

    a = soup.find('div', 'PageContentCommonStyling_text__CKOzO')
    if a == None:
        return None
    else:
        div = a.getText()
        return div


def get_img_hr(news_url):
    url = news_url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    r = requests.get(url, headers=headers)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, "lxml")

    pic = soup.find('img', class_='PageArticleContent_imageSrc__54iUt')
    if pic:
        image = pic.get('src')
        return image
    else:
        return None

