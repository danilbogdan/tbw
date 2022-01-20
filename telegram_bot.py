'''
{
   "coord":{
      "lon":-0.1257,
      "lat":51.5085
   },
   "weather":[
      {
         "id":804,
         "main":"Clouds",
         "description":"overcast clouds",
         "icon":"04d"
      }
   ],
   "base":"stations",
   "main":{
      "temp":40.87,
      "feelslike":35.06,
      "tempmin":38.7,
      "temp_max":42.98,
      "pressure":1037,
      "humidity":64
   },
   "visibility":10000,
   "wind":{
      "speed":9.22,
      "deg":330
   },
   "clouds":{
      "all":90
   },
   "dt":1642691408,
   "sys":{
      "type":2,
      "id":2019646,
      "country":"GB",
      "sunrise":1642665284,
      "sunset":1642696071
   },
   "timezone":0,
   "id":2643743,
   "name":"London",
   "cod":200
}

WEATHER_API_KEY = '5b642e1561mshe54d684b73ad18bp1121c4jsn79cf637b53a1'
'''

import requests
import telebot
from telebot import types

bot = telebot.TeleBot('5187725132:AAFHfAToPnKkCyeo0G43FuiZajpkMVZFxhM')
WEATHER_API_KEY = '5b642e1561mshe54d684b73ad18bp1121c4jsn79cf637b53a1'


@bot.message_handler(commands=['start', 'help'])
def handle_start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_weather = types.KeyboardButton(text='Узнать погоду', request_location=True)
    keyboard.add(button_weather)

    command_weather = types.BotCommand('weather', 'Get weather for Sievierodonetsk')
    bot.set_my_commands(commands=[command_weather])

    bot.send_message(message.chat.id, 'Привет! Нажми на кнопку или , чтобы я мог узнать погоду для тебя.',
                     reply_markup=keyboard)


if __name__ == '__main__':
    bot.infinity_polling()
