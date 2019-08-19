#this file contains all markup generations 
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("MENU", callback_data="get_menu"))
    return markup


def menu_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Tdy's Bf 🍞", callback_data="cb_tdy_bf"),
               InlineKeyboardButton("Tdy's Dinz 🍱", callback_data="cb_tdy_dn"),
               InlineKeyboardButton("Tmr's Bf 🍞", callback_data="cb_tmr_bf"),
               InlineKeyboardButton("Tmr's Dinz 🍱", callback_data="cb_tmr_dn"))
    return markup