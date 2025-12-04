from telegram import Update
from telegram.ext import ContextTypes
from app.bot.keyboards.market_menu import market_menu_keyboard
from app.bot.handlers.navigation_handler import handle_navigation
from app.services.volatility_service import get_india_vix

MARKET_ACTIONS = {
    "MARKET_VIX": "📉 VIX page — (stub).",
    "MARKET_INDICES": "📊 NIFTY/BANKNIFTY overview (stub).",
    "MARKET_GAINERS": "📈 Gainers / Losers (stub).",
    "MARKET_SECTOR": "🔎 Sector Analysis (stub).",
}

async def market_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data.strip()

    # ✅ Handle navigation
    if data in ["BACK", "MAIN_MENU"]:
        await handle_navigation(update, context)
        return

    # ✅ Handle refresh
    if data == "MARKET_REFRESH":
        await query.edit_message_text(
            "♻️ Refreshing Market Data...",
            reply_markup=market_menu_keyboard()
        )
        return

    # ✅ REAL NSE VIX (FULL DISPLAY)
    if data == "MARKET_VIX":
        vix = get_india_vix()

        if vix["status"] == "ok":

            # ✅ Build Strategy Text
            strategy_lines = []
            for name, timing, desc in vix.get("strategies", []):
                strategy_lines.append(
                    f"• *{name}* ({timing}) — {desc}"
                )

            strategy_text = (
                "\n".join(strategy_lines)
                if strategy_lines
                else "• No strategy available."
            )

            regime_emoji = {
                "LOW": "🟢 LOW",
                "NEUTRAL": "🟡 NEUTRAL",
                "HIGH": "🔴 HIGH"
            }.get(vix.get("regime"), vix.get("regime", "—"))

            text = (
                f"📉 *INDIA VIX — LIVE*\n\n"
                f"*Value:* `{vix['value']}`\n"
                f"*Change:* `{vix['change']} ({vix['percent_change']}%)`\n"
                f"*High:* `{vix['high']}`\n"
                f"*Low:* `{vix['low']}`\n\n"
                f"*Percentile:* `{vix.get('percentile', '—')}`\n"
                f"*Regime:* {regime_emoji}\n\n"
                f"*📏 NIFTY ATR:* `{vix.get('atr_pct', '—')}%`\n\n"
                f"*🧠 Strategy:*\n{strategy_text}\n\n"
                f"🕒 *Updated:* {vix['updated_at']}"
            )

        else:
            text = "⚠️ Unable to fetch India VIX right now."

        await query.edit_message_text(
            text,
            reply_markup=market_menu_keyboard(),
            parse_mode="Markdown"
        )
        return  # ✅ STOP here to avoid overwrite

    # ✅ Default fallback (other market buttons)
    await query.edit_message_text(
        "📊 Market action (stub).",
        reply_markup=market_menu_keyboard()
    )


    # ✅ Other stub actions
    message = MARKET_ACTIONS.get(data, "📊 Market action (stub).")
    await query.edit_message_text(
        message,
        reply_markup=market_menu_keyboard()
    )

