from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from create import dp



kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn_game = KeyboardButton('/game 🍬')
btn_location = KeyboardButton('/location 🌏',request_location=True)
kb_main_menu.add(btn_game, btn_location)


kb_main_set = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn_rule = KeyboardButton('/rule 📗')
btn_set100 = KeyboardButton('/set 100 🍬')
btn_set125 = KeyboardButton('/set 125 🍬')
btn_set175 = KeyboardButton('/set 175 🍬')
btn_set200 = KeyboardButton('/set 200 🍬')
btn_set250 = KeyboardButton('/set 250 🍬')
kb_main_set.add(btn_rule, btn_set100,btn_set125,btn_set175,btn_set200,btn_set250)