'''
Created on 10-Sep-2024

Looping statements: These statements help us to execute any statement/s repeatedly

1. While loop:
    a. Initialization
    b. Condition
    c. Increment/ Decrement
2. For loop: to iterate over the sequence

Looping control statements:
1. break
2. continue
'''
'''
a=1
while a <= 5:
    # a=a+1
    a+=1
    print("Hello World!")
'''
'''
a=5
while a>=1:
    print("Hello World!")
    a+=1
'''
'''
while True:
    print("Hello World!")
'''
'''
for a in "Initialization":
    print(a)
'''
'''
for a in range(2,11,2):
    print(a)
    print("Hello World!")
'''
'''
while True:
    age=int(input("Please enter your age:"))
    if age > 18:
        if age >= 60:
            print("Senior Citizen")
        else:
            print("Adult")
        
    else:
        if age <=12:
            print("Child")
        else:
            print("Teenager")
    check = input("Do you want to continue?(y/n):")   
    if check == "n":
        break
'''
'''
for i in range(100):
    print(i)
    if i == 50:
        break 
'''

'''
for i in range(100):
    if i == 50:
        continue
    
    print(i)            
'''
'''
a=0
while a<=100:
    print(a)
    a+=1
    if a == 51:
        break 
        
'''

a=0
while a<=100:
    if a == 50:
        a+=1
        continue
    print(a)
    a+=1
    