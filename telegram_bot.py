import telebot
from telebot import types
import requests

# https://rapidapi.com/community/api/open-weather-map/


bot = telebot.TeleBot("5017425940:AAEW7c0gjuZFfDXYcYxRDT-90qvk9CSMYlU")



def get_current_weather(location):
	url = "https://community-open-weather-map.p.rapidapi.com/weather"

	querystring = {"lat":str(location[0]),"lon":str(location[1]),"lang":"ua", "units": "metric"}

	headers = {
	    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
	    'x-rapidapi-key': "5b642e1561mshe54d684b73ad18bp1121c4jsn79cf637b53a1"
	    }

	response = requests.request("GET", url, headers=headers, params=querystring)
	return response.json()


def format_weather(weather):
	return f'''
	{weather["weather"][0]["description"]}

	Температура: {weather["main"]["temp"]}
	Скорость ветра: {weather["wind"]["speed"]}

	'''

@bot.message_handler(commands=["weather"])
def request_weather(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и передай мне свое местоположение", reply_markup=keyboard)


@bot.message_handler(content_types=["location"])
def send_weather(message):
	if message.location is not None:
		location = (message.location.latitude, message.location.longitude)
	else:
		location = (0, 0)
	raw_weather = get_current_weather(location)
	bot.reply_to(message, format_weather(raw_weather))


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


if __name__ == '__main__':
	bot.infinity_polling()