from tkinter import *

root = Tk()
root.geometry("400x500")
root.title("TKinter")
root.resizable(False, False)
root.configure(bg="cyan")

l1 = Label(root, text="Enter Your Name", bg="gray")
l1.pack()
t1 = Entry(root, bg="white")
t1.pack()


# def buttonClick():
#     name = t1.get()
#     l2 = Label(root,text=name)
#     l2.pack()

def displayName():
    # name = 'Hello '
    # name +=t1.get()
    name = t1.get()
    l2 = Label(root, text='Hello '+name)
    l2.pack()

b1 = Button(root, text="Submit", bg="gray", command=displayName)
b1.pack()

root.mainloop()
