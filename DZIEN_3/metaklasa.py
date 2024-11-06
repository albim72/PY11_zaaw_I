class MojaMeta(type):
    def __new__(cls,clsname,superclasses,attrs):
        print(f"__________ {cls.__class__.__name__} _________")
        print(f"nazwa klasy: {clsname}")
        print(f"klasy dziedziczone: {superclasses}")
        print(f"słownik atrybutów klasy: {attrs}")
        return type.__new__(cls,clsname,superclasses,attrs)
    
    def jedynka(cls):
        return 1
    
