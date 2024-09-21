'''
Created on 21-Sep-2024
1. Positional Arguments
2. Keyword arguments
3. Default arguments
4. Variable-length arguments
5. Variable-length keyword arguments
'''
from functions.my_functions import add

# def add(a=0, b=0, c=0): # Formal Arguments
#     print(f"Sum of {a}, {b} and {c} =", a+b+c)
    
def addition(*a): # Variable-length arguments
    print(a)

add(5, 3) # actual arguments #Positional Arguments
add(b=5, a=3)# Keyword arguments
addition()
addition(5)
addition(3, 6, 5)
addition(3, 6, 5, 6)

'''
Q. In a given tuple add all the elements and give the output.
(Don't use built-in function 'sum')
'''

def details(**x):
    print(x)

details(id=1, name="Vivek", place="Mysuru", Job="Tester")