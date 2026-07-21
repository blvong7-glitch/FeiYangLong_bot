import telebot

# API Token របស់ Bot អ្នក
TOKEN = '8497128058:AAHRuy0tSu0cfJT78cw-13a5X4qGAX95nQ0'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "សួស្តី! Bot កំពុងដំណើរការពី Render រួចរាល់ហើយ!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"អ្នកបានផ្ញើ៖ {message.text}")

bot.infinity_polling()
