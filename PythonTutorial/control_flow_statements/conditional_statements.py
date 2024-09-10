'''
Created on 09-Sep-2024

Conditional statements:
1. If statement
2. If-else statement
3. Series if-else statements
4. Nested if-else statements
'''

age=int(input("Please enter your age:"))

'''
if age >= 18:
    print("Allow inside")  
else:
    print("Don't allow")
'''    
'''
if age <= 18 and age > 12:
    print("Teenager")
     
elif age >= 60:
    print("Senior Citizen") 
    
elif age <=12:
    print("Child")
    
else:
    print("Adult")
'''    

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
    
