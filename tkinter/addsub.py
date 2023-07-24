from tkinter import *

def total():
    a = int(num1.get())
    b = int(num2.get())
    c = a + b
    tot.set(c)


def differ():
    a = int(num1.get())
    b = int(num2.get())
    d = a - b
    diff.set(d)


mgui = Tk()
mgui.geometry("400x350")
mgui.title("simple calculator")


num1 = StringVar()
num2 = StringVar()
tot = StringVar()
diff = StringVar()


label1 = Label(mgui, text="Num1", fg="blue", bg="white").grid(row=1, column=1)
label2 = Label(mgui, text="Num2", fg="blue", bg="white").grid(row=2, column=1)
entry1 = Entry(mgui, textvariable=num1).grid(row=1, column=2)
entry2 = Entry(mgui, textvariable=num2).grid(row=2, column=2)
entry3 = Entry(mgui, textvariable=tot).grid(row=3, column=2)
entry4 = Entry(mgui, textvariable=diff).grid(row=4, column=2)


button1 = Button(mgui, text="SUM", fg="red", bg="white", command=total).grid(
    row=3, column=1
)
button2 = Button(mgui, text="diff", fg="red", bg="white", command=differ).grid(
    row=4, column=1
)
mgui.mainloop()
