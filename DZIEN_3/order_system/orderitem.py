from dataclasses import dataclass, field
from product import Product
from typing import List
import datetime

@dataclass
class OrderItem:
    product:Product
    quantity:int
    
    def total_price(self)->float:
        if not self.product.is_available(self.quantity):
            raise ValueError(f"Produkt {self.product.name} jest niedostępny w żądanej ilości!")
        return self.quantity * self.product.price
