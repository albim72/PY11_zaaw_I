class SpecialSet(set):
    def __init__(self,*args):
        super().__init__(*args)

    def add(self,element):
        if isinstance(element,int) and element % 2 == 0:
            print(f"dodaję liczbę parzystą - {element} - do zbioru")
            super().add(element)
        else:
            print(f"element {element} nie jest parzystą liczbą i nie zostanie dodany!")

    def union(self, *others):
        print("Tworzenie nowego zbioru jako wynik operacji union....")
        return super().union(*others)

    def is_subset_of_evens(self):
        for elem in self:
            if not isinstance(elem,int) or elem % 2 != 0:
                return False
        return True

s = SpecialSet([2,4,8])
s.add(12)
s.add(14)
s.add(6)
s.add(3)

print(f"czy zbiór składa się tylko z liczb parzystych: {s.is_subset_of_evens()}")

s2 = SpecialSet([10,12])
s3 = s.union(s2)
print(f"zbiór s: {s}")
print(f"zbiór s2: {s2}")
print(f"Nowy zbiór: {s3}")

s3.remove(4)
print(f"zbiór po zmianie: {s3}")
