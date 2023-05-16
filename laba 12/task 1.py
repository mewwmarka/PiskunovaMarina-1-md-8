class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def ice_cream_list(self):
        print(f"Виды мороженого: {', '.join(self.flavors)}" )


Cafe1 = IceCreamStand('Ice', 'IceCream')
Cafe1.flavors.append(input('Введите сорт мороженого:'))
Cafe1.ice_cream_list()