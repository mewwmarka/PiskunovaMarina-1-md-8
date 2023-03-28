LETTER_POINTS = {
    ("А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"): 1,
    ("Д", "К", "Л", "М", "П", "У"): 2,
    ("Б", "Г", "Ё", "Ь", "Я"): 3,
    ("Ы", "Й"): 4,
    ("Ж", "З", "Х", "Ц", "Ч"): 5,
    ("Ш", "Э", "Ю"): 8,
    ("Ф", "Щ", "Ъ"): 10
}


def get_word_point(word: str):
    total: int = 0
    word = word.upper()
    for letter in word:
        for letters, point in LETTER_POINTS.items():
            if letter in letters:
                total += point

    return total


print(get_word_point(input("Введите слово: ")))
