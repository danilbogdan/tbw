import requests
import telebot
from telebot import types

WEATHER_API_KEY = '5b642e1561mshe54d684b73ad18bp1121c4jsn79cf637b53a1'
TELEGRAM_BOT_TOKEN = ''


bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def handle_start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_weather = types.KeyboardButton(text='Узнать погоду', request_location=True)
    keyboard.add(button_weather)

    command_weather = types.BotCommand('weather', 'Get weather for Sievierodonetsk')
    bot.set_my_commands(commands=[command_weather])

    bot.send_message(message.chat.id, 
                     '''Привет! Нажми на кнопку, чтобы я мог узнать погоду для твоего местоположения 
                     или отправь команду /weather, чтобы узнать погоду в Северодонецке.''',
                     reply_markup=keyboard)


if __name__ == '__main__':
    bot.infinity_polling()
