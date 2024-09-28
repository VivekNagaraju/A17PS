'''
Types of variables:
1. Instance variables/ object variables
2. Local variables/ method variables
3. Static variables/ class variables
'''
class Student:
    school="iQuest" # Static variables/ class variables
    def __init__(self, name, roll_no):
        self.name=name # instance variables
        self.roll_no=roll_no
        
    def total_marks(self, kannada, eng, hin): # local variables
        print(f"Total marks of {self.name} from {Student.school} is", kannada+eng+hin)
    
    # def get_individual_marks(self):
    #     print(kannada, eng, hin)
        
std1=Student("Vivek", 1)
std1.total_marks(100, 35, 25)