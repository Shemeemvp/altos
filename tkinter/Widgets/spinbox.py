from tkinter import *

master = Tk()
master.geometry("300x300")
w = Spinbox(master, from_=0, to=10)
w.pack()
master.mainloop()
