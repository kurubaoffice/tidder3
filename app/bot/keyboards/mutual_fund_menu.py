
# app/bot/keyboards/mutual_fund_menu.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def mutual_fund_menu_keyboard():
    buttons = [
        [InlineKeyboardButton("🔍 Search Fund", callback_data="mf_search")],
        [InlineKeyboardButton("⭐ Ratings", callback_data="mf_ratings")],
        [InlineKeyboardButton("📊 Screener", callback_data="mf_screener")],
        [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="MAIN_MENU")],
    ]
    return InlineKeyboardMarkup(buttons)
