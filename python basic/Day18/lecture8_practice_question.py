class Student:
    def __init__(self,name,marks):
         self.name=name
         self.marks=marks

    def get_marks(self):
        sum=0
        for val in self.marks:
            sum+=val
        
        return sum/3
    def show(self):
        print(f"HI,{self.name} Your average marks is {self.get_marks()}")
s1=Student("Dipesh",[90, 90 ,95])

print(s1.show())