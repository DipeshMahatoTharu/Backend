# youtubelink=https://www.youtube.com/watch?v=bAwmZVJeO5s&t=1985s

# class Student:
#     def __init__(self,name):
#         self.name=name

# s1=Student("Dipesh")

# del s1.name
# print(s1.name)


# class Account:
#     def __init__(self,Acc_name,Acc_pass):
#         self.Acc_name=Acc_name
#         self.__Acc_pass=Acc_pass

#     def reset(self):
#         print(self.__Acc_pass)

# acc1=Account("3131414114414","sakdmasd")

# acc1.Acc_name
# # acc1.reset()
# acc1.__Acc_pass



class Car:
    @staticmethod
    def start():
        print("Car Started")
    @staticmethod   
    def stop():
        print("car Stoped ..")
class Toyota(Car):
    def __init__(self,name):
        self.name=name

car1=Toyota("Fortunar")
car1.start()
car1.stop()