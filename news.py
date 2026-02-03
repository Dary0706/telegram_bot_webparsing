import requests
import text

def image_www(url):
    name = url.split('/')[-1]
    r = requests.get(url, allow_redirects=True)
    open(name, 'wb').write(r.content)

def image_name(url):
    name = url.split('/')[-1]
    return name


def final_news(paper_h, paper_div):
    if paper_div == None:
        news_paper = f'<b>🚨{paper_h}!</b>'
        return news_paper
    else:
        a = text.pipiska(paper_div, limit=800)
        b = f'<b>🚨{paper_h}!</b>'
        news_paper = f'\n\n<a href="https://t.me/EveHnews">🫐ЕжеНьюс | Новости</a>\n\n✍{a}\n\n#Новости #ВесьМир #ЕжеНьюс'
        c = b + news_paper
        return c











