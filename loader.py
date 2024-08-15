from telebot import TeleBot, custom_filters, StateMemoryStorage
from config import TOKEN
from database import DataBase
from config import *

bot = TeleBot(TOKEN, state_storage=StateMemoryStorage())
db = DataBase(DB_NAME, DB_PASSWORD, DB_HOST, DB_USER)


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.ChatFilter())