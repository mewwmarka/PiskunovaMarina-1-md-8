COUNTRIES: dict = {
    "Казахстан": "Астана",
    "Россия": "Москва",
    "Украина": "Киев",
    "Беларусь": "Минск",
    "Чехия": "Прага",
    "Франция": "Париж"
}


def print_key_value():
    [print(f'{key} - {value}') for key, value in COUNTRIES.items()]


def capital_by_country(country: str):
    return COUNTRIES[country]


def order_countries_by_alphabet():
    return dict(sorted(COUNTRIES.items()))


print_key_value()
print(capital_by_country('Казахстан'))
print(order_countries_by_alphabet())




