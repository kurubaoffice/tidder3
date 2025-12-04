# app/bot/handlers/text_blocker.py
from app.bot.keyboards.main_menu import main_menu_keyboard

async def block_free_text(update, context):
    # Block any plain text input and remind user to use menus.
    if update.message:
        await update.message.reply_text(
            "⚠️ Please use the menu buttons only. Tap below to continue:",
            reply_markup=main_menu_keyboard()
        )
