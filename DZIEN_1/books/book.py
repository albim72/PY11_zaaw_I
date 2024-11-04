from abc import ABC,abstractmethod

class Book(ABC):
    def __init__(self,title,author,year,pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def __repr__(self):
        return f"obiekt klasy {self.__class__.__name__} ({self.title} -> {self.author})"

    def __call__(self, price):
        return f"ilośc stron z dodatkami: {self.pages + 5}, cena: {price} zł"

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def read(self):
        pass
