import os
import threading
from flask import Flask
import telebot

# ១. បង្កើត Web Server តូចមួយដើម្បីបើក Port ឱ្យ Render ដឹងថា Bot កំពុង Live
app = Flask('')

@app.route('/')
def home():
    return "Telegram Bot is running!"

def run_flask():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

# ២. កូដ Telegram Bot
TOKEN = "8497128058:AAHRuy0tSu0cfJT78cw-13a5X4qGAX95nQ0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "សួស្តី! Bot កំពុងដំណើរការស្វ័យប្រវត្តិលើ Render រួចរាល់ហើយ!")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "បញ្ជាដែលមាន៖\n/start - ចាប់ផ្តើម\n/help - ជំនួយ")

@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    text = message.text.lower()
    if "សួស្តី" in text or "hello" in text:
        bot.reply_to(message, "ជម្រាបសួរ! មានការអ្វីឱ្យខ្ញុំជួយទេ?")
    elif "តម្លៃ" in text or "price" in text:
        bot.reply_to(message, "សម្រាប់ព័ត៌មានតម្លៃ សូមទាក់ទងមកកាន់ Admin។")
    else:
        bot.reply_to(message, f"ខ្ញុំទទួលបានសារ៖ '{message.text}'")

# ៣. ដំណើការ Web Server និង Bot ព្រមគ្នា
if __name__ == '__main__':
    t = threading.Thread(target=run_flask)
    t.start()
    bot.infinity_polling()
