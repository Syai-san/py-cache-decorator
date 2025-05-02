from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable :
        cached_results = {}

        @wraps(func)
        def wrapper(*args: Any) -> Any:
            cache_key = (func, args)
            if cache_key in cached_results:
                print("Getting from cache")
                return cached_results[cache_key]

            print("Calculating new result")
            result = func(*args)
            cached_results[cache_key] = result
            return result

        return wrapper



