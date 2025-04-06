from functools import lru_cache


@lru_cache(maxsize=100)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
