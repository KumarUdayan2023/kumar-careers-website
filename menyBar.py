from tkinter import *
from tkinter import filedialog

def openFile():
    print('This file is already opened!')

def saveFile():
    print("This file is saved!!")

def cut():
    print("You cut some text!!")

def copy():
    print("You copy some text!!")

def paste():
    print("You paste some text..")

window10 = Tk()
window10.title('My Project')
window10.geometry('500x500')

menubar1 = Menu(window10)
window10.config(menu=menubar1)

copyImage = PhotoImage(file='copy.png').subsample(10,10)
saveImage = PhotoImage(file='save.png').subsample(6, 6)

fileMenu = Menu(menubar1)
menubar1.add_cascade(label='file',menu=fileMenu, font=('MV Boli',25))
fileMenu.add_command(label='Open', command=openFile)
fileMenu.add_command(label='Save', command=saveFile, image=saveImage, compound=LEFT)
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=quit)

editMenu= Menu(menubar1)
menubar1.add_cascade(label='Edit',menu=editMenu, font=('MV Boli',25))
editMenu.add_command(label='Cut', command=cut)
editMenu.add_command(label='Copy', command=copy,image=copyImage, compound=LEFT)
editMenu.add_command(label='Paste', command=paste)





window10.mainloop()