class Osoba:
    def __init__(self,imie,nazwisko,wiek,waga,wzrost):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost

    def get_waga(self):
        return self.waga

    def set_waga(self,nowawaga):
        self.waga = nowawaga

    @property
    def wiek(self):
        return self._wiek

    @wiek.setter
    def wiek(self,nowywiek):
        self._wiek = nowywiek

    @property
    def bmi(self):
        return self.waga/(self.wzrost/100)**2



os = Osoba("Jan","Kos",30,89,176)
print(os)
print(os.get_waga())
os.set_waga(98)
print(os.get_waga())

print(os.wiek)
os.wiek = 38
print(os.wiek)

print(f"{os.bmi:.2f}")

