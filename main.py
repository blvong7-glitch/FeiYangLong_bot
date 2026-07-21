import os
import threading
from flask import Flask
import telebot

# 1. បង្កើត Web Server តូចមួយសម្រាប់ Render (ការពារ Timed Out)
app = Flask('')

@app.route('/')
def home():
    return "Bot is running online!"

def run_flask():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

# 2. Telegram Bot Configuration
TOKEN = "8497128058:AAHRuy0tSu0cfJT78cw-13a5X4qGAX95nQ0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "សួស្តី! ខ្ញុំជា Bot ស្វ័យប្រវត្តិ។ តើអ្នកត្រូវការឱ្យខ្ញុំជួយអ្វីដែរ?")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "អ្នកអាចប្រើប្រាស់បញ្ជាដូចខាងក្រោម៖\n/start - ចាប់ផ្តើម\n/help - ជំនួយ")

@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    text = message.text.lower()
    if "សួស្តី" in text or "hello" in text:
        bot.reply_to(message, "ជម្រាបសួរ! មានការអ្វីឱ្យខ្ញុំជួយទេ?")
    elif "តម្លៃ" in text or "price" in text:
        bot.reply_to(message, "សម្រាប់ព័ត៌មានតម្លៃ សូមទាក់ទងមកកាន់ Admin។")
    else:
        bot.reply_to(message, f"ខ្ញុំទទួលបានសាររបស់អ្នកហើយ៖ '{message.text}'")

# 3. ដំណើការ Web Server និង Bot ក្នុងពេលតែមួយ
if __name__ == '__main__':
    # រត់ Web Server លើ Thread ដាច់ដោយឡែក
    t = threading.Thread(target=run_flask)
    t.start()
    
    # រត់ Telegram Bot Polling
    bot.infinity_polling()
