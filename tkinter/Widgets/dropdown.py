from tkinter import *

top = Tk()
top.geometry("715x250")
menu = StringVar()
menu.set("Select Country")
drop = OptionMenu(top, menu, "India", "USA", "UAE", "Qatar", "Germany", "Russia")
drop.pack()
top.mainloop()
