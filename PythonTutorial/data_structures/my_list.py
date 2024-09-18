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
    c. Slicing Operator
    
3. List once created can be modified
4. List retains duplicate values
5. List stores None values
'''
a=[] # an empty list can be created
# print(a)
# print(type(a))

b=[1, 2, 3, 4] # homogeneous
# print(b)
# print(type(b))

c=[1, 2.4, "anv"] # heterogeneous
# print(c)

d=list(range(6)) # list can be created using built-in function
# print("d=",d)

# print(c[0])
# print(c[-1])

'''
print("for loop- iterates over the sequence")
for i in c:
    print(i)
    
    
print("While loop")
print("Length of C", len(c))
j=0
while j<len(c):
    print(c[j])
    j+=1
'''

d=list(range(1, 21, 2)) # list can be created using built-in function
print("d=",d)
# print(d[0:4])
# print(d[0:9:2])
# print(d[:9])

# print(d[5])

# d[5]=87 # modification- replacing an existing value
# print("d=",d)

'''
d[10]=55
print("d=",d)
'''
# d[4]=7
# print("d=",d)

# e=[1, 2, 3, 4, 2, 3, 4]
# print("e=", e)
#
# f=["jhds", 1, 2.4, True, None]
# print("f=", f)

d.append(5)
print("d=",d)

# d.clear()
# print("d=",d)

x=d.copy()
print("x=",x)

print(d.count(5))

d.extend([6, 10 ,7 , 8])
print("d=",d)

d.append([6, 10 ,7 , 8])
print("d=",d)

print(d[13])
print(d[15])

print(d.index(15))
print(d.index(7))
print(d.index(7, 4))

'''
Q1. Create a random list of numbers. Take an input from the user and determine:
    a. Whether that element is present in the given list
    b. If present then display the count
    c. Display the position/s at which the element is present
    
Q2. Create a random list of numbers. Take an input from the user and determine:
    a. Whether that element is present in the given list
    b. If present then display the count
    c. Remove the element from all the positions
'''

d.insert(5, 67)
print("d=",d)
print(d.pop(5))
print("d=",d)
d.remove(11)
print("d=",d)
print("Pop",d.pop())
print("d, after empty pop=",d)
# d.remove() #TypeError: list.remove() takes exactly one argument (0 given)
# print("d, after remove=",d)
d.remove(7)
print("d=",d)

d.reverse()
print("d, after reversing=",d)

d.sort()
print("d, after sorting=",d)

d.sort(reverse=True)
print("d, after sorting in descending order=",d)

e=[1, 2, 3, 4]
print("d=", d)
print("e=", e)

print("d+e=", d+e) #extend

# print("d-e=", d-e) #unsupported operand type(s) for -: 'list' and 'list'

# print("d*e=", d*e) #can't multiply sequence by non-int of type 'list'

print("e*2=", e*2) # extends a list with the same list number of times specified

print(4 in e)
