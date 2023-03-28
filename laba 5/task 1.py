numbers = [1, 6, 3, 4, 5]
answer = int(input("Введите число: "))
if answer in numbers:
    print(f'{numbers}\n{answer}\nПоздравляю, вы угадали число!')
else:
    print(f'{numbers}\n{answer}\nНет такого числа!')
