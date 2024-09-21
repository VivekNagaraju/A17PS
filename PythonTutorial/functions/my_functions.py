'''
Created on 21-Sep-2024

@author: admin
'''
# a=2
# b=3
# c=a+b
# print(f"Sum of {a} and {b} =", a+b)
#
# d=4
# e=7
# f=d+e
# print(f"Sum of {d} and {e} =", d+e)

def display(): # Function without parameters
    print("Welcome to iQuest!")

def add(a, b): # Function with Parameters
    print(f"Sum of {a} and {b} =", a+b)
    # return a+b

def mul(a, b):
    # print(f"Multiplication of {a} and {b} =", a*b)
    return a*b
    
def add_mul(a, b):
    # c=add(a, b) # calling a function from another function
    # d=mul(a, b)
    return add(a, b), mul(a, b)
    
# display()
# total=add(276, 5)
# # print(total)
# print(add(276, 5))
# mul(add(276, 5), 3)
# print(add_mul(6, 7))
# x, y= add_mul(9, 5)
# print(x)
# print(y)