# app/services/volatility_service.py

import requests
import pandas as pd
from datetime import datetime
from app.services.cache_service import cache_get, cache_set
from requests.exceptions import RequestException


# ============================================================
# 1. NSE INDIA VIX (LIVE)
# ============================================================

NSE_VIX_URL = "https://www.nseindia.com/api/allIndices"
NSE_HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.nseindia.com/"
}


def fetch_india_vix_live():
    try:
        r = requests.get(NSE_VIX_URL, headers=NSE_HEADERS, timeout=10)
        r.raise_for_status()

        data = r.json()

        for item in data.get("data", []):
            if item.get("index") == "INDIA VIX":

                last = float(item.get("last", 0))
                high = float(item.get("high", 0))
                low = float(item.get("low", 0))

                # ✅ FLEXIBLE FIELD SUPPORT (NSE changes often)
                change = float(
                    item.get("change")
                    or item.get("netChange")
                    or 0
                )

                percent_change = float(
                    item.get("pChange")
                    or item.get("percentChange")
                    or 0
                )

                return {
                    "value": last,
                    "change": change,
                    "percent_change": percent_change,
                    "high": high,
                    "low": low,
                    "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }

        print("[VIX] INDIA VIX not found in NSE response")
        return None

    except RequestException as e:
        print(f"[VIX] NSE request failed: {e}")
        return None

    except (ValueError, KeyError, TypeError) as e:
        print(f"[VIX] Data parsing error: {e}")
        return None



# ============================================================
# 2. VIX HISTORY (for PERCENTILE)
# ============================================================

def get_vix_history(days=252):
    try:
        url = "https://www.nseindia.com/api/chart-databyindex"
        params = {
            "index": "INDIA VIX",
            "period": "1Y"
        }

        r = requests.get(url, headers=NSE_HEADERS, params=params, timeout=10)
        r.raise_for_status()

        data = r.json().get("grapthData", [])

        values = [float(x[1]) for x in data if len(x) > 1]

        if not values:
            print("[VIX HISTORY] Empty history")
            return None

        return pd.Series(values[-days:])

    except RequestException as e:
        print(f"[VIX HISTORY] NSE request failed: {e}")
        return None

    except (ValueError, TypeError) as e:
        print(f"[VIX HISTORY] Data parsing error: {e}")
        return None



# ============================================================
# 3. VIX PERCENTILE
# ============================================================

def compute_vix_percentile(vix_series):
    ranks = vix_series.rank(pct=True)
    return float(ranks.iloc[-1] * 100)


# ============================================================
# 4. VOLATILITY REGIME
# ============================================================

def detect_regime(vix, percentile):

    if percentile is None:
        if vix <= 12:
            return "LOW"
        if 12 < vix <= 18:
            return "NEUTRAL"
        return "HIGH"

    if vix <= 12 or percentile <= 10:
        return "LOW"
    if 12 < vix <= 18:
        return "NEUTRAL"
    return "HIGH"


# ============================================================
# 5. NIFTY ATR %
# ============================================================

def compute_atr_pct(nifty_df, period=14):
    df = nifty_df.copy()

    df["H-L"] = df["high"] - df["low"]
    atr = df["H-L"].rolling(period).mean().iloc[-1]
    close = df["close"].iloc[-1]

    return round((atr / close) * 100, 2)


def get_nifty_ohlc(days=20):
    try:
        url = "https://www.nseindia.com/api/equity-stockIndices"
        params = {"index": "NIFTY 50"}

        r = requests.get(url, headers=NSE_HEADERS, params=params, timeout=10)
        r.raise_for_status()

        data = r.json().get("data", [])[:days]

        if not data:
            print("[NIFTY] Empty data")
            return None

        df = pd.DataFrame(data)

        df = df.rename(
            columns={
                "dayHigh": "high",
                "dayLow": "low",
                "lastPrice": "close",
            }
        )

        df[["high", "low", "close"]] = df[
            ["high", "low", "close"]
        ].astype(float)

        return df

    except RequestException as e:
        print(f"[NIFTY] NSE request failed: {e}")
        return None

    except (ValueError, KeyError, TypeError) as e:
        print(f"[NIFTY] Data parsing error: {e}")
        return None



# ============================================================
# 6. STRATEGY ENGINE
# ============================================================

def suggest_strategy(regime):

    if regime == "LOW":
        return [
            ("Buy Puts", "now", "Best time to buy puts. Crash probability high."),
            ("Buy Straddle", "now", "IV is cheap → perfect for straddles."),
            ("Put Calendar", "now", "Sell near-month / buy next-month ATM put."),
        ]

    if regime == "NEUTRAL":
        return [
            ("Light Long Vol", "monitor", "Build small hedges. Wait for breakout.")
        ]

    return [
        ("Sell Premium", "now", "High IV → iron condor, short strangle (hedged).")
    ]


# ============================================================
# 7. UNIFIED PUBLIC API
# ============================================================

def get_india_vix():
    cache_key = "INDIA_VIX_FULL"

    cached = cache_get(cache_key)
    if cached:
        return cached

    live = fetch_india_vix_live()
    if not live:
        return {"status": "error"}

    vix_value = live["value"]

    # Percentile
    vix_hist = get_vix_history()
    percentile = (
        round(compute_vix_percentile(vix_hist), 2)
        if vix_hist is not None
        else None
    )

    # Regime
    regime = detect_regime(vix_value, percentile)

    # ATR %
    nifty_df = get_nifty_ohlc()
    atr_pct = compute_atr_pct(nifty_df) if nifty_df is not None else None

    # Strategy
    strategies = suggest_strategy(regime)

    final = {
        "status": "ok",
        "value": live["value"],
        "change": live["change"],
        "percent_change": live["percent_change"],
        "high": live["high"],
        "low": live["low"],
        "percentile": percentile,
        "regime": regime,
        "atr_pct": atr_pct,
        "strategies": strategies,
        "updated_at": live["updated_at"],
    }

    cache_set(cache_key, final, ttl=60)
    return final
