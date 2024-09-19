'''
Created on 19-Sep-2024
d={key1:value1, key2:value2....}
'''
a={}
print(type(a))

b={1:"vivek", 2:"sowmya", 3:"Meghana"}
print(b)

c={1:"vivek", 2:"sowmya", 3:"Meghana", "a":"vivek"}
print(c)

d={1:"vivek", 2:"sowmya", 3:"Meghana", 1:"abc"}
print(d)

print(d[1])
d[3]="Megha"
print(d)

d[4]="bjhh"
print(d)

del d[4]
print(d)

# del d

# d.clear()
# print(d)

e= d.fromkeys([1, 2, 3, 4], "null")
print(e)

print(d.items())
print(d.keys())
print(d.values())


