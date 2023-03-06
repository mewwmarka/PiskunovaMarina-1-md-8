COLORS = {
    frozenset({'красный', 'синий'}): 'фиолетовый',
    frozenset({'красный', 'желтый'}): 'оранжевый',
    frozenset({'желтый', 'синий'}): 'зеленый'
}

color_one = str.lower(input("Введите 1 цвет: "))
color_two = str.lower(input("Введите 2 цвет: "))

finding_color = COLORS.get(
    frozenset({color_one, color_two})
)

if not finding_color:
    raise ValueError("не существует")
print(finding_color)

