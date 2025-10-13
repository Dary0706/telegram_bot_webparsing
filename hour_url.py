import requests
from bs4 import BeautifulSoup

def take_url_hr():
    url = "https://rg.ru/news.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "lxml")

    ls = list()

    for news in soup.find_all('a'):
        a = news.get('href')
        ls.append(a)

    url_list = list()

    for nopolitics in ls:
        c = str(nopolitics)
        if c[0:3] == '/20':
            nedo_url = nopolitics
            base_url = 'https://rg.ru' + nedo_url
            url_list.append(base_url)
    return url_list


