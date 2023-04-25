import json
with open("products.json", "r") as file:
    exists_data = json.load(file)

print('Введите данные в виде: Название,Цена,Вес,В наличии')

new_data = input().split(',')
exists_data['products'].append(
    dict(
        name=new_data[0],
        price=new_data[1],
        weight=new_data[2],
        available=bool(new_data[3])
    )
)

with open('products.json', 'w') as file:
    json.dump(exists_data, file)

for i in exists_data['products']:
    print(
        f'Название: {i["name"]}\n'
        f'Цена: {i["price"]}\n'
        f'Вес: {i["weight"]}\n'
        f'{"В наличии" if i["available"] else "Нет в наличии"}\n'
    )

print(exists_data)