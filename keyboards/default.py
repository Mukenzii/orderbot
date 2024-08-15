from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
def main_btns():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        KeyboardButton("Buyurtma Berish 📝"),
        KeyboardButton("Aloqa uchun ☎️"),
        KeyboardButton("Bizning filiallarimiz 📍"),
        KeyboardButton("Sozlamalar ⚙️")
    )
    return markup

def register_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Ro'yxatdan o'tish✏️"))
    return markup


def send_contact():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Kontaktingizni ulashing", request_contact=True))
    return markup


def submit_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Ha"),
               KeyboardButton("Yo'q"))
    return markup


def admin_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    markup.add(
        KeyboardButton("Foydalunvchilarga e'lon 📢"),
        KeyboardButton("Foydalanuvchilar soni 👤"),
        KeyboardButton("Kategoriyalar qo'shish "),
        KeyboardButton("Kategoriyalar o'chirish"),
        KeyboardButton("Mahsulot o'chirish"),
        KeyboardButton("Mahsulot qo'shish")
    )

    return markup









