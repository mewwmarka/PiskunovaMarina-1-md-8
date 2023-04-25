import json
# products = {"products":
#                 [
#                     {
#                         "name": "Шоколад",
#                         "price": 50,
#                         "available": True,
#                         "weight": 100
#                     },
#                     {
#                         "name": "Кофе",
#                         "price": 100,
#                         "available": False,
#                         "weight": 250
#                     },
#                     {
#                         "name": "Чай",
#                         "price": 70,
#                         "available": True,
#                         "weightweight": 50
#                     }
#                 ]
#             }
# with open('products.json', 'w') as file:
#     json.dump(products, file)

with open("products.json", "r") as file:
    data = json.load(file)

for i in data["products"]:
    print(
        f'Название: {i["name"]}\n'
        f'Цена: {i["price"]}\n'
        f'Вес: {i["weight"]}\n'
        f'{"В наличии" if i["available"] else "Нет в наличии"}\n'
    )