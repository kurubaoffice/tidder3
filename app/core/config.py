# app/core/config.py
"""
Central configuration loader for Tidder3.

Loads variables from .env, validates required keys,
and exposes safe access via Settings.
"""

import os
from dotenv import load_dotenv


# Load .env from project root
load_dotenv()

# Required keys for the application
REQUIRED_ENV_VARS = [
    "TELEGRAM_BOT_TOKEN",
]


def validate_required_env():
    """Ensure required environment variables exist."""
    missing = [key for key in REQUIRED_ENV_VARS if not os.getenv(key)]
    if missing:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing)}"
        )


# Run validation once on import
validate_required_env()


class Settings:
    """
    Access all environment variables from a single place.
    Import anywhere as:
        from app.core.config import settings
    """

    # System
    ENV: str = os.getenv("ENV", "development")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    # Telegram Bot
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_BOT_USERNAME: str = os.getenv("TELEGRAM_BOT_USERNAME", "TidderAI_Bot")

    # Data paths
    NSE_DATA_PATH: str = os.getenv("NSE_DATA_PATH", "app/data/storage/csv")
    CACHE_PATH: str = os.getenv("CACHE_PATH", "app/data/storage/cache")

    # Optional features
    ENABLE_NLP: bool = os.getenv("ENABLE_NLP", "false").lower() == "true"
    ENABLE_LIVE_OI: bool = os.getenv("ENABLE_LIVE_OI", "false").lower() == "true"


# Single shared instance
settings = Settings()

