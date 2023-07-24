from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Simple Calculator")

menuBar = Menu(root)
root.config(menu=menuBar)
fileMenu = Menu(menuBar)
menuBar.add_cascade(label = "Menu", menu= fileMenu)
fileMenu.add_command(label= "New")
fileMenu.add_separator()
fileMenu.add_command(label= "Exit", command=root.quit)

helpMenu = Menu(menuBar)
menuBar.add_cascade(label= "Help", menu=helpMenu)
helpMenu.add_command(label="Help")


num1 = StringVar()
num2 = StringVar()
total = StringVar()
differ = StringVar()
product = StringVar()
quotient = StringVar()

def sum():
    fnum = int(num1.get())
    snum = int(num2.get())
    resSum = fnum + snum
    total.set(resSum)

def dif():
    fnum = int(num1.get())
    snum = int(num2.get())
    resDif = fnum - snum
    differ.set(resDif)

def prod():
    fnum = int(num1.get())
    snum = int(num2.get())
    resProd = fnum * snum
    product.set(resProd)

def div():
    fnum = int(num1.get())
    snum = int(num2.get())
    resDiv = fnum / snum
    quotient.set(resDiv)

lab1 = Label(root, text="First Number", fg="red",width=15,height=1,padx=7,pady=4).grid(row=1, column=1)
ent1 = Entry(root, textvariable=num1).grid(row=1, column=2)
lab2 = Label(root, text="Second Number", fg="red",width=15,height=1,padx=7,pady=4).grid(row=2, column=1)
ent2 = Entry(root, textvariable=num2).grid(row=2, column=2)

but1 = Button(root, text="SUM",fg="blue", bg="lightgray",width=10,height=1,padx=7,pady=4, command=sum).grid(row=3, column=1)
ent3 = Entry(root, textvariable=total).grid(row=3, column=2)
but2 = Button(root, text="DIFFERENCE",fg="blue", bg="lightgray",width=10,height=1,padx=7,pady=4, command=dif).grid(row=4, column=1)
ent4 = Entry(root, textvariable=differ).grid(row=4, column=2)
but3 = Button(root, text="PRODUCT",fg="blue", bg="lightgray",width=10,height=1,padx=7,pady=4, command=prod).grid(row=5, column=1)
ent5 = Entry(root, textvariable=product).grid(row=5, column=2)
but4 = Button(root, text="QUOTIENT",fg="blue", bg="lightgray",width=10,height=1,padx=7,pady=4, command=div).grid(row=6, column=1)
ent6 = Entry(root, textvariable=quotient).grid(row=6, column=2)

root.mainloop()
