'''
Created on 12-Oct-2024

@author: admin
'''
class GrandFather:
    def __init__(self, name, age):
        print(f"This is GF Constructor with {name} and {age}")
        
    def gf_method(self):
        print("This is GF method")
        
class Father(GrandFather):
    # def __init__(self):
    #     print("This is Father Constructor")
    def __init__(self, name, age, adhaar_no):
        # print(f"This is Father Constructor with {name}, {age} and {adhaar_no}") 
        super().__init__(name, age) 
        print(f"adhaar_no is {adhaar_no}")  
        
    def f_method(self):
        print("This is father method")

ajja=GrandFather("ajja", 96)
appa=Father("appa", 66, 9896987)