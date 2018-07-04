# QUESTION 1

from tkinter import *
root=Tk()
d={"name":"a","mobilenumber":123}
l=Label(root,text="keys")
l.pack()
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
mylist=Listbox(root,yscrollcommand=scrollbar.set)
for i in d:
    d.get(i)
    mylist.insert(END,"The key is"+ str(i))
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)


#QUESTION 2

def items():
    d.update({"age":22,"address":"abc"})
    print(d)
button=Button(root,text="abc",command=items())
button.pack()
root.mainloop()

