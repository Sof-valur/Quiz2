from __future__ import annotations
from abc import ABC, abstractmethod

class Abstract_factory(ABC):

    @abstractmethod
    def create_productA(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_productB(self) -> AbstractProductB:
        pass


class ConcreteFactory1(Abstract_factory):

    def create_productA(self) -> AbstractProductA:
        return ConcreteProdA1()

    def create_productB(self) -> AbstractProductB:
        return ConcreteProdB1()

class ConcreteFactory2(Abstract_factory):
    def create_productA(self) -> AbstractProductA:
        return ConcreteProdA2()

    def create_productB(self) -> AbstractProductB:
        return ConcreteProdB2()

class AbstractProductA(ABC):
    def function_A(self) -> str:
        pass

class ConcreteProdA1(AbstractProductA):
    def function_A(self) -> str:
        return "Product A1 result"

class ConcreteProdA2(AbstractProductA):
    def function_A(self) -> str:
        return "Product A2 result"

class AbstractProductB(ABC):
    def function_B(self) :
        pass

    def another_function_B(self, collaborator: AbstractProductA) :
        pass

class ConcreteProdB1(AbstractProductB):
    def function_B(self) -> str:
        return "Product B1 result"

    def another_function_B(self, collaborator: AbstractProductA) -> str:
        result = collaborator.function_A()
        return f"Result of B1 collaborating with ({result})"

class ConcreteProdB2(AbstractProductB):
    def function_B(self) -> str:
        return "Product B2 result"

    def another_function_B(self, collaborator: AbstractProductA) -> str:
        result = collaborator.function_A()
        return f"Result of B2 collaborating with ({result})"

def client(factory: Abstract_factory) -> None:
    product_a = factory.create_productA()
    product_b = factory.create_productB()

    print(f"{product_b.function_B()}")
    print(f"{product_b.another_function_B(product_a)}", end="")

if __name__ == "__main__":
    print("Client: Testing Client with first factory type:")
    client(ConcreteFactory1())

    print("\n")

    print("Client: Testing Client with second factory type:")
    client(ConcreteFactory2())










# create_productA(self) -> AbstractProductA:
    # return ConcreteProductA1()
