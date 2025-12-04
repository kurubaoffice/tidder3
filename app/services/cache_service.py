
# app/services/cache_service.py
import time

_cache_store = {}  # in-memory cache


def cache_get(key: str):
    data = _cache_store.get(key)
    if not data:
        return None

    value, expiry = data
    if time.time() > expiry:
        del _cache_store[key]
        return None

    return value


def cache_set(key: str, value, ttl: int = 60):
    expiry = time.time() + ttl
    _cache_store[key] = (value, expiry)
