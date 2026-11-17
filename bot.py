import telebot

TOKEN = 
9035247122:AAE0l3rm1TRnNDzXmXUimzol8aCETxznQ10
bot = telebot.TeleBot

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! Bot chalu hoye geche")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, f"Tumi bolcho: {message.text}")

print("Bot chalu...")
bot.polling()
