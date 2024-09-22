'''
Created on 22-Sep-2024

@author: admin
'''
class HumanBeings:
    def __init__(self, name):
        self.name=name
        
    def walk(self):
        print(f"{self.name} is walking")
        
    def run(self):
        print(f"{self.name} is running")
        
object1=HumanBeings("Vivek")
object1.run()
object1.walk()
print(object1.name)

object2=HumanBeings("Megha")
object2.run()
object2.walk()
print(object2.name)
object1.run()