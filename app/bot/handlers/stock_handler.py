from telegram import Update
from telegram.ext import ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from app.bot.handlers.navigation_handler import handle_navigation

# Example stock list; you can dynamically generate this from your NSE data
STOCKS_LIST = ["TCS", "INFY", "RELIANCE", "HDFC"]

def stock_menu_keyboard(stocks: list = STOCKS_LIST):
    """
    Generates the stock selection keyboard with Back button
    """
    buttons = [[InlineKeyboardButton(stock, callback_data=f"STOCK_{stock}")] for stock in stocks]
    # Add Back button
    buttons.append([InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="BACK")])
    return InlineKeyboardMarkup(buttons)


async def stock_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data in ["BACK", "MAIN_MENU"]:
        # Go back to main menu
        await handle_navigation(update, context)
        return

    if data.startswith("STOCK_"):
        stock_name = data.replace("STOCK_", "")
        await query.edit_message_text(
            f"📊 Analysis for {stock_name} (stub).",
            reply_markup=stock_menu_keyboard()
        )
        return

    # Default: show stock menu
    await query.edit_message_text(
        "📈 Stock List",
        reply_markup=stock_menu_keyboard()
    )
