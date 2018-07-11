from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
from tkinter import simpledialog
import time
#===============================================functions=================================================================

filename=None

def newfile():
    global filename
    filename="Untitled"
    text.delete(0.0,END)

def savefile():
    global filename
    t=text.get(0.0,END)
    f=open(filename,mode='w')
    f.write(t)
    f.close()

def saveAs():
    f=asksaveasfile(mode='w', defaultextension='.txt')
    t=text.get(0.0,END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title='oops',message='unable to save file')

def openfile():
    f=askopenfile(mode='r')
    t=f.read()
    text.delete(0.0,END)
    text.insert(0.0,t)

def exit():
    if messagebox.askyesno("Quit","Are you sure you want to quit"):
        master.destroy()


def About():
    label=messagebox.showinfo("about"," A python alternative to notepad")

def findin():
    findString =simpledialog.askstring('Find','Enter text')
    t = text.get(0.0, END)

    # count=0
    occurences=t.upper().count(findString.upper())
    if t.upper().count(findString.upper()) > 0:
        label = messagebox.showinfo("RESULTS",findString +'has multiple occurences' + ""+ str(occurences))
    else:
        label = messagebox.showinfo('has nooccurences')

    print(t.upper().count(findString.upper()))

#=======================================================================================================================
def cut():
    text.event_generate("<<Cut>>")

def copy():
    text.event_generate("<<Copy>>")

def paste():
    text.event_generate("<<Paste>>")

def delete():
    text.delete(0.0,END)

def undo():
    text.edit_undo()

def redo():
    text.edit_redo()

def selectAll(event=None):
    text.tag_add('sel','0.0','end')
    return'break'


def tim():
    ti=time.gmtime()
    text.clipboard_append(time.asctime(ti))
    text.event_generate("<<Paste>>")

#================================================================================================================================

master=Tk()
master.title("TEXT EDITOR")
text=Text(master,width=400,height=400)
text.pack()
menu=Menu(master)
master.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label='file',menu=filemenu)
filemenu.add_command(label='New',command=newfile)
filemenu.add_command(label='Open',command=openfile)
filemenu.add_command(label='Save',command=savefile)
filemenu.add_command(label='SaveAs',command=saveAs)
filemenu.add_command(label='Find',command=findin)
filemenu.add_separator()
filemenu.add_command(label="Quit",command=exit)
editmenu=Menu(master)
menu.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Undo',command=undo)
editmenu.add_command(label='Redo',command=redo)
editmenu.add_command(label='Cut',command=cut)
editmenu.add_command(label='Copy',command=copy)
editmenu.add_command(label='Paste',command=paste)
editmenu.add_command(label='Delete',command=delete)
editmenu.add_separator()
editmenu.add_command(label='Replace')
editmenu.add_separator()
editmenu.add_command(label='Select All',command=selectAll)
editmenu.add_command(label='Time and Date',command=tim)



helpmenu=Menu(master)
menu.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='Help')
helpmenu.add_command(label='About',command=About)
mainloop()