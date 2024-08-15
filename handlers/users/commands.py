from telebot.types import Message
from loader import bot, db
from keyboards.default import main_btns

@bot.message_handler(commands=['start'])
def reaction_start(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    db.insert_user_tg(user_id)
    bot.send_message(chat_id, "Assalomualeykum Dostavka botimizga Xush kelibsiz!🤗",
                     reply_markup=main_btns())


