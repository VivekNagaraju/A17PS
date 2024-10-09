'''
String: Group of characters enclosed within ""/''/''' '''/""" """
'''
a="  iQuest  "
print(a)

b="""iQuest is a trainning institute.
Here training is provided on diff technologies
"""
print(b)

c=""
print(c)
print(b)

print(a[2])

print(a[1:5])

for x in a:
    print(x)
    
# a[0]="m" # immutable
# print(a)
d=a.capitalize()
print("d=", d)
print(a.casefold()==d.casefold())
print(a.casefold())
print(a.center(14, "*"))
print(a.strip())
print(a.lstrip())
print(a.rstrip())
print(b.split(" "))