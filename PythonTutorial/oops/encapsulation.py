'''
Encapsulation: Restricting the access of data members(variables, methods)
(Capsule)

Types/ Levels of encapsulation:
1. Protected members:
    - Can't be accessed outside the class
    - But can be accessed within the same class and its sub-classes
    - We use single underscore, "_", as prefix for any data member
2. Private members
    - Can't be accessed outside the class and also from its sub classes
    - We use double underscore, "__", as prefix for any data member
'''
class HumanBeings:
    def __init__(self, name=None, legs=2, hands=2):
        self.name=name
        self._legs=legs
        self.__hands=hands
        print(f"Object is created with name {self.name}, {self._legs} legs and {self.__hands} hands")
        
    def __walk(self):
        print(f"{self.name} is walking")
        
    def _run(self):
        print(f"{self.name} is running")

nanu=HumanBeings("abc")
nanu._run()
nanu._HumanBeings__walk() #name mangling
print(dir(nanu))