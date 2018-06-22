#QUESTION 1
import math
class circle():
    def __init__(self,radius):
        self.r=radius
    def getArea(self):
        return math.pi*(self.r**2)
    def getCircumference(self):
        return 2*math.pi*self.r

r=int(input("Enter radius of circle"))
c=circle(r)                                      #initialize class circle with radius
print(c.getArea())
print(c.getCircumference())

#END

#QUESTION 2

class student():
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def Display(self):
        print("The name of student is"+ self.name)
        print("The age of student is"+ self.rollno)   #display age and name
n=input("Enter name")
g=input("Enter age")
a=student(n,g)
a.Display()

#END
#QUESTION 3
class Temperature:
    def __init__(self,c,a):
        self.celsius=c
        self.fahrenheit=a
    def convertFahrenheit(self):
        f=self.celsius*1.8000+32.00
        print("The temperature in fahrenheit is",f)                #temperature conversions
    def convertCelsius(self):
        e=self.fahrenheit*0.56-32.00
        print("The temperature in celsius is",e)
h=float(input("Enter temperature in celsius"))
i=float(input("Enter temperature in fahrenheit"))
obj=Temperature(h,i)
obj.convertFahrenheit()
obj.convertCelsius()

#END

#QUESTION 4

class MovieDetails():
    reviews="one time watch"
    def __init__(self,Moviename,artistname,Yearofrelease,ratings):
        self.m=Moviename
        self.a=artistname
        self.y=Yearofrelease
        self.r=ratings
    def Display(self):
        print("Moviename is",self.m)
        print("Artistname is",self.a)
        print("Year of realease is",self.y)
        print("Ratings is",self.r)
    def Update(self):
        print("The updaed details are",self.reviews)
i=input("Enter moviename")
j=input("Enter artistname")
k=input("Enter year os release")                              #display and update movie details
l=input("Enter ratings")
d=MovieDetails(i,j,k,l)
d.Display()
f=MovieDetails(i,j,k,l)
f.reviews="must watch"
f.Update()

#END

#QUESTION 5

class Expenditure():
    def __init__(self,expenditure,savings):
        self.e=expenditure
        self.s=savings
    def Display(self):
        print("Expenditure is",self.e)
        print("Salary is",self.s)
    def calculate(self):
        a=self.e+self.s
        print("Total salary is",a)
                                                      #display total salary
b=int(input("Enter expenditure"))
c=int(input("Enter savings"))
obj=Expenditure(b,c)
obj.Display()
obj.calculate()

#END








