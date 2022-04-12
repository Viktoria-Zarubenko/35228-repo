from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """
        Klasa Creator deklaruje metodę fabrykującą, która ma zwrócić an
        obiekt klasy Plan. Podklasy Stwórcy zwykle zapewniają wdrożenie tej metody.
    """

    @abstractmethod
    def factory_method(self):
        """
            Należy pamiętać, że Stwórca może również zapewnić domyślną implementację
            metody fabrycznej.
        """
        pass

    def some_operation(self) -> str:

        # Wywołujemy metodę fabryki, aby utworzyć obiekt Plan.
        plan = self.factory_method()

        # Używamy Plan
        result = f"Kreator: ten sam kod kreatora, z którym właśnie pracowałismy {plan.operation()}"

        return result


"""
    Concrete Creators nadpisują metodę fabryczną, aby zmienić wynikowy rodzaj planów.
"""


class ConcreteCreator1(Creator):
    def factory_method(self) -> Plan:
        return ConcretePlan1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Plan:
        return ConcretePlan2()


class Plan(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass

class ConcretePlan1(Plan):
    def operation(self) -> str:
        return "{Wynik ConcretePlan1}"


class ConcretePlan2(Plan):
    def operation(self) -> str:
        return "{Wynik ConcretePlan2}"


def client_code(creator: Creator) -> None:
    """
        Kod klienta działa z instancją konkretnego twórcy, aczkolwiek poprzez
        jego podstawowy interfejs. Dopóki klient nadal współpracuje z twórcą poprzez
        interfejs bazowy, możemy przekazać mu dowolną podklasę twórcy.
    """

    print(creator.some_operation())