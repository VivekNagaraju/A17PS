'''
Formal arguments: Declared at the time of function definition
    1. Default arguments
    2. Variable length arguments
    3. Keyword variable length arguments
Actual arguments: Actual values passed when the function is called
    1. Positional arguments
    2. Keyword arguments

Types:
1. Positional arguments
2. Keyword arguments
3. Default arguments
4. Variable length arguments
5. Keyword variable length arguments
'''
# from functions_keerthan.my_functions import addition, subtraction
# from functions_keerthan.my_functions import addition
from functions_keerthan.my_functions import *


# def addition(a, b):
#     return a+b

# def subtraction(a, b): 
#     return a-b

def adding(*a): # Variable length arguments
    print(a)

def adding_kwargs(**a): # Keyword variable length arguments
    print(a)

print(subtraction(8, 5))
print(subtraction(5, 8)) #Positional arguments
print(subtraction(b=5, a=8)) # Keyword arguments

# print(addition(4, 3, 6))
adding(1, 2, 3,4,5)
adding_kwargs(a=1, b=2, c=65)

print(addition(4, 6))

