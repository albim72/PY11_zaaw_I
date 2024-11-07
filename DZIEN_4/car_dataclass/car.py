from dataclasses import dataclass

@dataclass
class Car:
    mark:str
    model:str
    year:int
    price:float
    is_electric:bool
    
    def car_description(self) -> str:
        electric_status = "Tak" if self.is_electric else "Nie"
        return (f"Marka: {self.mark}, Model: {self.model}, Rok: {self.year},"
                f"Cena: {self.price:.2f} zł, Elektryczny: {electric_status}")
