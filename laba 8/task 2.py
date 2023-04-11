from PIL import Image
holidays = {
    "День рождения": "otkritka.jpg",
    "Новый год": "new_year.jpg",
    "8 марта": "8_march.jpg",
    "23 февраля": "23_february"
            }
answer = input("К какому празднику нужна открытка? ").capitalize()
if answer in holidays:
    image = Image.open(holidays[answer])
    image.show()