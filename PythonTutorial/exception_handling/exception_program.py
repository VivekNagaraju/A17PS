'''
Created on 29-Sep-2024

@author: admin
'''
print(1+2)
print(3*5)
try:
    try:
        print(6/0)
# except ZeroDivisionError as ze:
#     print(ze)
# except TypeError as te:
#     print(te)
# except:
#     print("Exception occured")
    except (ZeroDivisionError, TypeError) as e:
        print(6/"nhgfc")
except Exception as e:
    print(e)
print(9^2)
