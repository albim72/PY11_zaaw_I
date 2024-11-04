#przykład 1
def liczby():
    wynik = []
    for i in range(31):
        wynik.append(i)

    return wynik

print(liczby())

def genliczby():
    for i in range(31):
        yield i

print(genliczby())
print(list(genliczby()))

for p in genliczby():
    print(p)

#przykład 2
def wznowienie(n,k):
    print("wstrzymanie działania 0")
    yield 3005
    print("wznowienie działanie 1")

    print("wstrzymanie działania 1")
    yield n+k
    print("wznowienie działanie 2")

    print("wstrzymanie działania 2")
    n = 8*k - 4
    yield n-k
    print("wznowienie działanie 3")

    print("wstrzymanie działania 3")
    yield n*k
    print("wznowienie działanie 4")

    print("wstrzymanie działania 4")
    yield n/k
    print("wznowienie działanie 5")

print(wznowienie(8,4))
print(list(wznowienie(8,4)))

for i in wznowienie(8,4):
    print("_"*50)
    print(type(i))
    print(f'zwrócono wartośc: {i}')

print("*"*60)
k = wznowienie(9,3)
print(next(k))
print(next(k))
