import telebot
from telebot import types
import news
import hour_url, hour_html
import time

token = '7917086296:AAF81AE2Q8eHQujDN-AnjsB-gZ_8npo-ohg'
bot = telebot.TeleBot(token)

ID = -1003107332060


@bot.message_handler(commands=['start'])
def hi(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Запуск!', callback_data='send_news'))
    bot.send_message(message.chat.id, f'Здравствуйте {message.from_user.first_name}! Начнём запуск новостей?', reply_markup=markup)


@bot.message_handler(commands=['send_news'])
def send_news(message):
    hr_magazine = hour_url.take_url_hr()
    hr_paper_h = hour_html.get_h1_hr(hr_magazine[6])
    hr_paper_div = hour_html.get_div_hr(hr_magazine[6])
    hr_paper_img = hour_html.get_img_hr(hr_magazine[6])

    hr_paper = news.final_news(hr_paper_h, hr_paper_div)

    if hr_paper_img == None:
        file3 = open(f'./rupor.jpg', 'rb')
        bot.send_photo(ID, file3, caption=f'{hr_paper}', parse_mode='html')
    else:
        news.image_www(hr_paper_img)
        c = news.image_name(hr_paper_img)
        print(c)
        file3 = open(f'./{c}', 'rb')
        bot.send_photo(ID, file3, caption=f'{hr_paper}', parse_mode='html')


@bot.message_handler(commands=['last_ten'])
def lt(message):
    ck = 0
    while ck != 10:
        hr_magazine = hour_url.take_url_hr()
        hr_paper_h = hour_html.get_h1_hr(hr_magazine[ck])
        hr_paper_div = hour_html.get_div_hr(hr_magazine[ck])
        hr_paper_img = hour_html.get_img_hr(hr_magazine[ck])

        hr_paper = news.final_news(hr_paper_h, hr_paper_div)


        if hr_paper_img == None:
            file = open(f'./rupor.jpg', 'rb')
            bot.send_photo(message.chat.id, file, caption=f'{hr_paper}', parse_mode='html')
        else:
            news.image_www(hr_paper_img)
            c = news.image_name(hr_paper_img)
            print(c)
            file3 = open(f'./{c}', 'rb')
            bot.send_photo(message.chat.id, file3, caption=f'{hr_paper}', parse_mode='html')
        ck += 1


@bot.message_handler(commands=['pre_post_news'])
def post_news(message):
    while True:
        hr_magazine = hour_url.take_url_hr()
        hr_paper_h = hour_html.get_h1_hr(hr_magazine[0])
        hr_paper_div = hour_html.get_div_hr(hr_magazine[0])
        hr_paper_img = hour_html.get_img_hr(hr_magazine[0])

        hr_paper = news.final_news(hr_paper_h, hr_paper_div)

        if hr_paper_img == None:
            file3 = open(f'./rupor.jpg', 'rb')
            bot.send_photo(ID, file3, caption=f'{hr_paper}', parse_mode='html')
        else:
            news.image_www(hr_paper_img)
            c = news.image_name(hr_paper_img)
            print(c)
            file3 = open(f'./{c}', 'rb')
            bot.send_photo(ID, file3, caption=f'{hr_paper}', parse_mode='html')
        time.sleep(1200)


@bot.callback_query_handler(func=lambda callback: True)
def callback_news(callback):
    while True:
        hr_magazine = hour_url.take_url_hr()
        hr_paper_h = hour_html.get_h1_hr(hr_magazine[0])
        hr_paper_div = hour_html.get_div_hr(hr_magazine[0])
        hr_paper_img = hour_html.get_img_hr(hr_magazine[0])

        hr_paper = news.final_news(hr_paper_h, hr_paper_div)

        if hr_paper_img == None:
            file3 = open(f'./rupor.jpg', 'rb')
            bot.send_photo(ID, file3, caption=f'{hr_paper}', parse_mode='html')
        else:
            news.image_www(hr_paper_img)
            c = news.image_name(hr_paper_img)
            print(c)
            file3 = open(f'./{c}', 'rb')
            bot.send_photo(ID, file3, caption=f'{hr_paper}', parse_mode='html')
        time.sleep(1200)

bot.polling(none_stop=True)