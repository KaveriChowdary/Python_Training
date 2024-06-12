class Test:
    def __init__(self):
        self.x=0
class Derived_Test(Test):
    def __init__(self):
        Test.__init__(self)
        self.y=1
def main():
    b=Derived_Test()
    print(b.x,b.y)
main()

##
class A:
    def __init__(self,z):
        self.z=z
class B(A):
    def __init__(self,z,x):
        super().__init__(x)
        self.z=z
    def p(self):
        print(self.z,A(12).z)
obj=B(10,15)
obj.p()

##
class A:
    def __init__(self,x=3):
        self._x=x
class B(A):
    def __init__(self):
        super().__init__(5)
    def disp(self):
        print(self._x)
def main():
    obj=B()
    obj.disp()
main()