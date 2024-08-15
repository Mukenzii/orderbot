from telebot.handler_backends import State, StatesGroup

class RegisterState(StatesGroup):
    full_name = State()
    contact = State()
    submit = State()


class CardState(StatesGroup):
    card = State()



class ProductState(StatesGroup):
    product_name = State()
    price = State()
    image = State()
    category = State()