'''
Operators: it is a symbol which does the operation (+, -, *,/ etc)
Operation: process of operating (add, sub, mul., div etc.,)
Operands: on which operation is done (variables- a, b)

Types of Operators:
1. Airthmetic Operators: +, -, *, /, %, **, // ; i/p= num, o/p= num
2. Relational/ Comparison Operators: <, >, <=, >=, ==, !=; i/p= num, o/p=bool
3. Assignment Operator: =
4. Logical Operators: AND, OR, NOT; i/p= bool(True, False), o/p= bool
5. Membership Operators: in, not in
6. Identity Operators: is, is not
'''
print("========Airthmetic Operators=======")
a=3
b=7
c=a+b
print("a+b", a+b)
print("a-b", a-b)
print("a*b", a*b)
print("b/a", b/a)
print("a**b", a**b)
print("b//a", b//a)
print("b%a", b%a)

print("========Relational/ Comparison Operators=======")
print("a=", a)
print("b=", b)
print("a<b", a<b)
print("a>b", a>b)
print("a<=b", a<=b)
print("a>=b", a>=b)
print("a==b", a==b)
print("a!=b", a!=b)

print("========Logical Operators========")
print("AND Operator")
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print("OR Operator")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print("NOT Operator")
print(not True)
print(not False)

print("======Membership Operators=====")
print("v" in "Vivek")
print("a" not in "Vivek")
print("v" not in "Vivek")
print("a"  in "Vivek")

print("======Identity Operators======")
e=6
f=6
print(id(e))
print(id(f))
print(e is f)
g=7
h=8
print(id(g))
print(id(h))
print(g is not h)