'''
Constructor(__init__): a (magic) method which is used to initialize/ construct an object
- It is not mandatory to define  constructor by a user
- When a constructor is not defined python interpretor will define its own constructor in the 
backend and constructs an object
- Constructor is called implicitly when an object is created.
- Constructor can be called explicitly when we have to re-initialize an object
- Constructor can be defined with/without parameters
'''
class HumanBeings:
    '''
    def __init__(self, name): #parameterized constructor
        self.name=name
        print("This is a constructor")
    
    def walk(self):
        print(f"{self.name} is walking")
        
    def run(self):
        print(f"{self.name} is running")
    '''
    def walk(self):
        print(f"Obj is walking")
        
    def run(self):
        print(f"Obj is running")
      
obj1=HumanBeings()
obj1.walk()
obj1.run()
print(type(obj1))
print(dir(obj1))

obj2=HumanBeings()
obj2.run()
obj2.walk()

# print(obj1.name)
# print(obj2.name)