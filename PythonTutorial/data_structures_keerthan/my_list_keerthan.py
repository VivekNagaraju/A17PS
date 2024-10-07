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
    - Slicing
'''
a=[] #empty list can be created
print(a)
print(type(a))

b=[1, 2, 3, 4] #list with elements. Homogeneous list
print(b)

c=[2, 3.78, "fh", True] # Heterogeneous list
print(c)

d=list(range(10)) #tuple, set()
print(d)

print(c[2]) # don't change this brackets for tuple/ set

for element in c:
    print(element)
