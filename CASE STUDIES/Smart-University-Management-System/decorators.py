import time
from functools import wraps
from exceptions import AuthorizationError


def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not kwargs.get("is_admin", False):
            raise AuthorizationError("Access Denied: Admin privileges required")
        return func(*args, **kwargs)
    return wrapper


def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Method {func.__name__}() executed successfully")
        return result
    return wrapper


def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIME] {func.__name__} took {end - start:.4f}s")
        return result
    return wrapper
