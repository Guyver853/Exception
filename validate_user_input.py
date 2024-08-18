"""
Объяснение работы функции:

Проверка типа данных: Если data не является словарем, возникает TypeError.

Проверка ключа 'name': Если ключ 'name' отсутствует или его значение не строка, генерируется ValueError.

Проверка ключа 'age': Если ключ 'age' отсутствует или его значение не положительное число (целое или дробное), возникает ValueError.

Внутри try блока обработка исключений ValueError и TypeError.
При возникновении любого из этих исключений создается новое исключение ValueError с сообщением и с указанием оригинального исключения
при помощи from e.

Так можно отследить всю цепочку ошибок и узнать, какая именно ошибка вызвала текущее исключение

Примеры проверки:

Корректные данные: {"name": "Alice", "age": 30} — данных обработаны без ошибок.

Отсутствует ключ 'name': выводит сообщение об ошибке.

Некорректное значение для 'age': выводит сообщение об ошибке.

Некорректный тип входных данных: выводит сообщение об ошибке.
"""


def validate_user_input(data):
    if not isinstance(data, dict):
        raise TypeError("Входные данные должны быть словарем.")

    try:
        if 'name' not in data or not isinstance(data['name'], str):
            raise ValueError("Ключ 'name' должен присутствовать и быть строкой.")

        if 'age' not in data or not (isinstance(data['age'], (int, float)) and data['age'] > 0):
            raise ValueError("Ключ 'age' должен присутствовать и быть положительным числом.")
    except (ValueError, TypeError) as e:
        raise ValueError("Ошибка в данных пользователя: " + str(e)) from e


# Проверка функции
try:
    validate_user_input({"name": "Alice", "age": 30})  # Корректные данные
    print("Данные корректны.")
except Exception as e:
    print(e)

try:
    validate_user_input({"age": 30})  # Отсутствует ключ 'name'
except Exception as e:
    print(e)

try:
    validate_user_input({"name": "Alice", "age": -5})  # Некорректное значение для age
except Exception as e:
    print(e)

try:
    validate_user_input("Некорректный тип данных")  # Некорректный тип входных данных
except Exception as e:
    print(e)

