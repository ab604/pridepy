"""
Simple ratelimit module replacement
This provides basic decorators without actual rate limiting
"""
import time
import functools


def sleep_and_retry(func):
    """Decorator that sleeps and retries on rate limit"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def limits(calls=1000, period=60):
    """Decorator that limits the number of calls in a given period"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Simple delay to avoid hammering the API
            time.sleep(0.05)  # 50ms delay between calls
            return func(*args, **kwargs)
        return wrapper
    return decorator
