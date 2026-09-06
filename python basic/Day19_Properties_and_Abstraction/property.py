class Student:
    def __init__(self,pys,bio,math):
        self.pys=pys
        self.bio=bio
        self.math=math
    @property
    def calPercentage(self):
        return str((self.math+self.bio+self.pys)/3) +"%"
    
stu=Student(99,80,97)
print(stu.calPercentage)

stu.pys=100
print(stu.calPercentage)