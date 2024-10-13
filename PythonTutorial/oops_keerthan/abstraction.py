'''
Abstraction: Functionality existing in thought but not implemented.

It might be because the implementation might differs from one sub-class to another

Types of methods:
1. Implemented method: definition and body
2. Unimplemented method: definition but no-body

- Abstract method acts as a mandatory field, 
 unless it is implemented user can't create an object from that class 
- Class which contains abstract method is an abstract class
- Whichever class inherits the abstract class should implement the abstract method in order create an object

Interface: Abstract class which contains abstract methods only. Whereas abstract contains both 
implemented and unimplemented methods
'''
from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self):
        print("Car object is created successfully!!")
        
    def move_forward(self): #Implemented method
        print("Car is moving forward")
    
    @abstractmethod    
    def open_airbags(self): #Unimplemented method
        pass

class HatchBack(Car):
    def build_bootspace(self):
        print("Boot space is built")   
        
    def open_airbags(self):
        print("Airbags are opened")    

# obj1=Car()
maruthi=HatchBack()
maruthi.build_bootspace()
maruthi.move_forward()
maruthi.open_airbags()







