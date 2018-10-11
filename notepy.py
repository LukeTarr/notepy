'''
Author: Luke Tarr
'''
from tkinter import *
from tkinter.filedialog import *

filename = None

#Functions for handling creation/opening of files
def new_file():
    global filename
    filename = "Untitled"

    text.delete(0.0, END)

def save_file():
    global filename
    
    fullText = text.get(0.0, END)

    try:
        fileToWrite = open(filename, 'w')
        fileToWrite.write(fullText)
        fileToWrite.close()
    except:
        showerror(title="Error", message="Unable to use saveFile")

def save_as():
    fileTo = asksaveasfile(mode='w')
    fullText = text.get(0.0, END)

    try:
        fileTo.write(fullText.rstrip())
    except:
        showerror(title="Error", message="Unable to use saveAs")

def open_file():
    global filename

    filepath = askopenfile(mode='r')
    data = filepath.read()
    filename = filepath.name
    
    text.delete(0.0, END)
    text.insert(0.0, data)


#Using Tkinter to create GUI
root = Tk()
root.title("notepy")

root.minsize(width=400, height=400)

text = Text(root, width=400, height=400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)

filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Save As", command=save_as)

filemenu.add_separator()

filemenu.add_command(label="Quit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

root.mainloop()