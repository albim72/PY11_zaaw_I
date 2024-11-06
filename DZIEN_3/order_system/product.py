from dataclasses import dataclass, field
from typing import List
import datetime

@dataclass
class Product:
    name:str
    price:str
    stock:int
    
    def is_available(self,quantity:int)->bool:
        return self.stock >= quantity
