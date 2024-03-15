from abc import ABC, abstractmethod

class Calculator(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    def add(self, x, y):
        pass

    @abstractmethod
    def sub(self, x, y):
        pass

    @abstractmethod
    def mul(self, x, y):
        pass

    @abstractmethod
    def div(self, x, y):
        pass

class BasicCalculator(Calculator):
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero."

class ScientificCalculator(Calculator):
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero."

basic_calc = BasicCalculator(1, "Basic Calculator")
print("Addition:", basic_calc.add(10, 5))
print("Subtraction:", basic_calc.sub(10, 5))
print("Multiplication:", basic_calc.mul(10, 5))
print("Division:", basic_calc.div(10, 5))

scientific_calc = ScientificCalculator(2, "Scientific Calculator")
print("Addition:", scientific_calc.add(10, 5))
print("Subtraction:", scientific_calc.sub(10, 5))
print("Multiplication:", scientific_calc.mul(10, 5))
print("Division:", scientific_calc.div(10, 5))
