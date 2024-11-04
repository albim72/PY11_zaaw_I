from typing import Any
print("kilka przykładów funkcji")

#przykład 1
def witaj(imie:str)->str:
    return f'Miło Cię widziec {imie}'

def konkurs(imie:str,punkty:int,miejsce:int) -> str:
    return f'uczestnik konkursu {imie}, liczba punktów: {punkty}, zajęte miejsce: {miejsce}'

def bonus(punkty:int,bonus:float)->float:
    return punkty * bonus

def osoba(funkcja:Any,*args)-> Any:
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Anna",78,9))
print(osoba(bonus,66,0.2))
