'''
Created on 09-Sep-2024

Type casting: Coversion of one data type into another
'''
a=float(input("Please enter a number:"))
b=float(input("Please enter another number:"))
c=a+b
print(type(a))
print(type(b))
print(f"Addition of two numbers {a} and {b} is:",c) #formatted strings
print("Addition of two numbers", a ,"and", b ,"is:", c)
print("Addition of two numbers %f and %f is: %f" %(a, b, c))