'''
Dictionary: The group of key-value pair elements
a={key1:value1, key2:value2...}

1. Empty dictionary can be created
'''
a={}
print(a)
print(type(a))

b={1:"Keerthan", 2:"Vivek"}
print(b)

print(b[1])

b[2]="Vicky" # update the existing element
print(b)

b[3]="abc" # adds the new element 
print(b)

del b[3]
print(b)

# del b # deletes the entire dictionary from the memory
# print(b)

# b.clear()
# print(b)

c=b.fromkeys([1,2,3, 4], None)
print(c)

print(b.get(2))
print(b.items())
print(b.keys())
print(b.values())

# print(b.pop(2)) # remove the corresponding key element
# print(b)

# b.popitem() # remove the last element
# print(b)


