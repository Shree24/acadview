#Question 1

'''import threading
from threading import Thread
import time
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
        time.sleep(5)
        print("Value send",self.h)
thread1=mythread(1)
thread1.start()
thread2=mythread(2)
thread2.start()

#End

#Question 2

import threading
import time
from threading import Thread
class mythread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(1,11):
            time.sleep(1)
            print(i)
t=mythread()
t.start()

#End

#Question 3


#End

# Question 4

import math
import threading
import time
from threading import Thread
from math import factorial
class a(threading.Thread):
    def __init__(self,n):
        threading.Thread.__init__(self)
        self.n=n
    def run(self):
        print("Factorial of a no. is",math.factorial(self.n))
b=int(input("Enter no"))
thread1=a(b)
thread1.start()

#End
000
#Question 3
'''
import time
import threading
class th(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        l=[1,2,3,4,5]
        a=[2,4,6,8,10]
        for i in l:
            print("number is ", l[i])
            time.sleep(int(a[i]))

t=th()
t.start()