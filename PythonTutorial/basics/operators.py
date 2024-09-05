'''
Created on 04-Sep-2024
"Operation is process of operating operands by an operator"

Operator: Is a symbol which is applied on operands to perform some 
specific action/ task/ operation

Types of Operators:
1. Arithmetic Operators: +, -, *, /, %, **, // #binary operators
2. Relational/ Comparison Operators: >, <, <=, >=, ==, !=
3. Assignment Operator: = # Unary Operator (Minus operator - to store negative value in an variable)
4. Logical Operators: AND, OR, NOT
5. Membership Operators: in, not in
6. Identity Operators: is, is not
7. Shifting Operators: Left Shift(<<), Right Shift(>>)
8. bitwise operators: &(bitwise and), |(bitwise or), ~ (bitwise not)

# Ternary Operators
'''

a=5
b=5
# print(a/b)
# print(a%b)
# print(a//b)
print(2**3)

print("=======Relational Operators=======")
print(76>7)
print(76<7)
print(7!=7)
print(a==b)

print("=======and========")
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print("=======or========")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print("=======not========")
print(not True)
print(not False)

print("=======membership operators========")
print("v" in "Vivek")
print("a" in "Vivek")
print("v" not in "Vivek")
print("a" not in "Vivek")
print("K" in "Vivek")

print("=======identity operators========")
print(id(a))
print(id(b))
print(a is b)

print("=======shift operators========")
"""
5 = 0000 0101 
-6 =  1111 1010
10= 1010
2 = 0010
"""
print(bin(5))
print(5 << 2)
print(bin(20))
print(5 >> 1)
print(bin(2))

print("=======bitwise operators========")

c=2 | 10
print(c)
print(bin(c))

a=5
b=~5
print(b)
print(bin(a))
print(bin(b))
