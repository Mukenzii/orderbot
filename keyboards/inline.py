from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import db


def order_btn(product_list):
    markup = InlineKeyboardMarkup()
    for item in product_list:
        markup.add(InlineKeyboardButton(item[0], callback_data=f"categories|{item[0]}"))
    markup.row(InlineKeyboardButton('⬅️ Asosiy Menyu', callback_data='back_menu'))
    return markup


def products_add_btn(product):
    markup = InlineKeyboardMarkup()
    for item in product:
        markup.add(InlineKeyboardButton(item[1], callback_data=f"product|{item[0]}"))
    markup.row(InlineKeyboardButton('Orqaga 🔙', callback_data=f'back_cat'))
    return markup


def product_count(category_id):
    markup = InlineKeyboardMarkup(row_width=3)
    markup.add(InlineKeyboardButton("1", callback_data=f'page|1'),
               InlineKeyboardButton("2", callback_data=f'page|2'),
               InlineKeyboardButton("3", callback_data=f'page|3'),
               InlineKeyboardButton("4", callback_data=f'page|4'),
               InlineKeyboardButton("5", callback_data=f'page|5'),
               InlineKeyboardButton("6", callback_data=f'page|6'),
               InlineKeyboardButton("7", callback_data=f'page|7'),
               InlineKeyboardButton("8", callback_data=f'page|8'),
               InlineKeyboardButton("9", callback_data=f'page|9'))

    markup.row(InlineKeyboardButton("Orqaga 🔙", callback_data=f"back_cat|{category_id}"))
    return markup


def get_count(category_id,page,product_id):
    items = [
        InlineKeyboardButton('➖', callback_data='minus'),
        InlineKeyboardButton(page, callback_data=f'quantity|{page}'),
        InlineKeyboardButton('➕', callback_data='plus')
    ]
    card = InlineKeyboardButton("Savat 🛒", callback_data='show_card')
    back_cat = InlineKeyboardButton('Ortga 🔙', callback_data=f'back_cat|{category_id}')
    add_card = InlineKeyboardButton("Savatga qo'shish 🛒", callback_data=f'add_card|{product_id}')


    return InlineKeyboardMarkup(keyboard=[
        items,
        [card, add_card],
        [back_cat]
    ])


def card_btns(data: dict):
    markup = InlineKeyboardMarkup(row_width=1)
    for product_name, items in data.items():
        product_id = items['product_id']
        markup.add(InlineKeyboardButton(f"❌ {product_name}", callback_data=f'remove|{product_id}'))
    markup.row(
        InlineKeyboardButton('Tozalash ♻️', callback_data='clear'),
        InlineKeyboardButton('Tasdiqlash ✅', callback_data='submit'))
    markup.add(InlineKeyboardButton('Kategoriyalar', callback_data='back_cat'))
    return markup


def payment_btn():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Naqd 💵', callback_data='payment|1'),
               InlineKeyboardButton('Click 💳', callback_data='payment|2'),
               InlineKeyboardButton("Payme 💳", callback_data='payment|3'))

    return markup


def delete_category_btn(category_list):
    markup = InlineKeyboardMarkup()
    for item in category_list:
        markup.add(InlineKeyboardButton(item[0], callback_data=f"del_category|{item[1]}"))
    return markup

def delete_product_btn(product_list):
    markup = InlineKeyboardMarkup()
    for item in product_list:
        markup.add(InlineKeyboardButton(item[0], callback_data=f'del_product|{item[1]}'))

    return markup



