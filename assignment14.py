# QUESTION 1

f=open("abc","r")
a=(f.readlines())                        # read lines of a file
a.reverse()
n=int(input("enter no. of lines"))
for i in range(0,n):
    print(a[i])
f.close
# END

# QUESTION 2

d="python"
f=open("abc","r")                       # COUNT FREQUENCY OF WORDS IN FILE
b=f.read()
c=b.split()
e=b.count(d)
print(e)

#END

# QUESTION 3
f=open("abc","r")
q=(f.readlines())                       # COPY CONTENTS OF A FILE
t=open("cd","a")
t.writelines(q)

# END

# QUESTION 4
with open("abc")as f,open("cd")as f1:
    for line1,line2 in zip(f,f1):
        print(line1+line2)

# END

# QUESTION 5

import random
afile=open("Random.txt","w")
for i in range(int(input("how many random numbers?:"))):
        line=str(random.randint(1,10))
        afile.write(line)
        print(line)
afile.close()




