# app/bot/middleware/user_session.py
# Lightweight in-memory session storage for UI state per user (can be upgraded to Redis)
from collections import defaultdict

_sessions = defaultdict(dict)

def set_session(user_id, key, value):
    _sessions[user_id][key] = value

def get_session(user_id, key, default=None):
    return _sessions[user_id].get(key, default)

def clear_session(user_id):
    _sessions.pop(user_id, None)

