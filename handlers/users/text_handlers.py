from loader import bot, db
from telebot.types import Message, CallbackQuery
from keyboards.default import *
from keyboards.inline import products_add_btn, order_btn
from state import RegisterState
import re



@bot.message_handler(func=lambda message: message.text == 'Buyurtma Berish 📝')
def reaction_order(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    result = db.check_user_id(user_id)
    if None in result:
        bot.send_message(chat_id, "Siz ro'yxatdan o'tmagansiz!", reply_markup=register_btn())
    else:
        bot.delete_message(chat_id, message.id)
        bot.send_message(chat_id, '⏳', reply_markup=ReplyKeyboardRemove())
        bot.send_message(chat_id, "Buyurtmani birga joylashtiramizmi? 🤗", reply_markup=order_btn(db.get_categories()))

@bot.message_handler(func=lambda message: message.text == "Ro'yxatdan o'tish✏️")
def reaction_register(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    bot.set_state(user_id, RegisterState.full_name, chat_id)
    bot.send_message(chat_id, "Ismingizni kiriting", reply_markup=ReplyKeyboardRemove())


@bot.message_handler(content_types=['text'], state=RegisterState.full_name)
def reaction_full_name(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    with bot.retrieve_data(chat_id, user_id) as data:
        if ' ' in message.text:
            data['full_name'] = ' '.join([item.capitalize() for item in message.text.split(' ')])
        else:
            data['full_name'] = message.text.capitalize()
    bot.set_state(user_id, RegisterState.contact, chat_id)
    bot.send_message(chat_id, "Kontaktingizni kiriting!", reply_markup=send_contact())


@bot.message_handler(content_types=['text', 'contact'], state=RegisterState.contact)
def reaction_contact(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    with bot.retrieve_data(user_id, chat_id) as data:
        if message.contact:
            data['contact'] = message.contact.phone_number
            bot.set_state(user_id, RegisterState.submit, chat_id)
            bot.send_message(chat_id, "Ma'lumotlar to'g'rimi?",reply_markup=submit_btn())
        else:
            if ' ' in message.text and '-' in message.text:
                number = message.text.replace(' ', '')
                number = number.replace('-', '')
            elif '-' in message.text:
                number = message.text.replace('-', '')
            elif ' ' in message.text:
                number = message.text.replace(' ', '')
            else:
                number = message.text

            if re.match(r"^(\+998)?(88|33|9(3|4|7|0|9))\d{7}$", number):
                data['contact'] = number
                bot.set_state(user_id, RegisterState.submit, chat_id)
                bot.send_message(chat_id, "Ma'lumotlarni tasdiqlaysizmi?",
                                 reply_markup=submit_btn())
            else:
                bot.send_message(chat_id, "Kontaktingiz noto'g'ri qaytadan kiriting!",
                                 reply_markup=send_contact())


@bot.message_handler(content_types=['text'], state=RegisterState.submit)
def reaction_submit(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if message.text == "Ha":
        with bot.retrieve_data(user_id, chat_id) as data:
            name = data['full_name'],
            contact = data['contact']
            db.save_user(name, contact, user_id)
            bot.send_message(chat_id, "Saqlandi", reply_markup=main_btns())
        bot.delete_state(chat_id, user_id)
    else:
        bot.set_state(user_id, RegisterState.full_name, chat_id)
        bot.send_message(chat_id, "Ism familyangizni qaytadan kiriting!",reply_markup=ReplyKeyboardRemove())


@bot.message_handler(func=lambda message: message.text == 'Aloqa uchun ☎️')
def reaction_contact(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, '☎️Aloqa uchun: +998999999999')


@bot.message_handler(func=lambda message: message.text == 'Bizning filiallarimiz 📍')
def reaction_location(message: Message):
    bot.send_message(message.chat.id, "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."
                                      "There is no one who loves pain itself, who seeks after it and wants to have it,"
                                      "simply because it is pain...")








