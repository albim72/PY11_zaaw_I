from pojazd import Pojazd

pj = Pojazd()
odl = 598
jd = 52
cn = 6.18

print(f'spalanie [l/100]: {pj.spalanie(odl,jd):.2f}')
print(f'koszty przejazdu na trasie {odl} km -> {pj.kosztyprzejazdu(odl,jd,cn):.2f} zł')
