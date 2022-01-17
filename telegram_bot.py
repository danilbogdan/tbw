import telebot
import requests

# https://rapidapi.com/community/api/open-weather-map/


bot = telebot.TeleBot("5017425940:AAEW7c0gjuZFfDXYcYxRDT-90qvk9CSMYlU")



def get_weather():
	url = "https://community-open-weather-map.p.rapidapi.com/weather"

	querystring = {"lat":"0","lon":"0","lang":"ua", "units": "metric"}

	headers = {
	    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
	    'x-rapidapi-key': "5b642e1561mshe54d684b73ad18bp1121c4jsn79cf637b53a1"
	    }

	response = requests.request("GET", url, headers=headers, params=querystring)

	return response.text


def format_weather(weather):
	return f'''
	{weather["weather"][0]["description"]}

	Температура: {weather["weather"][0]["main"]["temp"]}
	Скорость ветра: {weather["weather"][0]["main"]["wind"]["speed"]}

	'''


@bot.message_handler(commands=['weather'])
def send_weather(message):
	raw_weather = get_weather()
	bot.reply_to(message, format_weather(raw_weather))


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


if __name__ == '__main__':
	bot.infinity_polling()