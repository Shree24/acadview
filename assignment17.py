# QUESTION 1

from tkinter import *
root=Tk()
def hello():
    print("hello world")
b=Button(root,text="hello",command=hello)
b.pack()
c=Button(root,text="EXIT",command="exit")
c.pack()
root.mainloop()

# END

# QUESTION 2

from tkinter import *
root=Tk()
def hello():
    print("hello world")
b=Button(root,text="hello",command=hello)
def text():
    print("Acadview")
b.pack()
c=Button(root,text="EXIT",command="exit")
c.pack()
d=Button(root,text="action",command=text)
d.pack()
root.mainloop()
#END

# QUESTION 3

from tkinter import *
root=Tk()
f=Frame(root)
f.pack()
l=Label(root,text="Acad")
def change():
    l.config(text="abc")
l.pack()
b1=Button(root,text="a",command=change)
b1.pack()
b2=Button(root,text="Exit",command="exit")
b2.pack()
root.mainloop()

# END

#QUESTION 4

from tkinter import *
root=Tk()
l=Label(root,text="First name").grid(row=0)
la=Label(root,text="Second name").grid(row=1)
e1=Entry(root)
e2=Entry(root)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
root.mainloop()




