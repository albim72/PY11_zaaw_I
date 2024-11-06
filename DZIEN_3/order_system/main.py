from dataclasses import dataclass, field
from customer import Customer
from orderitem import OrderItem
from product import Product
from order import Order
from typing import List
import datetime

if __name__ == '__main__':
    #tworzenie produktów
    prodct1 = Product(name="Laptop", price=4500,stock=10)
    prodct2 = Product(name="Smartphone", price=2700, stock=15)

    #tworzenie klienta
    customer = Customer(first_name="Jan", last_name="Kowalski", email="jan.kowalski99@gmail.com")

    #tworzenie zamówienia
    order = Order(customer=customer)

    #dodawanie pozycji do zamówienia
    try:
        order.add_item(OrderItem(product=prodct1,quantity=2))
        order.add_item(OrderItem(product=prodct2,quantity=1))
    except ValueError as e:
        print(f"błąd: {e}")

    print(order.summary())
