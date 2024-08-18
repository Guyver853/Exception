"""
Создание класса NegativeNumberError:

На основе стандартного класса исключений Exception создается собственный класс.

В конструкторе принимает два параметра: value (переданное число) и message (сообщение об ошибке).

Переопределён метод __str__, чтобы возвращать сообщение, включающее значение числа,
что позволяет пользователю понять, какое именно значение вызвало исключение.

Создание функции check_positive_number:

1. Принимает одно число как аргумент.
2. Если число отрицательное, выбрасывает исключение NegativeNumberError.
3. Если число положительное, функция возвращает True.

Проверка функции:

В первом блоке try-except вызывается функция с отрицательным числом -5, которое вызывает NegativeNumberError.
 Сообщение об ошибке выводится на экран.
Во втором блоке try-except вызывается функция с положительным числом 10, которое проходит проверку.
Результат выводится на экран.
"""

class NegativeNumberError(Exception):
    def __init__(self, value, message="Число должно быть положительным"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.value}"


def check_positive_number(number):
    if number < 0:
        raise NegativeNumberError(number)
    return True


# Проверка функции с отрицательным числом
try:
    check_positive_number(-5)  # Отрицательное число
except NegativeNumberError as e:
    print(e)

# Проверка функции с положительным числом
try:
    result = check_positive_number(10)  # Положительное число
    print("Число положительное:", result)
except NegativeNumberError as e:
    print(e)
