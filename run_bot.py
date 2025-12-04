"""
Tidder3 Telegram Bot Entry Point
"""

import logging
from telegram.ext import ApplicationBuilder

from app.core.config import settings
from app.core.logger import logger
from app.bot.router import register_all_handlers


def main():
    logger.info("🚀 Starting TidderAI Bot...")

    application = (
        ApplicationBuilder()
        .token(settings.TELEGRAM_BOT_TOKEN)
        .concurrent_updates(True)
        .build()
    )

    # Load all handlers from router
    register_all_handlers(application)

    logger.info("🤖 TidderAI Bot is running...")

    # PTB v20+ automatically manages asyncio loop
    application.run_polling()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        logger.warning("🛑 Bot Stopped")
