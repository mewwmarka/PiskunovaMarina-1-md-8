year = int(input("Введите год: "))
print(
    f"Год {year} - високосный"
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    else "Этот год не високосный"
)

