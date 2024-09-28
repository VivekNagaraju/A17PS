'''
Polymorphism:
Poly= Many
Morphs= Forms

Types of polymorphism:
1. Overloading
    a. Operator Overloading: +, *
    b. Method Overloading
    c. Constructor Overloading
2. Overriding
    a. Method Overriding
    b. Constructor Overriding
'''
# from typing import overload
class Maths:
    def __init__(self):
        print("No argument constructor")
    
    '''   
    @overload
    def __init__(self, a):
        print("One argument constructor")
        
    @overload
    def __init__(self, a, b):
        print("Two argument constructor")
    '''
            
    def add(self,a=0, b=0, c=0): # Default Arguments
        print(f"Sum of {a}, {b} and {c} =", a+b+c)

obj1=Maths()