def devide_hundred(number: int) -> float:
    try:
        return 100 / number
    except ValueError:
        print("Неверный формат числа")
    except ZeroDivisionError:
        print("Число не может быть равно нулю")

print(devide_hundred(4))