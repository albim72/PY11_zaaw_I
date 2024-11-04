liczby = (900,1001,-787,0,67,89,6,8,3,12,66,457,-99,-765,589,987,21)

def statystyki(dane)->tuple:
    minimum:int = min(dane)
    maksimum:int = max(dane)
    rozstep:int = maksimum - minimum
    sr_arytm = sum(dane)/len(dane)
    return minimum,maksimum,rozstep,sr_arytm


wynik = statystyki(liczby)
print(wynik)
print(type(wynik))

mini,maxi,roz,sa = statystyki(liczby)
print(f'wartośc maksymalna: {maxi}, wartośc minimalna: {mini}, rozstęp: {roz}, średnia arytmetyczna: {sa}')
