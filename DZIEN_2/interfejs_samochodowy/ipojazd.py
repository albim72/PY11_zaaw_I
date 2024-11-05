from abc import ABCMeta, abstractmethod

class IPojazd(metaclass=ABCMeta):
    @abstractmethod
    def spalanie(self,odl,jedn):raise NotImplementedError
    
    @abstractmethod
    def kosztyprzejazdu(self,odl,jedn,cena):raise NotImplementedError
