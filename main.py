import telebot

bot = telebot.TeleBot("1534183615:AAHSWVl5i2ccUEaoHUzZ69YoR-g-_KJhbSA")

@bot.message_handler(commands=['start', 'help'])

def send_welcome(message):

bot.reply_to(message, "Hello! I'm Android Wedakarayo Test Bot. How can I help you?")


@bot.message_handler(commands=['test'])

def start_message(message):  

bot.reply_to(message, "It's working!")


bot.polling()
