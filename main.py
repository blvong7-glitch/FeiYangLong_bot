import os
import telebot

# ទាញយក Token របស់ Bot
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # ឬប្រើ os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# 1. ស្វ័យប្រវត្តិ៖ ឆ្លើយតបពេលចុច /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "សួស្តី! ខ្ញុំជា Bot ស្វ័យប្រវត្តិ។ តើអ្នកត្រូវការឱ្យខ្ញុំជួយអ្វីដែរ?")

# 2. ស្វ័យប្រវត្តិ៖ ឆ្លើយតបពេលចុច /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "អ្នកអាចប្រើប្រាស់បញ្ជាដូចខាងក្រោម៖\n/start - ចាប់ផ្តើម\n/help - ជំនួយ")

# 3. ស្វ័យប្រវត្តិ៖ ឆ្លើយតបតាមពាក្យគន្លឹះ (Keywords)
@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    text = message.text.lower()
    
    if "សួស្តី" in text or "hello" in text:
        bot.reply_to(message, "ជម្រាបសួរ! មានការអ្វីឱ្យខ្ញុំជួយទេ?")
    elif "តម្លៃ" in text or "price" in text:
        bot.reply_to(message, "សម្រាប់ព័ត៌មានតម្លៃ សូមទាក់ទងមកកាន់ Admin។")
    else:
        bot.reply_to(message, f"ខ្ញុំទទួលបានសាររបស់អ្នកហើយ៖ '{message.text}'")

# រត់ Bot ឱ្យធ្វើការរហូត
bot.infinity_polling()
