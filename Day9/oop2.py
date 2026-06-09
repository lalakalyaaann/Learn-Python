#del keyword 
class student:
    def __init__(self,name):
        self.name=name

s1=student("Kalyan") #s1 object is created 
print(s1)
del s1    #s1 object is deleted 
print(s1)  #s1 object doesnot exist


#private attribute and methods

class Person:
    #private attribute
    __name="No name"
    #private method 
    def __hello():
        print("Hello, This is private method.")
p1=Person()
print(p1.__name)
print(p1.__hello())


class Person:
    #private attribute
    __name="kalyan"
    #private method 
    def __hello(self):
        print("Hello, This is private method.")
    #friend function
    def welcome(self):
          self.__hello()

p1=Person()
print(p1.welcome())


#inheritance 
#single inheritance 

class Car:
    @staticmethod
    def start():
        print("Car Started!")
    @staticmethod
    def stop():
        print("Car stopped! ")
class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("Fortuner")
car2=ToyotaCar("Datsun")
print(car1.name)
print(car1.start())  #inherited from car class


#multilevel inheritance  

# class Car:
    @staticmethod
    def start():
        print("Car Started!")
    @staticmethod
    def stop():
        print("Car stopped! ")
class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand
class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type

car1=Fortuner("Diesel")
car1.start()

#multiple inheritance 


class A:
    varA="Welcome to section A"
class B:
    varB="Welcome to section B"
class C(A,B):
    varC="Welcome to section C"

c1=C()
print(c1.varC)
print(c1.varA)
print(c1.varB)

#super method 
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():,
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("prius", "electric")
print(car1.type)

#class method 

class Person:
    name="annonymous"

    @classmethod,
    def changeName(cls,name):
        cls.name=name
p1=Person()
p1.changeName("Kalyan")
print(p1.name)
print(Person.name)

#property decorator

class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    @property
    def percentage(self): 
        return str((self.phy +self.chem +self.math)/3)+"%"



stu1=Student(91,95,99)
print(stu1.percentage)
stu1.phy=86
print(stu1.percentage)


#polymorphism

#implicit overloading
print(1+2) #sum
print("Kalyan "+"is "+"student") #concatenate
print([1,2,3]+[4,5]) #merges 


#operator overloading 
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def ShowNumber(self):
        print(self.real, "i +",self.img , "j")
    
    def __add__(self,num2):
        newreal=self.real + num2.real
        newimg=self.img+ num2.img
        return Complex(newreal,newimg)
    def __sub__(self,num2):
        newreal=self.real -num2.real
        newimg=self.img- num2.img
        return Complex(newreal,newimg)

num1=Complex(1,3)
num1.ShowNumber()

num2=Complex(2,5)
num2.ShowNumber()
# num3=num1.add(num2)
# num3.ShowNumber()
num3=num1+num2
num3.ShowNumber()

num4=num1-num2
num4.ShowNumber()