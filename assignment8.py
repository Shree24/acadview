#QUESTION 1

#A time tuple is the usage of a tuple (list of ordered items/functions) for the ordering and notation of time.
#The tuple used for time in Python-based systems can be largely summarized as ordering by year (value of 1970 or higher),
#month (1 to 12), day (1 to 31), hour (0 to 23), minutes (0 to 59), seconds (0 to 59), day of the week (0 to 6,
#where 0 = Monday and 6 = Sunday),day of the year (1 to 366), and finally a DST (Daylight Savings Time) value of either
#-1 (“fall back”), 0 (“normal”),
#+1 (“spring forward”.                             #time tuple

#END

#QUESTION 2

import datetime,time                               # get formatted time
print(time.asctime(time.localtime()))

#END

#QUESTION 3

import datetime                                    #extract month from time
print(datetime.date.today().month)

#END

#QUESTION 4

from datetime import date
print(datetime.date.today().day)                   #extract day from time

#END

#QUESTION 5

import datetime
d=datetime.date.today()
d.strftime("%d%m%y")                                #extract date from time
print(d.day)


#QUESTION 6

import math
n=int(input("enter no."))                            #find factorial
print(math.factorial(n))

#END

#QUESTION 7

from math import gcd
n=int(input("enter number"))                          # find gcd
m=int(input("enter number"))
print(math.gcd(n,m))

#END

#QUESTION 8

import os
print(os.getcwd())
print(os.name)                                        # use os package
print(os.environ)
#END