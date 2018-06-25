#Question 1

class Animal:                                           # defined class animal
    def animal_attribute(self):
        print("Animals are multicellular")              # properties of animals
class Tiger(Animal):                                    # defined class tiger, inheritance
    def tiger_attribute(self):                          # property of tiger
        print("Embodiment of physical power")
a=Animal()                                              #function call
b=Tiger()
a.animal_attribute()
b.tiger_attribute()
b.animal_attribute()

#End

#Question 2

class A:                                       # defined class A
    def f(self):                               # method or function f
        return self.g()

    def g(self):                                # method g
        return 'A'

class B(A):                                     # inheritance
    def g(self):                                # overriding as same function name in A and B so return in base class
        return 'B'                              # is overridden with derived or child class

a = A()                                         # function call
b = B()
print (a.f(), b.f())
print (a.g(), b.g())

# End

# Question 3

#class Cop:
    #def __init__(self,name,age,work_experience,designation):
        #self.n=name
       # self.a=age
       # self.w=work_experience
        #self.d=designation
   # def add(self):
        #name=input("Enter name")
        #age=input("Enter age")
        #work_experience=input("Work experience")
        #designation=input("add designation")
    #def display(self):
      #  print("The  following details")
   # def update(self,name,age,work_experience,designation):
    #    self.q=name
     #   self.t=age
      #  self.u=work_experience
       # self.i=designation
        #print("name=",self.q)
        #print("age=",self.t)
        #print("work_experience=",self.u)
        #print("designation=",self.i)
#class Mission(Cop):
 #   def add_mission(self):
  #      print("Mission details")
#n=print("enter name")
#y=print("enter age")
#p=print("enter work_experience")
#g=print("enter designation")
#j=Cop(n,y,p,g)
#o=Mission(n,y,p,g)
#j.add()
#j.display()
#j.update()
#o.add_mission()
#  Question 4
class shape:                                             # class shape
    def __init__(self,length,breadth):                   # initialized object
        self.l=length
        self.b=breadth
    def Area(self):                                      # function Area
        print("Area of rectangle is",self.l*self.b)
        print("Area of square is",self.l*self.l)
j=int(input("Enter length"))
k=int(input("Enter breadth"))
s=shape(j,k)
s.Area()

#End





