'''
Inheritance: Availability/ accessability of parent/ super class properties from child/sub class
object

Types of inheritance:
1. Single level inheritance: GrandFather -> Father
2. Multi-level inheritance: GrandFather -> Father -> Child
3. Multiple inheritance: Father -> Child <- Mother
'''
class GrandFather:
    def gf_method(self):
        print("This is GF method")
        
    def watch(self):
        print("This is GF's watch")
        
class Father(GrandFather):
    def f_method(self):
        print("This is father method")
        
    def car(self):
        print("This is Father's car")
    
    def watch(self):
        print("This is Father's watch")
class Mother:
    def m_method(self):
        print("This is mother method")
        
    def car(self):
        print("This is Mother's car")
    
class Child(Father, Mother): 
    def c_method(self):
        print("This is child method")  
            
ajja=GrandFather()
ajja.gf_method()

appa=Father()
appa.f_method()
appa.gf_method()

paapu=Child()
paapu.m_method()
paapu.car()
paapu.watch()

print(Child.mro()) # mro= Method Resolution Order