import random
answer_count = 0
i = 0
while i < 3:
    number1 = random.randint(0,10)
    number2 = random.randint(0,10)
    answer = input(f'{number1} + {number2} = ')
    if int(answer) == number1 + number2:
        print("Правильно!")
        answer_count += 1
    else:
        print("Ответ неверный")
        i += 1
print(f'Игра окончена. Правильных ответов: {answer_count}')
