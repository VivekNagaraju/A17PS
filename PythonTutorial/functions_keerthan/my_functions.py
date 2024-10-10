'''
Function: Group of statements which perform certain task

Advantages:
1. Code re-usability
2. Easy maintenence

Types:
1. predefined functions
    - built-in functions: sub-set of predefined
     > no need of importing
2. User defined functions

Type 2:
1. Function with parameters
2. Function without parameters

Special cases:
1. Assigning a function to a variable
2. Passing function as an argument/ parameter for another function
3. Calling a function inside another function. 
4. Returning a function
'''
'''
a=7
b=6
print(f"Sum of {a} and {b} =", a+b)

a=9
b=2
print(f"Sum of {a} and {b} =", a+b)

c=5
d=8
print(f"Sum of {c} and {d} =", c+d)
'''
def addition(a, b): # Parameterized functions- function with parameters
    # print(f"Sum of {a} and {b} =", a+b)
    return a+b

def subtraction(a, b): # formal arguments
    return a-b

def add_sub(a, b):
    return addition(a, b), subtraction(a, b) # Calling a function inside another function. Returning a function

def welcome(): # Non-parametrized functions- function without parameters
    print("Welcome to iQuest")    
    
def double(a, b=2): # Default arguments
    return a*b
'''
print("===Functions===")
addition(2, 3) # actual arguments
addition(6, 7.9)
addition(9.6, 4)
    
welcome()
welcome()
welcome()
welcome()

print(addition(9.6, 4))

x=addition(87, 54) # Assigning a function to a variable
print("x=",x)
print("x*2=",double(x))

print(double(addition(4, 9))) # Function as an argument/ parameter for another function

print(add_sub(8, 2))
y, z=add_sub(9, 3)
print(y)
print(z)

print(double(5))
'''




