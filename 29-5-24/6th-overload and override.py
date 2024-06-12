'''#overloading
class Product:
    def disp(self):
        print("this is a product info")
    def disp(self,name):
        print("the name of the product is",name)
p1=Product()
p1.disp()
p1.disp("dell")    ### it doesnot support the overloading bur overriding can be possible'''
#overloading happpens in same class ,multiple  same methiods in same class
#overriding happens in different class , same methods in two different classes

#overriding
class Product:
    def disp(self):
        print("this is a product info")
class Cal(Product):
    def disp(self):
        print("this is a calculator info")
        super().disp()
p1=Cal()
p1.disp()

##
class A:
    def __str__(self):
        return 'hi'
class B(A):
    def __init__(self):
        super().__init__()
class C(B):
    def __init__(self):
        super().__init__()
def main():
    obj1=B()
    obj2=C()
    obj3=A()
    print(obj1,obj2,obj3)
main()

##
class A:
    def __init__(self):
        self.m=5
    def __str__(self):
        return str(self.m)
obj=A()
print(obj)


#
class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return 1
    def __eq__(self,other):
        return self.x*self.y==other.x*other.y
o1=A(5,2)
o2=A(2,5)
print(o1==o2) #whenever objects are compared then __eq__ invokes and checks for the condition