from tkinter import *

def create_window():
    new_window1 = Tk()
    old_windows.destroy()
    new_window1 = old_windows
    Button(old_windows, text="creat a new window", command=create_window).pack()
old_windows = Tk()

Button(old_windows, text="creat a new window",command=create_window).pack()


old_windows.mainloop()

