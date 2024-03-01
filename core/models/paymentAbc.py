from abc import ABC, abstractmethod

# Definición de la clase abstracta con el método abstracto pagar
class PaymentABC(ABC):
    @abstractmethod
    def pay(self, price, mode):
        pass