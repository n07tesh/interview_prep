'''
An abstract class can be considered as a blueprint for other classes.
It allows you to create a set of methods that must be created within any child classes built from the abstract class
'''
#syntax
from abc import ABC, abstractmethod
class figure(ABC):
    @abstractmethod
    def calcArea(self):
        pass
class square(figure):
    def calcArea(self):
        return self.side * self.side

class rectangle(figure):
    def calcArea(self):
        return self.width * self.height

square_ = square()
square_.side = 2
print(square_.calcArea())

rectangle_ = rectangle()
rectangle_.width = 3
rectangle_.height = 3
print(rectangle_.calcArea())
