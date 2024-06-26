# -*- coding: utf-8 -*-
"""cse111 lab 6

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ci1FfT_S_FJMM6B2MnWduf-fGa_FXj-y

task 1
"""

class Student:
  ID = 0
  def __init__(self,name, department, age ,cgpa):
    self.name = name
    self.department = department
    self.age =age
    self.cgpa = cgpa
    Student.ID+=1
  def showDetails(self):
   print(f"ID:{Student.ID}")
   print(f"Name: {self.name}")
   print(f"Department: {self.department}")
   print(f"Age: {self.age}")
   print(f"CGPA: {self.cgpa}")
  @classmethod
  def from_String(cls,X):
    name,department,age,cgpa=X.split("-")
    obj=cls(name,department,int(age),float(cgpa))
    return obj
  @classmethod
  def
s1 = Student("Samin", "CSE", 21, 3.91)
s1.showDetails()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.showDetails()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.showDetails()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.showDetails()

"""task 2"""

class Assassin:
  count = 0
  def __init__(self,jfk,oswald=100):
    self.name = jfk
    self.Success_rate = oswald
    Assassin.count+=1
  @classmethod
  def failureRate(cls,jfk,oswald):
    obj=cls(jfk,100-oswald)
    return obj
  @classmethod
  def failurePercentage(cls,name,per):
    obj=cls(name,100-int(per[0]))
    return obj
  def printDetails(self):
    print(f"Name: {self.name}\nSuccess rate: {self.Success_rate}")
    print(f"Total number of Assassin: {Assassin.count}")
john_wick = Assassin('John Wick', 100)
john_wick.printDetails()
print('================================')
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print('================================')
akabane = Assassin.failurePercentage("Akabane", "10%")
akabane.printDetails()

"""task 3"""

class Passenger:
  count =0
  def __init__(self,name):
    self.name=name
    self.fare=450
    Passenger.count+=1
  def set_bag_weight(self,num):
    if num<=20:
      self.fare=self.fare
    elif 20<num<=50:
      self.fare+=50
    elif 50<num:
      self.fare+=100
    else:
      print("Overweight")
  def printDetail(self):
    print(f"Name: {self.name}\nBus Fare: {self.fare} taka")
print("Total Passenger:", Passenger.count)
p1 = Passenger("Jack")
p1.set_bag_weight(90)
p2 = Passenger("Carol")
p2.set_bag_weight(10)
p3 = Passenger("Mike")
p3.set_bag_weight(25)
print("=========================")
p1.printDetail()
print("=========================")
p2.printDetail()
print("=========================")
p3.printDetail()
print("=========================")
print("Total Passenger:", Passenger.count)

"""task 4"""

class Travel:
  count=0
  def __init__(self,start,des):
    Travel.count+=1
    self.start=start
    self.destination=des
    self.time=1
  def set_destination(self,des):
    self.destination=des
  def set_time(self,time):
    self.time=time
  def set_source(self,start):
    self.start=start
  def display_travel_info(self):
    return f"Source: {self.start}\nDestination:{self.destination}\nFlight Time:{self.time}:00"
print("No. of Traveller =", Travel.count)
print("=======================")
t1 = Travel("Dhaka","India")
print(t1.display_travel_info())
print("=======================")
t2 = Travel("Kuala Lampur","Dhaka")
t2.set_time(23)
print(t2.display_travel_info())
print("=======================")
t3 = Travel("Dhaka","New_Zealand")
t3.set_time(15)
t3.set_destination("Germany")
print(t3.display_travel_info())
print("=======================")
t4 = Travel("Dhaka","India")
t4.set_time(9)
t4.set_source("Malaysia")
t4.set_destination("Canada")
print(t4.display_travel_info())
print("=======================")
print("No. of Traveller =", Travel.count)

"""task 5"""

class Employee:
  def __init__(self,name,wp):
    self.name=name
    self.workingPeriod=wp
  @classmethod
  def employeeByJoiningYear(cls,name,year):
    obj= cls(name,2023-year)
    return obj
  @staticmethod
  def experienceCheck(exp,gender):
    if exp<3 and gender=="male":
      return f"He is not experienced"
    elif exp<3 and gender=="male":
      return f"She is not experienced"
    elif exp>=3 and gender=="female":
      return f"She is experienced"
    elif exp>=3 and gender=="male":
      return f"He is experienced"
