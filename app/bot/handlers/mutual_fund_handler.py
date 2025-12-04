# app/bot/handlers/mutual_fund_handler.py
from app.bot.keyboards.mutual_fund_menu import mutual_fund_menu_keyboard
from app.bot.handlers.navigation_handler import handle_navigation

async def mutual_fund_callback(update, context):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data in ["BACK", "MAIN_MENU"]:
        await handle_navigation(update, context)
        return

    await query.edit_message_text(
        "💰 Mutual Fund Analysis",
        reply_markup=mutual_fund_menu_keyboard()
    )


async def mutual_fund_action_handler(update, context):
    query = update.callback_query
    data = query.data
    await query.answer()

    if data in ["BACK", "MAIN_MENU"]:
        await handle_navigation(update, context)
        return

    await query.edit_message_text(
        f"💰 Mutual Fund action: {data} (stub)",
        reply_markup=mf_menu_keyboard()
    )
