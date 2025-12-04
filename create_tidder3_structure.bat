@echo off
SET BASE=tidder3

echo Creating Tidder3 folder structure...

REM ===============================
REM ROOT
REM ===============================
mkdir %BASE%
mkdir %BASE%\app
mkdir %BASE%\tests
mkdir %BASE%\docs
mkdir %BASE%\scripts

echo.>%BASE%\README.md
echo.>%BASE%\requirements.txt
echo.>%BASE%\run_bot.py
echo.>%BASE%\run_server.py


REM ===============================
REM BOT LAYER
REM ===============================
mkdir %BASE%\app\bot
mkdir %BASE%\app\bot\handlers
mkdir %BASE%\app\bot\keyboards
mkdir %BASE%\app\bot\middleware

echo.>%BASE%\app\bot\bot_main.py
echo.>%BASE%\app\bot\router.py

REM Handlers
echo.>%BASE%\app\bot\handlers\main_menu_handler.py
echo.>%BASE%\app\bot\handlers\market_handler.py
echo.>%BASE%\app\bot\handlers\stock_handler.py
echo.>%BASE%\app\bot\handlers\option_handler.py
echo.>%BASE%\app\bot\handlers\mutual_fund_handler.py
echo.>%BASE%\app\bot\handlers\subscription_handler.py
echo.>%BASE%\app\bot\handlers\help_handler.py
echo.>%BASE%\app\bot\handlers\navigation_handler.py

REM Keyboards
echo.>%BASE%\app\bot\keyboards\main_menu.py
echo.>%BASE%\app\bot\keyboards\market_menu.py
echo.>%BASE%\app\bot\keyboards\stock_menu.py
echo.>%BASE%\app\bot\keyboards\option_menu.py
echo.>%BASE%\app\bot\keyboards\mutual_fund_menu.py
echo.>%BASE%\app\bot\keyboards\subscription_menu.py
echo.>%BASE%\app\bot\keyboards\help_menu.py

REM Middleware
echo.>%BASE%\app\bot\middleware\rate_limit.py
echo.>%BASE%\app\bot\middleware\user_session.py


REM ===============================
REM SERVICES
REM ===============================
mkdir %BASE%\app\services

echo.>%BASE%\app\services\symbol_service.py
echo.>%BASE%\app\services\analysis_service.py
echo.>%BASE%\app\services\volatility_service.py
echo.>%BASE%\app\services\technicals_service.py
echo.>%BASE%\app\services\oi_live_service.py
echo.>%BASE%\app\services\sentiment_nlp_service.py
echo.>%BASE%\app\services\subscription_service.py
echo.>%BASE%\app\services\cache_service.py


REM ===============================
REM ADAPTERS
REM ===============================
mkdir %BASE%\app\adapters

echo.>%BASE%\app\adapters\indicators_adapter.py
echo.>%BASE%\app\adapters\reporting_adapter.py
echo.>%BASE%\app\adapters\pipeline_adapter.py
echo.>%BASE%\app\adapters\live_data_adapter.py


REM ===============================
REM DOMAIN (Migrate from Tidder 2.0)
REM ===============================
mkdir %BASE%\app\domain
mkdir %BASE%\app\domain\indicators
mkdir %BASE%\app\domain\analysis
mkdir %BASE%\app\domain\reporting
mkdir %BASE%\app\domain\utils

REM Indicators
echo.>%BASE%\app\domain\indicators\compute.py
echo.>%BASE%\app\domain\indicators\interpretation.py
echo.>%BASE%\app\domain\indicators\confidence_score.py

REM Analysis
echo.>%BASE%\app\domain\analysis\index_analysis.py
echo.>%BASE%\app\domain\analysis\stock_analysis.py
echo.>%BASE%\app\domain\analysis\option_analysis.py

REM Reporting
echo.>%BASE%\app\domain\reporting\formatter.py
echo.>%BASE%\app\domain\reporting\summary.py
echo.>%BASE%\app\domain\reporting\telegram_format.py

REM Utils
echo.>%BASE%\app\domain\utils\math_utils.py
echo.>%BASE%\app\domain\utils\data_utils.py


REM ===============================
REM CORE LAYER
REM ===============================
mkdir %BASE%\app\core

echo.>%BASE%\app\core\logger.py
echo.>%BASE%\app\core\config.py
echo.>%BASE%\app\core\constants.py
echo.>%BASE%\app\core\exceptions.py


REM ===============================
REM DATA LAYER
REM ===============================
mkdir %BASE%\app\data
mkdir %BASE%\app\data\fetch
mkdir %BASE%\app\data\live
mkdir %BASE%\app\data\storage
mkdir %BASE%\app\data\storage\csv
mkdir %BASE%\app\data\storage\db
mkdir %BASE%\app\data\storage\cache

REM Fetchers
echo.>%BASE%\app\data\fetch\nse_price_fetcher.py
echo.>%BASE%\app\data\fetch\nse_index_fetcher.py
echo.>%BASE%\app\data\fetch\nse_oi_fetcher.py

REM Live
echo.>%BASE%\app\data\live\kite_live_feed.py


REM ===============================
REM UTILS
REM ===============================
mkdir %BASE%\app\utils

echo.>%BASE%\app\utils\helpers.py
echo.>%BASE%\app\utils\file_utils.py

echo.
echo Tidder3 structure created successfully!
pause
