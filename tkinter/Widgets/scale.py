from tkinter import *
master = Tk()
master.geometry("500x500")
w = Scale(master, from_=0, to=42)
w.pack()
w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()
master.mainloop()