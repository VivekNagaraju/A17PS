'''
Created on 16-Sep-2024
Lists:
1. Creation:
    a. Empty list- an empty list can be created
    b. with elements- list can be homogeneous/ heterogeneous
    c. using built-in function - list 
    
2. Accessing:
    a. Indexing
    b. looping statements
'''
a=[] # an empty list can be created
print(a)
print(type(a))

b=[1, 2, 3, 4] # homogeneous
print(b)
print(type(b))

c=[1, 2.4, "anv"] # heterogeneous
print(c)

d=list(range(6)) # list can be created using built-in function
print(d)

print(c[0])
print(c[-1])

print("for loop- iterates over the sequence")
for i in c:
    print(i)
    
    
print("While loop")
print("Length of C", len(c))
j=0
while j<len(c):
    print(c[j])
    j+=1

