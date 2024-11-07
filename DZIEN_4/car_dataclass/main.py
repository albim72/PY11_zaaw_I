from car import Car
from inventory import CarInventory

car1 = Car(mark="Tesla", model="Model S",year=2022, price=278000,is_electric=True)
car2 = Car(mark="Toyota", model="Avensis",year=2016, price=45000,is_electric=False)
car3 = Car(mark="BMW", model="i3",year=2021, price=112000,is_electric=True)

#tworzenie inwentarza
invent = CarInventory()
invent.add_car(car1)
invent.add_car(car2)
invent.add_car(car3)

print("\nStartowa wersja inwentarza:")
invent.list_inventory()

print("\nSamochody marki Tesla:")
tesla = invent.find_cars_by_mark("Tesla")
for car in tesla:
    print(car.car_description())

print("\nKońcowa wersja inwentarza:")
invent.remove_car(car2)
invent.list_inventory()
