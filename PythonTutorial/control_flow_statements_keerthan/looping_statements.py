'''
Looping(Iterations) statements: Statements which execute a group of statements multiple times until a condition is satisfied

Types of loops:
1. While loop
2. For loop

1. While loop:
    - Initialization
    - Condition
    - Increment/ Decrement
    
2. For loop

Loop control statements:
1. Break
2. Continue

'''

'''
count=5

while count>0:
    print("Hello world!")
    # count= count+1
    count-=1 # += Increment Operator -= Decrement Operator
'''
# range(start, stop, step)
# range(stop)
# range(start, stop)
'''
for count in range(5):
    print("Hello world!")
    print(count)
    
'''
'''
count=0
while True:
    print("Hello world!")
    count+=1
    print(count)
    if count == 150:
        break
'''
'''
for count in range(500):
    print("Hello world!")
    print(count)
    if count == 150:
        break
'''
'''
count=0
while count<200:
    if count == 151:
        count+=1
        continue
    print("Hello world!")
    count+=1
    print(count)
'''    
for count in range(500):
    if count == 151:
        continue
    print("Hello world!")
    print(count)