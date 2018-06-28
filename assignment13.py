# QUESTION 1

'''
a=3
 if a<4:
    a=a/(a-3)                                             # zero division error as a=3 and a=3/(3-3)=3/0 so no division
     print(a)                                             error occurs

'''
try:
    a=3
    if a<4:
        a=a/(a-3)
except ZeroDivisionError:
    print("No. is divisible by zero")
else:
    print(a)

# END

#QUESTION 2

try:
    l=[1,2,3]
    print(l[3])                                             # index error as in list l there is no. in index 3
except IndexError:
    print("index not found")

# END

#QUESTION 3

try:
    raise NameError("Hi there")  # Raise Error
except NameError:                # it will print an exception
    print("An exception")

# END

# QUESTION 4(a)
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
		print(c)
AbyB(2.0, 3.0)

#(b)

def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
		print(c)
AbyB(3.0, 3.0)

# END

# QUESTION 5

try:
    import smaily
    l=["a","b","c"]
    print(l[3])
except ImportError:
    print("file doesn't exist")
except IndexError:
    print("index not found")
except ValueError:
    print("value should be in Int")

# END

# QUESTION 6

class AgeError(Exception):
    pass
try:
    a=int(input("enter age"))
    if(a<18):
        raise AgeError
except ValueError:
    print("Please enter Int")
except AgeError:
    print("younger")
else:
    print("you are eligible")

# END