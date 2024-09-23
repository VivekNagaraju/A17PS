'''
Created on 22-Sep-2024

Constructors: Methods used to construct/ initialize the objects
1. It is not mandatory to define a constructor by users
2. Constructor is called by default/ implicitly, at the time of object creation. 
But a constructor can be called explicitly if required.
3. Constructor can be created without parameters

'''
class HumanBeings:
    def __init__(self, name):
        self.name=name
        self.legs=2
        self.hands=2
        print(f"Object is created with {self.legs} legs and {self.hands} hands")
        
    def walk(self):
        print(f"{self.name} is walking")
        
    def run(self):
        print(f"{self.name} is running")
        
object1=HumanBeings("Vivek")
# print(object1.name)
# object1.__init__("Vikki")
# object1.run()
# object1.walk()
# print(object1.name)

# object2=HumanBeings("Megha")
# object2.run()
# object2.walk()
# print(object2.name)
# object1.run()