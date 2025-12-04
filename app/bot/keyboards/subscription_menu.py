
# app/bot/keyboards/subscription_menu.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def subscription_menu_keyboard():
    buttons = [
        [InlineKeyboardButton("💎 Plans", callback_data="subs_plans")],
        [InlineKeyboardButton("📅 Features", callback_data="subs_features")],
        [InlineKeyboardButton("🧾 Billing", callback_data="subs_billing")],
        [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="MAIN_MENU")],
    ]
    return InlineKeyboardMarkup(buttons)
