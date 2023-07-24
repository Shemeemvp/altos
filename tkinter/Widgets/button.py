from tkinter import *
from tkinter import messagebox

top = Tk()  
top.geometry("400x400")  
def funRed():  
    messagebox.showinfo("TKinter", "RED Button clicked")

def funGreen():  
    messagebox.askquestion("TKinter", "Are You Sure to select GREEN")

def funBlue():  
    messagebox.showerror("TKinter", "Woops! Something went wrong with BLUE..")

def funYellow():  
    messagebox.showwarning("TKinter", "YELLOW button")

b1 = Button(top,text = "Red",command = funRed,activeforeground = "red",
activebackground = "white",bg='red',fg='white',pady=10)  
b2 = Button(top, text = "Blue",command=funBlue,activeforeground = "blue",
activebackground = "white",bg='blue',fg='white',pady=10)  
b3 = Button(top, text = "Green",command=funGreen,activeforeground = "green",
activebackground = "white",bg='green',fg='white',pady = 10)
b4 = Button(top, text = "Yellow",command=funYellow,activeforeground = "black",
activebackground = "white",bg='yellow',fg='black',pady = 10)  
b1.pack(side = LEFT)  
b2.pack(side = RIGHT)  
b3.pack(side = TOP)  
b4.pack(side = BOTTOM)  
top.mainloop()