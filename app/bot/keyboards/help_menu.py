
# app/bot/keyboards/help_menu.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def help_menu_keyboard():
    buttons = [
        [InlineKeyboardButton("📘 How to Use", callback_data="help_how")],
        [InlineKeyboardButton("👨‍💻 Support", callback_data="help_support")],
        [InlineKeyboardButton("ℹ️ About", callback_data="help_about")],
        [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="MAIN_MENU")],
    ]
    return InlineKeyboardMarkup(buttons)
