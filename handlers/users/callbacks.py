from loader import bot
from telebot.types import CallbackQuery
from keyboards.inline import *
from keyboards.default import main_btns
from state import CardState


@bot.callback_query_handler(func=lambda call: 'categories' in call.data)
def reaction_categories(call: CallbackQuery):
    chat_id = call.message.chat.id
    category = call.data.split('|')[1]
    product = db.get_product_by_category(category)
    bot.delete_message(chat_id, call.message.id)
    bot.send_message(chat_id, category, reply_markup=products_add_btn(product))


@bot.callback_query_handler(func=lambda call: 'back_menu' in call.data)
def reaction_back_menu(call: CallbackQuery):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id, call.message.id)
    bot.send_message(chat_id, '⬅️ Asosiy Menyu', reply_markup=main_btns())


@bot.callback_query_handler(func=lambda call: "product" in call.data)
def reaction_product(call: CallbackQuery):
    chat_id = call.message.chat.id
    product_id = int(call.data.split('|')[1])
    product = db.product_info(product_id)
    product_name, price, image, category_id = product[1:]
    bot.send_photo(chat_id, image,
                   caption=f"Siz tanladingiz: {product_name}\nNarxi: {price}so'm\n---\nIltimos kerakli miqdorni kiriting!",
                   reply_markup=product_count(product_id))


@bot.callback_query_handler(func=lambda call: 'page' in call.data)
def reaction_product_count(call: CallbackQuery):
    chat_id = call.message.chat.id
    page = int(call.data.split('|')[1])
    keyboard_list = call.message.reply_markup.keyboard
    product_id = int(keyboard_list[-1][-1].callback_data.split('|')[1])
    category_id = int(keyboard_list[-1][0].callback_data.split('|')[1])
    product = db.product_info(product_id)
    product_name, price, = product[1:3]
    bot.send_message(chat_id,
                     f"Mahsulot nomi: {product_name}\n {page} x {price} = {page * price}\nUmumiy hisob: {page * price}",
                     reply_markup=get_count(category_id, page, product_id))


@bot.callback_query_handler(func=lambda call: 'back_cat' in call.data)
def reaction_back(call: CallbackQuery):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id, call.message.id)
    bot.send_message(chat_id, 'Buyurtmani birga joylashtiramizmi? 🤗', reply_markup=order_btn(db.get_categories()))


@bot.callback_query_handler(func=lambda call: call.data == 'plus')
def reaction_plus(call: CallbackQuery):
    chat_id = call.message.chat.id
    keyboard_list = call.message.reply_markup.keyboard
    product_id = int(keyboard_list[-1][-1].callback_data.split('|')[1])
    category_id = int(keyboard_list[-1][0].callback_data.split('|')[1])
    page = int(keyboard_list[0][1].callback_data.split('|')[1])
    quantity = int(keyboard_list[0][1].text)
    page += 1
    bot.edit_message_reply_markup(chat_id, call.message.id,
                                  reply_markup=get_count(category_id, page, product_id))


#
#
@bot.callback_query_handler(func=lambda call: call.data == 'minus')
def reaction_plus(call: CallbackQuery):
    chat_id = call.message.chat.id
    keyboard_list = call.message.reply_markup.keyboard
    product_id = int(keyboard_list[-1][-1].callback_data.split('|')[1])
    category_id = int(keyboard_list[-1][0].callback_data.split('|')[1])
    page = int(keyboard_list[0][1].callback_data.split('|')[1])
    quantity = int(keyboard_list[0][1].text)
    if page > 1:
        page -= 1
        bot.edit_message_reply_markup(chat_id, call.message.id,
                                      reply_markup=get_count(category_id, page, product_id))
    else:
        bot.answer_callback_query(call.id, "Kamida 1 ta mahsulot kerak ⚠️", show_alert=True)


@bot.callback_query_handler(func=lambda call: 'add_card' in call.data)
def reaction_add_card(call: CallbackQuery):
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    bot.set_state(chat_id, CardState.card, user_id)
    product_id = int(call.data.split('|')[1])
    product = db.product_info(product_id)
    product_name, price = product[1:3]
    quantity = int(call.message.reply_markup.keyboard[0][1].text)
    with bot.retrieve_data(user_id, chat_id) as data:
        if data.get('card'):
            data['card'][product_name] = {
                'quantity': quantity,
                'price': price,
                'product_id': product_id
            }
        else:
            data['card'] = {
                product_name: {
                    'quantity': quantity,
                    'product_id': product_id,
                    'price': price
                }
            }
        bot.answer_callback_query(call.id, "Qo'shildi!", show_alert=True)


@bot.callback_query_handler(func=lambda call: call.data == 'show_card')
def reaction_show_card(call: CallbackQuery):
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    try:
        with bot.retrieve_data(chat_id, user_id) as data:
            res = get_card_text(data)
            text, markup = res['text'], res['markup']
            bot.send_message(chat_id, text, reply_markup=markup)
    except:
        bot.send_message(chat_id, "Savatingiz bo'sh", reply_markup=main_btns())


def get_card_text(data: dict):
    text = "Savatda: \n"
    total_price = 0
    for product_name, items in data['card'].items():
        quantity, product_id, price = items['quantity'], items['product_id'], items['price']
        products_price = price * quantity
        total_price += products_price
        text += f"""\n {product_name}
Narxi: {price} * {quantity} = {products_price}\n"""
    if total_price == 0:
        text = "Savatingiz bo'sh"
        markup = main_btns()
    else:
        text = f"\n Umumiy narx: {total_price} so'm"
        markup = card_btns(data['card'])
    return {'markup': markup, 'text': text}


@bot.callback_query_handler(func=lambda call: 'remove' in call.data)
def reaction_remove(call: CallbackQuery):
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    product_id = int(call.data.split('|')[1])
    with bot.retrieve_data(user_id, chat_id) as data:
        keys = [product_name for product_name in data['card'].keys()]
        for item in keys:
            if data['card'][item]['product_id'] == product_id:
                del data['card'][item]
    res = get_card_text(data)
    text, markup = res['text'], res['markup']
    bot.delete_message(chat_id, call.message.id)
    bot.send_message(chat_id, text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'clear')
def reaction_clear_card(call: CallbackQuery):
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    bot.delete_state(chat_id, user_id)
    bot.delete_message(chat_id, call.message.id)
    bot.send_message(chat_id, "Savat bo'shadi!", reply_markup=main_btns())


@bot.callback_query_handler(func=lambda call: call.data == 'submit')
def reaction_submit(call: CallbackQuery):
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    bot.send_message(chat_id, "To'lov turini tanlang!", reply_markup=payment_btn())


@bot.callback_query_handler(func=lambda call: 'payment' in call.data)
def reaction_payment(call: CallbackQuery):
    chat_id = call.message.chat.id
    bot.send_message(chat_id, "Buyurtmangiz qabul qilindi!\nOperator qong'irog'ini kuting 📲", reply_markup=main_btns())
