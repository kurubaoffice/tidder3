
# app/bot/keyboards/main_menu.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu_keyboard():
    buttons = [
        [InlineKeyboardButton("📈 Market Analysis", callback_data="MARKET_MENU")],
        [InlineKeyboardButton("📊 Stock Analysis", callback_data="STOCK_MENU")],
        [InlineKeyboardButton("🧨 Options Analysis", callback_data="OPTION_MENU")],
        [InlineKeyboardButton("💼 Mutual Funds", callback_data="MF_MENU")],
        [InlineKeyboardButton("💎 Subscription", callback_data="SUB_MENU")],
        [InlineKeyboardButton("❓ Help", callback_data="HELP_MENU")],
    ]

    return InlineKeyboardMarkup(buttons)


def market_menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📉 NIFTY Overview", callback_data="MARKET_NIFTY")],
        [InlineKeyboardButton("📈 BankNifty Overview", callback_data="MARKET_BANK")],

        [InlineKeyboardButton("↩️ Back", callback_data="BACK")],
        [InlineKeyboardButton("🏠 Main Menu", callback_data="MAIN_MENU")],
    ])