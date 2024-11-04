import time

#przykład 1
def pomiarczasu(funkcja):
    def wrapper():
        starttime = time.time()
        funkcja()
        endtime = time.time()
        wynik = endtime - starttime
        print(f"czas wykonania funkcji: {wynik} s")
    return wrapper

def usypiacz(funkcja):
    def wrapper():
        time.sleep(3)
        return funkcja()
    return wrapper


@pomiarczasu
@usypiacz
def big_lista():
    sum([i**5 for i in range(10_000_000)])

big_lista()

#przykład 2
def debug(funkcja):
    def wrapper(*args):
        print(f'wołana funkcja: {funkcja.__name__}')
        funkcja(*args)
    return wrapper

@debug
def info(i):
    print(f'ważny kod: {i}')

info("6543345309")

#przykład 3  dekorator sprawdzający typy argumentów
def sprawdz_typy(typy):
    def dekorator(funkcja):
        def wrapper(*args,**kwargs):
            for (arg,typ) in zip(args,typy):
                if not isinstance(arg,typ):
                    raise TypeError(f"Argument {arg} nie jest typu: {typ}")
            return funkcja(*args,**kwargs)
        return wrapper
    return dekorator

@sprawdz_typy((int,int))
def mnozenie(a,b):
    return a*b

try:
    print(mnozenie(6,8))
    print(mnozenie(6,"osiem"))
except TypeError as te:
    print(te)

#przykład 4 -> dekorator służący do memoizacji wyników

def memoizacja(funkcja):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print(f'Zwracanie wyniku z cache dla argumentów {args}')
            print(f'funkcja: {funkcja.__name__}({args} -> {funkcja(*args)})')
            return cache[args]
        else:
            wynik = funkcja(*args)
            cache[args] = wynik
            return wynik
    return wrapper

@memoizacja
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
