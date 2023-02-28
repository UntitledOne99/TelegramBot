import telebot
import config
import test
import Forecast
import translate
from telebot import types
from dadata import Dadata

dadata = Dadata(config.tokenDadata)
translator = translate.Translator(from_lang='russian', to_lang="english")

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     'Greetings, my friend !\nTell me your story, {0.first_name} !'.format(message.from_user,
                                                                                           bot.get_me()),
                     parse_mode='html')


@bot.message_handler(commands=['vidgets'])
def vidgets_show(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    weatherBtn = types.KeyboardButton('Weather ~')
    moneyBtn = types.KeyboardButton('Currency course $')
    geoBtn = types.KeyboardButton('Send your location', request_location=True)
    markup.add(weatherBtn, moneyBtn, geoBtn)
    bot.send_message(message.chat.id, "Let's see what I can do for you ...", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_bot(message):
    print('\n', message)
    if message.chat.type == 'private':
        if message.text == 'Weather ~':
            bot.send_message(message.chat.id, Forecast.weather())
        elif message.text == 'Currency course $':
            bot.send_message(message.chat.id, 'Money is a venom')
        else:
            bot.send_message(message.chat.id, 'Ask me about something else, wanderer')


class Geo:
    test.city = 'Minsk'
    @staticmethod
    @bot.message_handler(content_types=['location'])
    def ask_location(message):
        lon = (message.location).longitude
        lat = (message.location).latitude
        result = dadata.geolocate(name="address", lat=lat, lon=lon)
        test.city = translator.translate(((result[0])['data'])['city'])
        city = test.city
        print(test.city,city)
        return test.city


bot.polling(none_stop=True)
