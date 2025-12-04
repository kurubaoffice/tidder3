from app.bot.keyboards.option_menu import option_menu_keyboard
from app.bot.handlers.navigation_handler import handle_navigation

async def option_callback(update, context):
    query = update.callback_query
    await query.answer()
    data = query.data

    # Handle back navigation first
    if data in ["BACK", "MAIN_MENU"]:
        await handle_navigation(update, context)
        return

    # Show Option menu by default
    await query.edit_message_text(
        "🧨 Option Analysis",
        reply_markup=option_menu_keyboard()
    )

async def option_action_handler(update, context):
    query = update.callback_query
    data = query.data
    await query.answer()

    # Handle back navigation first
    if data in ["BACK", "MAIN_MENU"]:
        await handle_navigation(update, context)
        return

    # Stub action handler
    await query.edit_message_text(
        f"🧨 Option action: {data} (stub)",
        reply_markup=option_menu_keyboard()
    )
