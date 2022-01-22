import requests
import telebot
from telebot import types

WEATHER_API_KEY = '5b642e1561mshe54d684b73ad18bp1121c4jsn79cf637b53a1'
TELEGRAM_BOT_TOKEN = '5183862802:AAGKOmPEalqEuBUt7ze9SYzJvRUPo-153AM'


bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


def get_current_weather(location):
    url = 'https://community-open-weather-map.p.rapidapi.com/weather'

    querystring = {'lat': str(location[0]), 'lon': str(location[1]), 'lang': 'ua', 'units': 'metric'}

    headers = {
        'x-rapidapi-host': 'community-open-weather-map.p.rapidapi.com',
        'x-rapidapi-key': WEATHER_API_KEY
    }

    response = requests.request('GET', url, headers=headers, params=querystring)
    return response.json()


def format_weather(weather):
    return f'''
    {weather['weather'][0]['description']}

    Температура: {weather['main']['temp']}°
    Швидкість вітру: {weather['wind']['speed']}
    '''


def get_icon_url(weather):
    return f'https://openweathermap.org/img/wn/{weather["weather"][0]["icon"]}@4x.png'


@bot.message_handler(commands=['start', 'help'])
def handle_start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_weather = types.KeyboardButton(text='Узнать погоду', request_location=True)
    keyboard.add(button_weather)

    command_weather = types.BotCommand('weather', 'Get weather for Sievierodonetsk')
    bot.set_my_commands(commands=[command_weather])

    bot.send_message(message.chat.id, 'Привет! Нажми на кнопку или , чтобы я мог узнать погоду для тебя.',
                     reply_markup=keyboard)


@bot.message_handler(content_types=['location'])
def handle_location(message):
    location = (message.location.latitude, message.location.longitude)
    raw_weather = get_current_weather(location)
    bot.send_photo(message.chat.id, get_icon_url(raw_weather), format_weather(raw_weather))


@bot.message_handler(commands=['weather'])
def handle_weather_for_sievier(message):
    location = (48.9483, 38.4917)
    raw_weather = get_current_weather(location)
    bot.send_photo(message.chat.id, get_icon_url(raw_weather), format_weather(raw_weather))


if __name__ == '__main__':
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
    bot.infinity_polling()
