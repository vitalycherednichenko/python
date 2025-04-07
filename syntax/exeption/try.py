try:
    result = 10 / 0
except ZeroDivisionError:
    print("Деление на ноль!")
finally:
    print("Этот блок выполняется всегда.")

try:
    number = int(input("Введите число: "))
    result = 10 / number
except ValueError:
    print("Ошибка: Введите корректное число!")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")