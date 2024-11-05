from dataclasses import dataclass

class Liczba:
    def __init__(self,x,y):
        self.x = x
        self.y = y

liczba = Liczba(5,3)
print(liczba.x)
print(liczba.y)

@dataclass
class DLiczba:
    x:int
    y:int
    z:float


dl = DLiczba(5,3,4.6)
print(dl.z)

print(liczba)
print(dl)


@dataclass
class Dane:
    nazwa:str
    licznik:int
    cena:float = 10.00

    @property
    def licznik(self):
        return self._licznik

    @licznik.setter
    def licznik(self,nw):
        self._licznik = nw

p = Dane("pudełko",4,11.45)
print(p)
p.licznik = 56
print(p)
