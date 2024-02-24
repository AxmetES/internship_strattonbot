import telebot
from telebot import types

from config import settings
import crud

bot = telebot.TeleBot(settings.BOT_TOKEN)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    if 'Strattonbot' in message.text:
        crud.insert_message(message.text, message.json['date'])
        bot.send_message(message.chat.id, message.text)


if __name__ == "__main__":
    crud.create_table()
    bot.infinity_polling()
