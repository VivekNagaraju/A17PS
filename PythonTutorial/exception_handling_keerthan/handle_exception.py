'''
Exception handling: Handling of unusual circumstances which occur during run-time (run-time errors, logical errors)

Errors: complie-time/ syntax errors, run-time errors, logical errors

complie-time/ syntax errors programmer is sole responsible. It should be fixed before executing the pogram

Cases:
1. One try - one default except
2. One try - one default except with message 
3. One try - one error specific except
4. One try - multiple error specific except blocks
5. One try - multiple error specific except blocks along with default except block
6. Nested try-except inside another try block
'''
print(1+2)
print(4*5)
print(10-6)
# print(78/"abc")
try:
    
    try:
        print(78/0)
    
    except ZeroDivisionError as ze:
        print(78/"hjga")
#
# except TypeError as te:
#     print("Type error")

# except (ZeroDivisionError, TypeError) as zte:
#     print("Zero divison error/ Type error")
    
except Exception as e:
    print(e)
print(5**3)
print(96%4)

