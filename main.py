import telebot

bot = telebot.TeleBot("1604055296:AAGZ_M52cLbaTh16CqaJrkw0VEZuwcCmFc0")


@bot.message_handler(commands=['test'])
def start_message(message):  
                           bot.reply_to(message, "It's working!")
bot.polling()
