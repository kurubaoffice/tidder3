# app/bot/handlers/navigation_handler.py
from telegram import Update
from telegram.ext import ContextTypes
from app.bot.keyboards.main_menu import main_menu_keyboard


async def handle_navigation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data

    await query.answer()

    if data in ["MAIN_MENU", "BACK"]:
        await query.edit_message_text(
            "🏠 Main Menu",
            reply_markup=main_menu_keyboard()
        )
