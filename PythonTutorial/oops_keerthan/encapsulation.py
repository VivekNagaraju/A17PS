'''
Encapsulation: Restricting the access to properties/members of a class
1. Protected members: can be accessed within a class and its sub-classes. 
    Prefix- '_'. Ex: _a=2
2. Private members: can be accessed within the same class only.
    Prefix- '__'. Ex: __a=2
'''
class Student:
    def __init__(self, name, roll_no, contact):
        self.name=name
        self._roll_no=roll_no # Protected variable
        self.__contact=contact # Private member
        
    def display_details(self):
        print(f"""
            Name: {self.name},
            roll_no: {self._roll_no},
            Contact: {self.__contact}
        """)


std1=Student("Keerthan", 7, 8861911092)
std1.display_details()
std1.roll_no=70
std1.display_details()
std1._roll_no=700
std1.display_details()
std1.__contact=0000000000
std1.display_details()
print(dir(std1))
std1._Student__contact=000000000 # Name mangling
std1.display_details()