# app/bot/router.py

from telegram.ext import (
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)

from app.bot.handlers.main_menu_handler import start_command
from app.bot.handlers.navigation_handler import handle_navigation
from app.bot.handlers.market_handler import market_callback
from app.bot.handlers.stock_handler import stock_callback
from app.bot.handlers.option_handler import option_callback
from app.bot.handlers.mutual_fund_handler import mutual_fund_callback
from app.bot.handlers.subscription_handler import subscription_callback
from app.bot.handlers.help_handler import help_callback


def register_all_handlers(app):

    # /start
    app.add_handler(CommandHandler("start", start_command))

    # Main navigation
    app.add_handler(CallbackQueryHandler(handle_navigation, pattern="^(MAIN_MENU|BACK)$"))

    # Feature callbacks
    app.add_handler(CallbackQueryHandler(market_callback, pattern="^MARKET_"))
    app.add_handler(CallbackQueryHandler(stock_callback, pattern="^STOCK_"))
    app.add_handler(CallbackQueryHandler(option_callback, pattern="^OPTION_"))
    app.add_handler(CallbackQueryHandler(mutual_fund_callback, pattern="^MF_"))
    app.add_handler(CallbackQueryHandler(subscription_callback, pattern="^SUB_"))
    app.add_handler(CallbackQueryHandler(help_callback, pattern="^HELP_"))

    # Reject random text
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reject_text))


async def reject_text(update, context):
    await update.message.reply_text("⚠️ Please use the menu buttons only.")
