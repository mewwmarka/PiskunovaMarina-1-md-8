class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, location, working_hours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
        self.location = location
        self.working_hours = working_hours

    def ice_cream_list(self):
        print(f"Виды мороженого: {', '.join(self.flavors)}" )

    def add_flavor(self, flavor):
        self.flavors.append(flavor)
        print("Успешно добавлен!")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print("Успешно удален!")
        else:
            print("Такого нет в списке!")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print("Такой сорт мороженого есть")
        else:
            print("Такого сорта мороженого нет")


class SoftIceCream(IceCreamStand):
    def shuffle(self):
        print("Мороженое размешивается")


class BoxIceCream(IceCreamStand):
    def cut(self):
        print("Разрезать мороженое по частям")


Cafe1 = IceCreamStand('Ice', 'IceCream', "Cool Street", "10:00 - 19:00")
Cafe1.add_flavor(input('Введите сорт мороженого:'))
Cafe1.ice_cream_list()
Cafe1.check_flavor("Ванильный")
Cafe1.remove_flavor(input("Введите то, что хотите удалить"))

