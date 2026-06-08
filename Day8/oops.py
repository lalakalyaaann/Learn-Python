# #class
class student :
    name="Kalyan"
#object
s1=student()
print(s1)
print(s1.name)


class car:
    color="red"
    brand="Mercedes"
c1=car()
print(c1.color)
print(c1.brand)

#constructor
#__init__ function: invoked when object is created

class student :
    name="Kalyan"
    def __init__(self):
         print(self)
         print("Creating object...")

s1=student()


class student :

    def __init__(self,name,marks):
         self.name=name
         self.marks=marks
         print("Creating object...")

s1=student("Kalyan",98)
print(s1.name,s1.marks)
s2=student("Ishan",90)
print(s2.name,s2.marks)


#methods
class student :
    college_name="PN Campus"
    def __init__(self,name,marks):
         self.name=name
         self.marks=marks
         print("Creating object...")
    def welcome(self):
         print(self.name,"Welcome to hello world.")
    def get_marks(self):
         print(self.marks)

s1=student("Kalyan",91)
s1.welcome()
s1.get_marks()

"""Create a student class that takes name and marks of 3 subjects
as arguments in constructor. Then create a method to calculate average"""
class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def calc_avg(self):
        sum=0
        for value in self.marks:
            sum+=value
        print("hi ",self.name, ". Your average marks is ", sum/3)


s1=Student("Kalyan Dhamala",[99,92,82])
s1.calc_avg()

#static methods
@staticmethod
def hello():
    print("No self argument passed.. Static Method")

hello()