employee1 = Employee('Dororo', 3)
employee2 = Employee.employeeByJoiningYear('Harry', 2016)
print(employee1.workingPeriod)
print(employee2.workingPeriod)
print(employee1.name)
print(employee2.name)
print(Employee.experienceCheck(2, "male"))
print(Employee.experienceCheck(3, "female"))

"""task 6"""

class Laptop:
  laptopCount=0
  def __init__(self,name,amo):
    self.name=name
    self.count=amo
    Laptop.laptopCount+=amo
  @classmethod
  def advantage(cls):
    print("Laptops are portable")
  @classmethod
  def resetCount(cls):
    Laptop.laptopCount=0






lenovo = Laptop("Lenovo", 5)
dell = Laptop("Dell", 7)
print(lenovo.name, lenovo.count)
print(dell.name, dell.count)
print("Total number of Laptops", Laptop.laptopCount)
Laptop.advantage()
Laptop.resetCount()
print("Total number of Laptops", Laptop.laptopCount)

"""task 7"""

class Cat:
  Number_of_cats = 0
  def __init__(self,color,position):
    self.color=color
    self.position=position
    Cat.Number_of_cats+=1
  @classmethod
  def no_parameter(cls):
   obj= cls("White","sitting")
   return obj
  @classmethod
  def first_parameter(cls,x):
    obj=cls(x,"sitting")
    return obj
  @classmethod
  def second_parameter(cls,y):
    obj=cls("White",y)
    return obj
  def printCat(self):
    print(f"{self.color} cat is {self.position}")
  def changeColor(self,z):
    self.color=z
print("Total number of cats:", Cat.Number_of_cats)
c1 = Cat.no_parameter()
c2 = Cat.first_parameter("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c5 = Cat.second_parameter("playing")
print("=======================")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c5.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
print("=======================")
print("Total number of cats:", Cat.Number_of_cats)

"""task 8

"""

import math
class Cylinder:
  height=18
  radius=5
  def __init__(self,radius,height):
    self.radius = radius
    self.height=height
    print(f"Default radius={Cylinder.radius} and height={Cylinder.height}")
    Cylinder.height=height
    Cylinder.radius=radius
    print(f"Updated: radius={Cylinder.radius} and height={Cylinder.height}")
  @staticmethod
  def area(x,y):
    area=2*math.pi*(x**2)+2*math.pi*x*y
    print(f"Area: {area}")
  @staticmethod
  def volume(x,y):
    volume=math.pi*x**2*y
    print(f"Volume: {volume}")
  @classmethod
  def swap(cls,x,y):
    obj = cls(y,x)
    return obj
  @classmethod
  def changeFormat(cls,x):
    c = x.split("-")
    for i in c:
      a = float(c[0])
      b = float(c[1])
      obj=cls(a,b)
      return obj


c1 = Cylinder(0,0)
Cylinder.area(c1.radius,c1.height)
Cylinder.volume(c1.radius,c1.height)
print("===============================")
c2 = Cylinder.swap(8,3)
c2.area(c2.radius,c2.height)
c2.volume(c2.radius,c2.height)
print("===============================")
c3 = Cylinder.changeFormat("7-13")
c3.area(c3.radius,c3.height)
c3.volume(c3.radius,c3.height)
print("===============================")
Cylinder(0.3,5.56).area(Cylinder.radius,Cylinder.height)
print("===============================")
Cylinder(3,5).volume(Cylinder.radius,Cylinder.height)

"""task 9"""

class Student:
  total=0
  brac=0
  other=0
  def __init__(self,name,dept,uni="BRAC University"):
    self.name=name
    self.dept=dept
    self.uni=uni
    Student.total+=1
    if uni=="BRAC University":
      Student.brac+=1
    else:
      Student.other+=1
  @classmethod
  def printDetails(cls):
    print(f"Total Student(s): {Student.total}\nBRAC University Student(s): {Student.brac}\nOther Institution Student(s): {Student.other}")
  def individualDetail(self):
    print(f"Name: {self.name}\nDepartment: {self.dept}\nInstitution: {self.uni}")
  @classmethod
  def createStudent(cls,name,dept,uni="BRAC University"):
    obj=cls(name,dept,uni)
    return obj
Student.printDetails()
print('#########################')

mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()

print('========================')

harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()

print('=========================')

levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()

class SultansDine:
  branch=0
  taka=0
  lst=[]
  def __init__(self,dest):
    self.destination=dest
  @classmethod
  def details(cls):
    print(f"Total Number of branch(s): {SultansDine.branch}\nTotal Sell: {SultansDine.taka} Taka")