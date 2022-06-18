import telebot

bot = telebot.TeleBot('5451551928:AAER8On_vvEBZKkxwgr6lmJ_r_LQIVrX9Ng')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Добро пожаловать в stories</b>', parse_mode='html')


bot.polling(none_stop=True)




