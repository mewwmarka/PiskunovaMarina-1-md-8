numbers_count = input("Введите количество слов: ")
print(
    " ".join(
        [input() for _ in range(int(numbers_count))]
    )
)