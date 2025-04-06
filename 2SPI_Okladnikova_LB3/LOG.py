import logging
import time
from functools import wraps

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def log(func):
    @wraps(func) # сохраняет метаданные оригинальной функ
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Начало времени выполнения
        func_name = func.__name__  # Имя функции
        # Выполняем функцию и обрабатываем возможные ошибки
        try:
            result = func(*args, **kwargs)  # Вызов функции
            logging.info(
                f'Вызов функции: {func_name}, Аргументы: {args}, {kwargs}, Результат: {result}, Время выполнения: {time.time() - start_time:.4f} секунд')
            return result
        # обрабатываем исключения
        except Exception as e:
            logging.error(f'Ошибка в функции: {func_name}, Аргументы: {args}, {kwargs}, Ошибка: {e}')
            raise  # Повторно выбрасываем исключение

    return wrapper


@log
def divide(x, y):
    return x / y

@log
def add(x, y):
    return x + y

# Вызовы функций
print(divide(10, 2))  # 5.0
print(add(3, 4))      # 7

# Вызов с ошибкой
try:
    print(divide(10, 0))  # Ошибка деления на ноль
except ZeroDivisionError:
    pass
