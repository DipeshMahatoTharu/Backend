# # youtube link =




class Name:
    #clas variable 
    college="Hearld College Kathmandu "

    def __init__(self,name,marks):
        self.marks=marks
        #object full new variable made and name is constructor 
        self.name=name 
        
    def welcome(self):
        print(f"Hi , {self.name}")

    def ger_marks(self):
        return self.marks



        
name1=Name("Kritika Pandey",90)
print(f"{name1.name} is studying in {Name.college}")

print(name1.ger_marks())




name1.welcome()



name1.name="Dipesh"
print(name1.name)




