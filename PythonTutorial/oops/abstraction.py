'''
Abstraction: Something which exists in idea/ thought but not implemented
(Abstract)

Types of methods:
1. Implemented methods- method definition and method body
2. Unimplemented methods- method definition with 'pass' keyword

An Object can't be created from an abstract class, unless abstract method is 
implemented by its subclasses.

Abstract class: Implemented methods and abstract methods
- one or more unimplemented methods
- An Object can't be created from an abstract class

Interface: It is a class having all abstract methods
'''
from abc import *
class HumanBeings(ABC):
    def __init__(self, name=None, legs=2, hands=2):
        self.name=name
        self._legs=legs
        self.__hands=hands
        print(f"Object is created with name {self.name}, {self._legs} legs and {self.__hands} hands")
    
    @abstractmethod   
    def walk(self): #unimplemented method
        pass
        
    def run(self): #implemented method
        print(f"{self.name} is running")

class Male(HumanBeings):
    def walk(self):
        print(f"{self.name} is walking")
        
    def boxing(self):
        print(f"{self.name} is boxing")
        
nanu=Male("Vivek")
nanu.run()
nanu.boxing()