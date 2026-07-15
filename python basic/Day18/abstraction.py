#abstraction only show improtant things 
class Car:
    def __int__(self):
        self.acc=False
        self.brk=True
        self.clu=False
    
    def start(self):
        self.clu=True
        self.acc=True
        print("car Started ")
        
car1=Car()
car1.start()
    