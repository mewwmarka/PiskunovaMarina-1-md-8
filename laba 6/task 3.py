STUDENTS = {
    "Марина": {"Русский", "Английский", "Китайский"},
    "Герман": {"Немецкий", "Русский"},
    "Ангелина": {"Китайский", "Английский"}
}


def get_summary_languages():
    summary = set()
    for languages in STUDENTS.values():
        summary = summary | languages
    return sorted(summary)


def get_language_owners(language: str):
    language = language.capitalize()

    return [
        name for name, languages in STUDENTS.items()
        if language in languages
    ]


print(get_summary_languages())
print(get_language_owners(input("Введите язык: ")))
