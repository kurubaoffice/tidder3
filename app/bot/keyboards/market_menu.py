# app/bot/keyboards/market_menu.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def market_menu_keyboard():
    buttons = [
        [InlineKeyboardButton("📉 Volatility (VIX)", callback_data="MARKET_VIX")],
        [InlineKeyboardButton("📊 NIFTY/BANKNIFTY", callback_data="MARKET_INDICES")],
        [InlineKeyboardButton("📈 Gainers / Losers", callback_data="MARKET_GAINERS")],
        [InlineKeyboardButton("🔎 Sector Analysis", callback_data="MARKET_SECTOR")],
        [InlineKeyboardButton("🔄 Refresh", callback_data="MARKET_REFRESH")],
        [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="BACK")],
    ]
    return InlineKeyboardMarkup(buttons)
