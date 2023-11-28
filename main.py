import telebot

bot = telebot.TeleBot('6946647890:AAHu0gOQ38bVN4ErXCGUrX9i_4837SJYCnQ')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     'Привет! Вот, какую музыку я могу предложить:\nНажми /guitar, чтобы послушать гитару \nНажми /guqin, чтобы послушать гуцинь \nНажми /piano, чтобы послушать пианино \nНажми /flute, чтобы послушать флейту',
                     parse_mode='Markdown')


@bot.message_handler(commands=['guitar'])
def main(message):
    bot.send_message(message.chat.id, '[гитара](https://youtu.be/NwQjTNdRvDA?si=T78IWbOfDApxIfiB)',
                     parse_mode='Markdown')


@bot.message_handler(commands=['guqin'])
def main(message):
    bot.send_message(message.chat.id, '[гуцинь](https://youtu.be/VOBkbW2gRRU?si=6oIza_VHMTndI6wb)',
                     parse_mode='Markdown')


@bot.message_handler(commands=['piano'])
def main(message):
    bot.send_message(message.chat.id, '[пианино](https://youtu.be/gSY-wD4l5DM?si=aJJbS4GonpsKWOnD)',
                     parse_mode='Markdown')


@bot.message_handler(commands=['flute'])
def main(message):
    bot.send_message(message.chat.id, '[флейта](https://youtu.be/0D22PcN9Wds?si=Gvfr0jtdyum733WL)',
                     parse_mode='Markdown')


bot.infinity_polling()