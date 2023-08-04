import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("370x550")
root.title("Calculator")
root.resizable(False,False)
root.configure(bg='#0b569c')

# icon = PhotoImage(file='icon.ico')
# root.iconphoto(False, icon)

menuBar = Menu(root)
root.config(menu=menuBar)
fileMenu = Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Clear", command=lambda:clearLabel())
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)

helpMenu = Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="Help")
helpMenu.add_command(label="About")

res_label = ""
def show(value):
    global res_label
    res_label+=value
    result_label.config(text=res_label)


def clearLabel():
    global res_label
    res_label = ""
    result_label.config(text=res_label)

def calculate():
    global res_label
    result = ""

    if res_label != "":
        try:
            result = eval(res_label)
        except:
            result = "Invalid"
            res_label = ""
    result_label.config(text = result)

result_label = Label(root,font=("arial",25),bd=5,relief=RAISED)
result_label.place(x=10,y=10,width=350,height=80)

Button(root, text="C", width=3, height=1 ,bd=3, relief=RIDGE, font=('arial',30,'bold'),fg='cyan',bg='#858b94',command=lambda:clearLabel()).place(x=10,y=100)
Button(root, text="%", width=3, height=1, bd=3, relief=RIDGE, font=('arial',30,'bold'),fg='cyan',bg='#858b94',command=lambda:show("%")).place(x=100,y=100)
Button(root, text="/", width=3, height=1, bd=3, relief=RIDGE, font=('arial',30,'bold'),fg='cyan',bg='#858b94',command=lambda:show("/")).place(x=190,y=100)
Button(root, text="*", width=3, height=1, bd=3, relief=RIDGE, font=('arial',30,'bold'),fg='cyan',bg='#858b94',command=lambda:show("*")).place(x=280,y=100)

Button(root, text="7", width=3, height=1, bd=3, relief=RIDGE, font=('arial',30,'bold'),fg='cyan',bg='#858b94',command=lambda:show("7")).place(x=10,y=190)
Button(root, text="8", width=3, height=1, bd=3, relief=RIDGE, font=('arial',30,'bold'),fg='cyan',bg='#858b94',command=lambda:show("8")).place(x=100,y=190)
Button(root, text="9", width=3, height=1, bd=3, relief=RIDGE, font=('arial',30,'bold'),fg='cyan',bg='#858b94',command=lambda:show("9")).place(x=190,y=190)
Button(root, text="-", width=3, height=1, bd=3, relief=RIDGE, font=('arial',30,'bold'),fg='cyan',bg='#858b94',command=lambda:show("-")).place(x=280,y=190)

Button(root, text="4", width=3, height=1, bd=3, relief=RIDGE, font=('arial',30,'bold'),fg='cyan',bg='#858b94',command=lambda:show("4")).place(x=10,y=280)
Button(root, text="5", width=3, height=1, bd=3, relief=RIDGE, font=('arial',30,'bold'),fg='cyan',bg='#858b94',command=lambda:show("5")).place(x=100,y=280)
Button(root, text="6", width=3, height=1, bd=3, relief=RIDGE, font=('arial',30,'bold'),fg='cyan',bg='#858b94',command=lambda:show("6")).place(x=190,y=280)
Button(root, text="+", width=3, height=1, bd=3, relief=RIDGE, font=('arial',30,'bold'),fg='cyan',bg='#858b94',command=lambda:show("+")).place(x=280,y=280)

Button(root, text="1", width=3, height=1, bd=3, relief=RIDGE, font=('arial',30,'bold'),fg='cyan',bg='#858b94',command=lambda:show("1")).place(x=10,y=370)
Button(root, text="2", width=3, height=1, bd=3, relief=RIDGE, font=('arial',30,'bold'),fg='cyan',bg='#858b94',command=lambda:show("2")).place(x=100,y=370)
Button(root, text="3", width=3, height=1, bd=3, relief=RIDGE, font=('arial',30,'bold'),fg='cyan',bg='#858b94',command=lambda:show("3")).place(x=190,y=370)
Button(root, text=".", width=3, height=1, bd=3, relief=RIDGE, font=('arial',30,'bold'),fg='cyan',bg='#858b94',command=lambda:show(".")).place(x=10,y=460)

Button(root, text="0", bd=3, relief=RIDGE, font=('arial',30,'bold'),fg='cyan',bg='#858b94',command=lambda:show("0")).place(x=100,y=460,width=171, height=82,)
Button(root, text="=", width=3, height=3, bd=3, relief=RIDGE, font=('arial',30,'bold'),fg='#fff',bg='#1475f5',command=lambda:calculate()).place(x=280,y=370)

root.mainloop()