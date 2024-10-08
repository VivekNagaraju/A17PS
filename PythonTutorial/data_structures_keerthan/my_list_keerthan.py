'''
List:
1. Creation:
    - empty list can be created
    - list with elements (manually)
        > homogeneous list= list with same data type elements
        > heterogeneous list= list with diff. data type elements
    - using built-in function 'list'
    
    
2. Accessing:
    - Indexing: Index is a value given to the position in a DS
    - for loop
    - Slicing: Extracting the elements of a list into sub-list using Slicing operator
        Syntax: list_name[start:stop:step]

3. List once created can be modified- mutability (List is mutable)
4. list stores None value
5. list stores duplicate values
6. List is dynamic
'''
a=[] #empty list can be created
print(a)
print(type(a))

b=[1, 2, 3, 3, 4, 4] #list with elements. Homogeneous list
print(b)

c=[2, 3.78, "fh", True,None] # Heterogeneous list
print(c)

d=list(range(2, 20, 2)) #tuple, set()
print("d=",d)

print(c[2]) # don't change this brackets for tuple/ set

for element in c:
    print(element)

print("====Slicing====")
print("d=",d)
print(d[2:7:1])
print(d[2:7:2])
print(d[2:])
print(d[:7])

d[4]=11
print("d after modifying", d)

print(len(d))
'''
d[9]=65 #IndexError: list assignment index out of range
print("d after adding new element", d)
'''

d.append(6)
print("d after appending 6", d)

# d.clear()
# print("after clearing d",d)

e=d.copy()
print("e=", e)

print(d.count(6))
d.extend(c)
print("d after extending with c", d)

print(d.index(6))
print(d.index(6, 3))
# print(d.index(6, 10)) # ValueError: 6 is not in list

d.insert(5, 56)
print(d)

print(d.pop(6))
print(d)

d.remove(True)
d.remove(None)
d.remove('fh')
print(d)

d.reverse()
print(d)

d.sort()
print("d after sorting", d)

# d.sort()
# d.reverse()
d.sort(reverse=True)
print("d after sorting in descending order", d)

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
