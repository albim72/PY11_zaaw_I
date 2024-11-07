# 1. Metaklasa CoffeeMeta
class CoffeeMeta(type):
    def __new__(cls, name, bases, dct):
        # Tworzymy nazwę pliku do zapisu typów kaw
        filename = "coffee_types.txt"

        # Zapisujemy nazwę klasy (typ kawy) do pliku
        with open(filename, 'a') as f:
            f.write(f"Available coffee type: {name}\n")

        # Tworzymy klasę przy użyciu metaklasy
        return super().__new__(cls, name, bases, dct)


# 2. Klasa Coffee - reprezentująca gotowy produkt
class Coffee:
    def __init__(self, coffee_type, sugar, milk, foam, flavor):
        self.coffee_type = coffee_type
        self.sugar = sugar
        self.milk = milk
        self.foam = foam
        self.flavor = flavor

    def __str__(self):
        return f"{self.coffee_type} with {self.sugar} sugar, {self.milk} milk, {self.foam} foam, flavored with {self.flavor}"


# 3. Builder - klasa CoffeeBuilder
class CoffeeBuilder:
    def __init__(self):
        self.coffee_type = None
        self.sugar = 0
        self.milk = 0
        self.foam = False
        self.flavor = None

    def set_coffee_type(self, coffee_type):
        self.coffee_type = coffee_type
        return self

    def set_sugar(self, sugar):
        self.sugar = sugar
        return self

    def set_milk(self, milk):
        self.milk = milk
        return self

    def set_foam(self, foam):
        self.foam = foam
        return self

    def set_flavor(self, flavor):
        self.flavor = flavor
        return self

    def build(self):
        return Coffee(self.coffee_type, self.sugar, self.milk, self.foam, self.flavor)


# 4. Klasy kaw, dziedziczące po Coffee i używające metaklasy CoffeeMeta
class Espresso(Coffee, metaclass=CoffeeMeta):
    def __init__(self, sugar, milk, foam, flavor):
        super().__init__("Espresso", sugar, milk, foam, flavor)


class Cappuccino(Coffee, metaclass=CoffeeMeta):
    def __init__(self, sugar, milk, foam, flavor):
        super().__init__("Cappuccino", sugar, milk, foam, flavor)


class Latte(Coffee, metaclass=CoffeeMeta):
    def __init__(self, sugar, milk, foam, flavor):
        super().__init__("Latte", sugar, milk, foam, flavor)


# Przykład użycia:

# Tworzymy instancję CoffeeBuilder
builder = CoffeeBuilder()

# Budujemy kawę Latte z dodatkami
latte = builder.set_coffee_type("Latte") \
    .set_sugar(2) \
    .set_milk(150) \
    .set_foam(True) \
    .set_flavor("Vanilla") \
    .build()

print(latte)  # Wypisuje: Latte with 2 sugar, 150 milk, True foam, flavored with Vanilla

# Tworzymy klasy kawy Espresso, Cappuccino
espresso = Espresso(sugar=1, milk=0, foam=False, flavor="None")
cappuccino = Cappuccino(sugar=3, milk=100, foam=True, flavor="Cinnamon")

# Wypisujemy klasyczne kawy
print(espresso)  # Wypisuje: Espresso with 1 sugar, 0 milk, False foam, flavored with None
print(cappuccino)  # Wypisuje: Cappuccino with 3 sugar, 100 milk, True foam, flavored with Cinnamon

# Sprawdzamy plik coffee_types.txt, w którym zapisano dostępne typy kaw
with open("coffee_types.txt", "r") as f:
    print(f.read())
