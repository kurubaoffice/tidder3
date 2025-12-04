# app/bot/handlers/main_menu_handler.py
from telegram import Update
from telegram.ext import ContextTypes
from app.bot.keyboards.main_menu import main_menu_keyboard


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to TidderAI Bot!\nChoose an option:",
        reply_markup=main_menu_keyboard()
    )


