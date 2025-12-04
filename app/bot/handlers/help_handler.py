# app/bot/handlers/help_handler.py

from app.bot.keyboards.help_menu import help_menu_keyboard
from app.bot.handlers.navigation_handler import handle_navigation

async def help_callback(update, context):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data in ["BACK", "MAIN_MENU"]:
        await handle_navigation(update, context)
        return

    await query.edit_message_text(
        "❓ Help & Support",
        reply_markup=help_menu_keyboard()
    )


async def help_action_handler(update, context):
    query = update.callback_query
    data = query.data
    await query.answer()

    if data in ["BACK", "MAIN_MENU"]:
        await handle_navigation(update, context)
        return

    await query.edit_message_text(
        f"❓ Help action: {data} (stub)",
        reply_markup=help_menu_keyboard()
    )
