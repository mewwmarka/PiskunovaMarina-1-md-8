number = int(input("введите номер места: "))
if number > 55 or number < 1:
    raise ValueError

location = "верхнее" if number % 2 == 0 else "нижнее"

place = "боковое" if 55 > number > 36 else "в купе"

print(f'Место: {location} {place}')


