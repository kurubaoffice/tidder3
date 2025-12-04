# app/bot/bot_main.py
import logging
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters
)
from app.core.config import BOT_TOKEN
from app.bot.router import ROUTE_PATTERNS
# handlers
from app.bot.handlers.main_menu_handler import start_handler, main_menu_handler
from app.bot.handlers.market_handler import market_handler, market_action_handler
from app.bot.handlers.stock_handler import stock_handler, stock_action_handler
from app.bot.handlers.option_handler import option_handler, option_action_handler
from app.bot.handlers.mutual_fund_handler import mutual_fund_handler, mf_action_handler
from app.bot.handlers.subscription_handler import subscription_handler, subscription_action_handler
from app.bot.handlers.help_handler import help_handler, help_action_handler
from app.bot.handlers.navigation_handler import back_to_main_handler
from app.bot.handlers.text_blocker import block_free_text
from app.bot.middleware.rate_limit import RateLimiter

logger = logging.getLogger(__name__)

async def create_app():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Middleware: attach simple rate limiter (example)
    app.add_handler(CommandHandler('start', start_handler))

    # Core menu routes (exact patterns)
    app.add_handler(CallbackQueryHandler(main_menu_handler, pattern="^main_menu$"))

    # Submenu entry handlers
    app.add_handler(CallbackQueryHandler(market_handler, pattern="^market$"))
    app.add_handler(CallbackQueryHandler(stock_handler, pattern="^stock$"))
    app.add_handler(CallbackQueryHandler(option_handler, pattern="^options$"))
    app.add_handler(CallbackQueryHandler(mutual_fund_handler, pattern="^mutual$"))
    app.add_handler(CallbackQueryHandler(subscription_handler, pattern="^subs$"))
    app.add_handler(CallbackQueryHandler(help_handler, pattern="^help$"))

    # Submenu action handlers (detailed actions under each submenu)
    app.add_handler(CallbackQueryHandler(market_action_handler, pattern="^market_"))
    app.add_handler(CallbackQueryHandler(stock_action_handler, pattern="^stock_"))
    app.add_handler(CallbackQueryHandler(option_action_handler, pattern="^options_"))
    app.add_handler(CallbackQueryHandler(mf_action_handler, pattern="^mf_"))
    app.add_handler(CallbackQueryHandler(subscription_action_handler, pattern="^subs_"))
    app.add_handler(CallbackQueryHandler(help_action_handler, pattern="^help_"))

    # Universal back button to main menu
    app.add_handler(CallbackQueryHandler(back_to_main_handler, pattern="^main_menu$"))

    # Strict: block free-text messages that are not commands
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), block_free_text))

    logger.info("🚀 Tidder3 Bot (UI) is running")
    await app.run_polling()
