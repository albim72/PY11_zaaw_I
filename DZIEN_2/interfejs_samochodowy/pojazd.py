from ipojazd import IPojazd

class Pojazd(IPojazd):
    def spalanie(self, odl, jedn):
        return jedn*100/odl

    def kosztyprzejazdu(self, odl, jedn, cena):
        return self.spalanie(odl,jedn)*(odl/100)*cena
