def myCash(func):
    cash = {}

    def wrapper(*args):
        if args in cash:
            return cash[args]

        rezult = func(*args)
        cash[args] = rezult
        return rezult
    return wrapper
