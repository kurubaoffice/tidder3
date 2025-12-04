
# app/bot/keyboards/option_menu.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def option_menu_keyboard():
    buttons = [
        [InlineKeyboardButton("📌 OI & PCR", callback_data="options_oi")],
        [InlineKeyboardButton("🧲 OI Change Scanner", callback_data="options_scanner")],
        [InlineKeyboardButton("🔥 Unusual Activity", callback_data="options_unusual")],
        [InlineKeyboardButton("📉 Max Pain / IV", callback_data="options_iv")],
        [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="MAIN_MENU")],
    ]
    return InlineKeyboardMarkup(buttons)
