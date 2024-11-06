from abc import ABC, abstractmethod

#metaklasa do śledzenia rejestracji fabryk
class FactoryMeta(type):
    factories = {}

    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)
        if not name.startswith('Abstract'):
            FactoryMeta.factories[name] = new_cls
        return new_cls

#klasa abstrakcyjna dla dokumentów
class AbstractDocument(ABC):
    @abstractmethod
    def generate_content(self):
        pass

    def display(self):
        print("Displaying Content")
        print(self.generate_content())
        
        
#konkretna implementacja dokumentów
class InvoiceDocument(AbstractDocument):
    def generate_content(self):
        return "Treśc faktury: Detale trasakcji, kwoty, daty."
    
class ReportDocument(AbstractDocument):
    def generate_content(self):
        return "Treśc raportu: Analizy danych, podsumowanie miesięczne."
