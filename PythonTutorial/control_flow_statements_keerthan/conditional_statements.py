'''
Indent/ indentation

1. If statement
2. If-else
3. Series if-else statements
4. Nested if-else statements
'''

age=int(input("Please enter your age"))
'''
if age >= 18:
    print("You're allowed")
else:
    print("You're not allowed13")
'''
'''
if age < 13:
    print("You're a child")
    
elif age < 20:
    print("You're a teenager")

elif age < 60:
    print("You're an adult")
    
else:
    print("You're senior citizen")
'''

if age > 19:
    if age >= 60:
        print("You're senior citizen")
    else: 
        print("You're an adult")
else:
    if age > 12:
        print("You're a teenager")
    else:
        print("You're a child")