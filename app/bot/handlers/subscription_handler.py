# app/bot/handlers/subscription_handler.py

from app.bot.keyboards.subscription_menu import subscription_menu_keyboard
from app.bot.handlers.navigation_handler import handle_navigation

async def subscription_callback(update, context):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data in ["BACK", "MAIN_MENU"]:
        await handle_navigation(update, context)
        return

    await query.edit_message_text(
        "📜 Subscription Options",
        reply_markup=subscription_menu_keyboard()
    )


async def subscription_action_handler(update, context):
    query = update.callback_query
    data = query.data
    await query.answer()

    if data in ["BACK", "MAIN_MENU"]:
        await handle_navigation(update, context)
        return

    await query.edit_message_text(
        f"📜 Subscription action: {data} (stub)",
        reply_markup=subscription_menu_keyboard()
    )


