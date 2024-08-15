from loader import bot, db
from telebot.types import ReplyKeyboardRemove
from keyboards.default import admin_btn
from state import ProductState
from keyboards.inline import delete_category_btn, delete_product_btn

from config import ADMINS

from telebot.types import Message



@bot.message_handler(chat_id=ADMINS ,func=lambda message: message.text == "Foydalanuvchilar soni 👤")
def reaction_users_count(message: Message):
    chat_id = message.chat.id
    users = db.get_users()[0][0]
    bot.send_message(chat_id, f"Hozirgi vaqtdagi foydalanuvchilar soni: {users} ta")


@bot.message_handler(chat_id=ADMINS, func=lambda message: message.text == "Foydalunvchilarga e'lon 📢")
def reaction_ad(message: Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "Jo'natish kerak bo'lgan ma'lumotni kiriting!", reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg,repost)


def repost(message: Message):
    chat_id = message.chat.id
    users_count = db.get_users()[0][0]
    users = db.get_users_id()[0][0]
    iterator = 0
    error = 0
    try:
        for user in users:
            bot.copy_message(user[0], chat_id, message.id)
        iterator += 1
    except:
        error +=1

    for admin in ADMINS:
        bot.send_message(admin, f"Jo'natildi {iterator} / {users_count},"
                                f"Muammolar bo'ldi {error}", reply_markup=admin_btn())

@bot.message_handler(chat_id=ADMINS, func=lambda message: message.text == "Kategoriyalar qo'shish")
def reaction_add_category(message: Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "Kategoriyani nomini kiriting", reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, add_category)


def add_category(message: Message):
    chat_id = message.chat.id
    category = message.text.capitalize()
    db.insert_category(category)
    bot.send_message(chat_id, "Qo'shildi", reply_markup=admin_btn())


@bot.message_handler(chat_id=ADMINS, func=lambda message: message.text == "Mahsulot qo'shish")
def reaction_add_product(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    bot.set_state(user_id, ProductState.product_name, chat_id)
    bot.send_message(chat_id, "Mahsulotni nomini kiriting", reply_markup=ReplyKeyboardRemove())

@bot.message_handler(chat_id=ADMINS, content_types=['text'],state=ProductState.product_name)
def product_name(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    with bot.retrieve_data(user_id, chat_id) as data:
        data['product_name']  = message.text.capitalize()
    bot.set_state(user_id, ProductState.price, chat_id)
    bot.send_message(chat_id, "Mahsulot narxini kiriting")

@bot.message_handler(chat_id=ADMINS, content_types=['text'], state=ProductState.price)
def product_price(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    with bot.retrieve_data(user_id, chat_id) as data:
        data['price'] = message.text
    bot.set_state(user_id, ProductState.image, chat_id)
    bot.send_message(chat_id, "Mahsulot rasmini kiriting!", reply_markup=ReplyKeyboardRemove())

@bot.message_handler(chat_id=ADMINS, content_types=['text'], state=ProductState.image)
def product_image(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    with bot.retrieve_data(user_id, chat_id) as data:
        data['image'] = message.text.capitalize()
    bot.set_state(user_id, ProductState.category, chat_id)
    bot.send_message(chat_id, "Mahsulot kategoriyasini kiriting!", reply_markup=ReplyKeyboardRemove())

@bot.message_handler(chat_id=ADMINS, content_types=['text'], state=ProductState.category)
def product_category(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    with bot.retrieve_data(user_id, chat_id) as data:
        product_name = data['product_name']
        price = data['price']
        image = data['image']
        category = message.text.capitalize()
    category_id = db.return_category_id(category)
    db.insert_product(product_name, price, image, category_id)
    bot.delete_state(user_id, chat_id)
    bot.send_message(chat_id, "Mahsulot qo'shildi", reply_markup=admin_btn())




@bot.message_handler(chat_id=ADMINS, func=lambda message: message.text == "Kategoriyalar o'chirish")
def reaction_del_category(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Kategoriyani tanlang", reply_markup=delete_category_btn(db.get_category_del()))


@bot.message_handler(chat_id=ADMINS, func=lambda message: message.text == "Mahsulot o'chirish")
def reaction_del_product(message:Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Mahsulotni tanlang", reply_markup=delete_product_btn(db.get_products_by_delete()))














