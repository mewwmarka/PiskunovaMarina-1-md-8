class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 0

    def describe_restaurant(self):
        print(f'Название ресторана: {self.restaurant_name} \nТип кухни: {self.cuisine_type}')

    def open_restaurant(self):
        print("Ресторан открыт!")

    @property
    def rating(self):
        return f'Новый рейтинг: {self._rating}'

    @rating.setter
    def rating(self, value):
        self._rating = value


newRestaurant = Restaurant('Клод Моне', 'Французская')
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

restaurant_1 = Restaurant('Moon', 'Итальянская')
restaurant_1.describe_restaurant()
restaurant_2 = Restaurant('Asia', 'Китайская')
restaurant_2.describe_restaurant()
restaurant_3 = Restaurant('Теремок', 'Русская')
restaurant_3.describe_restaurant()
restaurant_3.rating = input('Введите новый рейтинг: ')

print(restaurant_3.rating)

