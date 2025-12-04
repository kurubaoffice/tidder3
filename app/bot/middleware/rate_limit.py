
# app/bot/middleware/rate_limit.py
# Very small example of a rate limiter stub. Plug into handlers or use as decorator.

import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, period_seconds=1.0):
        self.period = period_seconds
        self.users = defaultdict(float)

    def allowed(self, user_id):
        now = time.time()
        last = self.users[user_id]
        if now - last >= self.period:
            self.users[user_id] = now
            return True
        return False
