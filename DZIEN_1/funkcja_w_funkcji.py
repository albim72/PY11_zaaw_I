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

#przykład 2 - prosty dekorator

def startstop(funkcja):
    def wrapper(*args):
        print("_"*60)
        print("startowanie procesu...")
        funkcja(*args)
        print("kończenie procesu...")
    return wrapper

def zawijanie(w_co):
    print(f"zawijanie czekoladek w {w_co}")

zw = startstop(zawijanie)
print(zw)
zw("sreberka")

@startstop
def dmuchanie(czego):
    print(f"dmuchanie {czego} na urodziny!")

@startstop
def info():
    print("@ - dekoracja bezwzględna!")

dmuchanie("baloników")
dmuchanie("świeczek na torcie")
info()

#przykład 3

liczby = [45,262,5,8,49,-3,53,25,22,12,48,90,32,8,7,3,2]
parzyste = list(filter(lambda x:x%2 == 0,liczby))
print(parzyste)

cube = list(map(lambda x:x**3,liczby))
print(cube)


#list comprehension
dane = [i**7 for i in range(12_000)]
print(dane)
