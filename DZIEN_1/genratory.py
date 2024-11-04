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
