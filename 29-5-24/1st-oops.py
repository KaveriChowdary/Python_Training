class Person:
    def __init__(self,name):
        self.name=name
    def say_hi(self):
        print("hey hi",self.name)
p=Person('hani') #object creation
p.say_hi()

##
class Student() :
    def __init__(self,r,n,p,a):
        self.roll= r
        self.name=n
        self.phone=p
        self.add=a
    
    def displayinfo(self):
        print(" name : ",self.name,"\n","phone :",self.phone)
s=Student(12,"hani",34579889890,"wgl")
s.displayinfo()