from loader import bot
from config import ADMINS
from telebot.types import Message
from keyboards.default import admin_btn


@bot.message_handler(chat_id=ADMINS, commands=['start'])
def reaction_start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Salom Admin!', reply_markup=admin_btn())








