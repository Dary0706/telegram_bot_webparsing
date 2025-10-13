import requests
import text

def image_www(url):
    name = url.split('/')[-1]
    r = requests.get(url, allow_redirects=True)
    open(name, 'wb').write(r.content)
    # time.sleep(45)

def image_name(url):
    name = url.split('/')[-1]
    return name


def final_news(paper_h, paper_div):
    a = text.pipiska(paper_div, limit=1024)
    if paper_div == None:
        news_paper = f'<b>🚨{paper_h}!</b>'
        return news_paper
    else:
        news_paper = f'<b>🚨{paper_h}!</b> \n\n✍{a}'
        return news_paper




