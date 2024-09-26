'''
Inheritance: Inheriting the properties(variables and methods) of one class to another class

Super class/ Parent class: Class from which properties are inherited
Sub class/ Child class: Class which inherits the properties

Types of Inheritance:
1. Single level inheritance
2. Multilevel inheritance
3. Multiple inheritance
'''

class GrandFather:
    def __init__(self, name, age):
        print("This is GF Constructor", name, age)
        
    def gf_method(self):
        print("This is Grand Father method")
        
class Father(GrandFather):
    def __init__(self, name, age):
        print("This is Father Constructor")
        super().__init__(name, age)
        
    def f_method(self):
        print("This is Father method")
        
    def car(self):
        print("This is Father's car")
        
class Mother:
    def m_method(self):
        print("This is Mother method")
    
    def car(self):
        print("This is Mother's car")
        
class Child(Father, Mother):
    def c_method(self):
        print("This is Child method")
        
    def car(self):
        print("This is Child's car")
        
obj1=GrandFather("ajja", 73)
obj1.gf_method()

obj2=Father("appa", 53)
obj2.f_method()
obj2.gf_method()

obj3=Child("nanu", 30)
obj3.c_method()
obj3.f_method()
obj3.gf_method()
obj3.m_method()
obj3.car()

print("Method resolution Order")
print(Child.mro())