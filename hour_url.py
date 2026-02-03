import requests
from bs4 import BeautifulSoup

def take_url_hr():
    url = "https://www.rbc.ru/short_news"
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

    a = ls[2][-9:]

    for url in ls:
        c = str(url)
        if c[-10:] == 'short_news':
            url_list.append(c)
    return url_list

# print(take_url_hr())

