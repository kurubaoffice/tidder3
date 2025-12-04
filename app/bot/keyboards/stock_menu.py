
# app/bot/keyboards/stock_menu.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def stock_menu_keyboard():
    buttons = [
        [InlineKeyboardButton("🔍 Search Stock", callback_data="stock_search")],
        [InlineKeyboardButton("📈 Technical Analysis", callback_data="stock_tech")],
        [InlineKeyboardButton("🎯 Confidence Score", callback_data="stock_conf")],
        [InlineKeyboardButton("🔔 Alerts", callback_data="stock_alerts")],
        [InlineKeyboardButton("📊 Stock Overview", callback_data="stock_overview")],
        [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="MAIN_MENU")],
    ]
    return InlineKeyboardMarkup(buttons)
