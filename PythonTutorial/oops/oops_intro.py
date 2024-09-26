'''
Created on 22-Sep-2024

<class '__main__.HumanBeings'>
<class 'float'>

print(type(object1))
print(type(l))

1. Inheritance
2. Polymorphism
3. Encapsulation
4. Abstraction
'''
class HumanBeings:
    def walk(self):
        print("I'm walking")
        
    def run(self):
        print("I'm running")
        
object1=HumanBeings()
print(type(object1))
object1.walk()
object1.run()
print(dir(object1))


