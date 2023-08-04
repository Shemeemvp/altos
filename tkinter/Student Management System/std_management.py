from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
# import mysql.connector as mysql
from tkinter import ttk
from tkinter.messagebox import askyesno
# import phonenumbers
import re
import tkinter.font
# Database creation

# con = mysql.connect(host="localhost", user="root", password="")
# cursor = con.cursor()
# cursor.execute("CREATE DATABASE std_management")
# cursor.execute("commit")

# Table Creation

# con = mysql.connect(host="localhost", user="root", password="", database = "std_management")
# cursor = con.cursor()
# cursor.execute("CREATE TABLE student (id int, name varchar(50), phone varchar(50), email varchar(100), address varchar(200))")
# cursor.execute("commit")


# Database and GUI operations


def show():
    try:
        noData.place_forget()
        wrLbl1.place_forget()
        wrLbl2.place_forget()
        wrLbl3.place_forget()
        wrLbl4.place_forget()
    except:
        pass
    con = mysql.connect(
        host="localhost", user="root", password="", database="std_management"
    )
    cursor = con.cursor()
    cursor.execute("select * from student")

    if cursor.fetchone() is None:
        try:
            for item in tree.get_children():
                tree.delete(item)
        except:
            pass
        noData.place(x=445, y=500)
    else:
        con = mysql.connect(
            host="localhost", user="root", password="", database="std_management"
        )
        cursor = con.cursor()
        cursor.execute("select * from student")
        studDetails = cursor.fetchall()
        try:
            for item in tree.get_children():
                tree.delete(item)
        except:
            pass
        for row in studDetails:
            stdId = str(row[0])
            stdName = str(row[1])
            stdPhone = str(row[2])
            tree.insert("", "end", text="1", values=(stdId, stdName, stdPhone))

    con.close()


# def validateForm():
#     id = idEnt.get()
#     name = nameEnt.get()
#     phone = phoneEnt.get()
#     email = emailEnt.get()
#     address = addressEnt.get("1.0","end-1c")

#     if id != "" or name != "" or phone != "" or email != "" or address != "":
#         con = mysql.connect(
#             host="localhost", user="root", password="", database="std_management"
#         )
#         cursor = con.cursor()
#         cursor.execute("SELECT * FROM student where id ='" + id + "'")
#         if cursor.fetchone() is not None:
#             try:
#                 wrLbl1.place_forget()
#                 wrLbl2.place_forget()
#             except:
#                 pass
#             wrLbl1.place(x=535, y=80)
#             return True
#         elif id.isnumeric() is False:
#             try:
#                 wrLbl1.place_forget()
#                 wrLbl2.place_forget()
#             except:
#                 pass
#             wrLbl2.place(x=535, y=80)
#             return True
#         else:
#             return False
#     else:
#         MessageBox.showinfo("Student Data", "Please fill all fields")


def insert():
    id = idEnt.get()
    name = nameEnt.get()
    name = "".join([i for i in nameEnt.get() if not i.isdigit()])
    name = name.replace(" ", "")
    phone = phoneEnt.get()
    email = emailEnt.get()
    address = addressEnt.get("1.0", "end-1c")

    if id == "" or name == "" or phone == "" or email == "" or address == "":
        MessageBox.showinfo("Student Data", "Please fill all fields")
    elif id != "":
        con = mysql.connect(
            host="localhost", user="root", password="", database="std_management"
        )
        cursor = con.cursor()
        cursor.execute("SELECT * FROM student where id ='" + id + "'")
        if cursor.fetchone() is not None:
            try:
                wrLbl1.place_forget()
                wrLbl2.place_forget()
                wrLbl3.place_forget()
                wrLbl4.place_forget()
            except:
                pass
            wrLbl1.place(x=535, y=80)
        elif id.isnumeric() is False:
            try:
                wrLbl1.place_forget()
                wrLbl2.place_forget()
            except:
                pass
            wrLbl2.place(x=535, y=80)

        elif phone.isnumeric() is False or len(phone) < 10:
            try:
                wrLbl1.place_forget()
                wrLbl2.place_forget()
                wrLbl3.place_forget()
            except:
                pass
            wrLbl3.place(x=535, y=160)
        elif email != "":
            regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
            if re.fullmatch(regex, email) is None:
                try:
                    wrLbl1.place_forget()
                    wrLbl2.place_forget()
                    wrLbl3.place_forget()
                    wrLbl4.place_forget()
                except:
                    pass
                wrLbl4.place(x=535, y=200)
            else:
                try:
                    wrLbl1.place_forget()
                    wrLbl2.place_forget()
                    wrLbl3.place_forget()
                    wrLbl4.place_forget()
                except:
                    pass
                con = mysql.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="std_management",
                )
                cursor = con.cursor()
                cursor.execute(
                    "insert into student values('"
                    + id
                    + "','"
                    + name
                    + "','"
                    + phone
                    + "','"
                    + email
                    + "','"
                    + address
                    + "')"
                )
                cursor.execute("commit")

                idEnt.delete(0, "end")
                nameEnt.delete(0, "end")
                phoneEnt.delete(0, "end")
                emailEnt.delete(0, "end")
                addressEnt.delete("1.0", "end")

                show()
                MessageBox.showinfo("Student Data", "Data Added Successfully")
                con.close()


def update():
    id = idEnt.get()
    name = nameEnt.get()
    phone = phoneEnt.get()
    email = emailEnt.get()
    address = addressEnt.get("1.0", "end-1c")

    if id == "" or name == "" or phone == "" or email == "" or address == "":
        MessageBox.showwarning("Data Updating", "Please fill all the fields")

    elif id != "":
        con = mysql.connect(
            host="localhost", user="root", password="", database="std_management"
        )
        cursor = con.cursor()
        cursor.execute("SELECT * FROM student where id ='" + id + "'")
        if cursor.fetchone() is None:
            MessageBox.showerror("Invalid", "Entered Student ID does not exists!!")
        elif id.isnumeric() is False:
            try:
                wrLbl1.place_forget()
                wrLbl2.place_forget()
                wrLbl3.place_forget()
                wrLbl4.place_forget()
            except:
                pass
            wrLbl2.place(x=535, y=80)

        elif phone.isnumeric() is False:
            try:
                wrLbl1.place_forget()
                wrLbl2.place_forget()
                wrLbl3.place_forget()
                wrLbl4.place_forget()
            except:
                pass
            wrLbl3.place(x=535, y=160)
        elif email != "":
            regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
            if re.fullmatch(regex, email) is None:
                try:
                    wrLbl1.place_forget()
                    wrLbl2.place_forget()
                    wrLbl3.place_forget()
                    wrLbl4.place_forget()
                except:
                    pass
                wrLbl4.place(x=535, y=200)
            else:
                con = mysql.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="std_management",
                )
                cursor = con.cursor()
                cursor.execute(
                    "update student set name='"
                    + name
                    + "',phone='"
                    + phone
                    + "',email='"
                    + email
                    + "',address='"
                    + address
                    + "' where id='"
                    + id
                    + "'"
                )
                cursor.execute("commit")

                idEnt.delete(0, "end")
                nameEnt.delete(0, "end")
                phoneEnt.delete(0, "end")
                emailEnt.delete(0, "end")
                addressEnt.delete("1.0", "end")
                show()
                MessageBox.showinfo(
                    "Student Data", "Student's Data Updated Successfully"
                )
                con.close()


def delete():
    if idEnt.get() == "":
        MessageBox.showerror("Remove Student", "Please enter the student ID")
    elif idEnt.get() != "":
        con = mysql.connect(
            host="localhost", user="root", password="", database="std_management"
        )
        cursor = con.cursor()
        cursor.execute("SELECT * FROM student where id ='" + idEnt.get() + "'")
        if cursor.fetchone() is None:
            MessageBox.showerror("Invalid", "Entered Student ID does not exists!!")

        elif idEnt.get() != "":
            confirmDelete = askyesno(
                title="Remove Student",
                message="Are you sure that you want to Remove ID: " + idEnt.get() + "?",
            )
            if confirmDelete:
                con = mysql.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="std_management",
                )
                cursor = con.cursor()
                cursor.execute("delete from student where id='" + idEnt.get() + "'")
                cursor.execute("commit")

                idEnt.delete(0, "end")
                nameEnt.delete(0, "end")
                phoneEnt.delete(0, "end")
                emailEnt.delete(0, "end")
                addressEnt.delete("1.0", "end")
                show()
                MessageBox.showinfo(
                    "Remove Student", "Student's Data are removed successfully"
                )
                con.close()


def get():
    if idEnt.get() == "":
        MessageBox.showerror("Student Data", "Please Enter the Student ID")
    elif idEnt.get() != "":
        con = mysql.connect(
            host="localhost", user="root", password="", database="std_management"
        )
        cursor = con.cursor()
        cursor.execute("SELECT * FROM student where id ='" + idEnt.get() + "'")
        if cursor.fetchone() is None:
            MessageBox.showerror("Invalid", "Entered Student ID does not exists!!")
        else:
            con = mysql.connect(
                host="localhost", user="root", password="", database="std_management"
            )
            cursor = con.cursor()
            cursor.execute("select * from student where id='" + idEnt.get() + "'")
            details = cursor.fetchall()
            try:
                nameEnt.delete(0, "end")
                phoneEnt.delete(0, "end")
                emailEnt.delete(0, "end")
                addressEnt.delete("1.0", "end")
            except:
                pass

            for item in details:
                nameEnt.insert(0, item[1])
                phoneEnt.insert(0, item[2])
                emailEnt.insert(0, item[3])
                addressEnt.insert("1.0", item[4])
            con.close()


def clearFields():
    try:
        idEnt.delete(0, "end")
        nameEnt.delete(0, "end")
        phoneEnt.delete(0, "end")
        emailEnt.delete(0, "end")
        addressEnt.delete("1.0", "end")
    except:
        pass


# GUI Components

# Root Window configurations
root = Tk()
root.geometry("1080x655")
root.title("Student Management System")
root.resizable(False, True)
root.configure(bg="#0a2654")

# MenuBar configurations
menuBar = Menu(root)
root.config(menu=menuBar)
fileMenu = Menu(menuBar, tearoff=0)
editMenu = Menu(menuBar, tearoff=0)
viewMenu = Menu(menuBar, tearoff=0)
helpMenu = Menu(menuBar, tearoff=0)

menuBar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Clear Fields", command=clearFields)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.destroy)

menuBar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo")
editMenu.add_command(label="Redo")
editMenu.add_separator()
editMenu.add_command(label="Cut")
editMenu.add_command(label="Copy")
editMenu.add_command(label="Paste")

menuBar.add_cascade(label="View", menu=viewMenu)
viewMenu.add_command(label="Full Screen")
viewMenu.add_separator()
viewMenu.add_command(label="Zoom In")
viewMenu.add_command(label="Zoom Out")
viewMenu.add_command(label="Reset Zoom")

menuBar.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="Help")
helpMenu.add_command(label="Report Issue")
helpMenu.add_separator()
helpMenu.add_command(label="About")

# Heading Labels
head_label = Label(
    root,
    text="Student Management System",
    bg="#0a2654",
    fg="#fff",
    font=("Microsoft YaHei", 20, "bold"),
    pady=10,
)
head_label.pack()

table_label = Label(
    root,
    text="Student's List",
    bg="#0a2654",
    fg="#fff",
    font=("Calibri Light", 17, "bold"),
)
table_label.place(x=440, y=360)

# Input Labels
stdId = Label(root, text="ID", font=("times", 13), bg="#0a2654", fg="#fff")
stdId.place(x=150, y=80)

StdName = Label(root, text="Name", font=("times", 13), bg="#0a2654", fg="#fff")
StdName.place(x=150, y=120)

StdPhone = Label(root, text="Phone", font=("times", 13), bg="#0a2654", fg="#fff")
StdPhone.place(x=150, y=160)

StdEmail = Label(root, text="E-Mail", font=("times", 13), bg="#0a2654", fg="#fff")
StdEmail.place(x=150, y=200)

StdAddress = Label(root, text="Address", font=("times", 13), bg="#0a2654", fg="#fff")
StdAddress.place(x=150, y=240)

# Input Fields
idEnt = Entry(root, font=("times", 11))
idEnt.place(x=280, y=80, height=25, width=250)

nameEnt = Entry(root, font=("times", 11))
nameEnt.place(x=280, y=120, height=25, width=250)

phoneEnt = Entry(root, font=("times", 11))
# phoneEnt. insert(0, "+91 ")
phoneEnt.place(x=280, y=160, height=25, width=250)

emailEnt = Entry(root, font=("times", 11))
emailEnt.place(x=280, y=200, height=25, width=250)

addressEnt = Text(root, font=("times", 11), height=4, width=40)
addressEnt.place(x=280, y=240)

# Buttons
insertButton = Button(
    root,
    text="INSERT",
    font=("italic", 10, "bold"),
    bg="white",
    fg="#093985",
    activebackground="#093985",
    activeforeground="#fff",
    command=insert,
)
insertButton.place(x=700, y=80, width=75)

deleteButton = Button(
    root,
    text="DELETE",
    font=("italic", 10, "bold"),
    bg="white",
    fg="#093985",
    activebackground="#093985",
    activeforeground="#fff",
    command=delete,
)
deleteButton.place(x=700, y=130, width=75)

updateButton = Button(
    root,
    text="UPDATE",
    font=("italic", 10, "bold"),
    bg="white",
    fg="#093985",
    activebackground="#093985",
    activeforeground="#fff",
    command=update,
)
updateButton.place(x=700, y=180, width=75)

getButton = Button(
    root,
    text="GET",
    font=("italic", 10, "bold"),
    bg="white",
    fg="#093985",
    activebackground="#093985",
    activeforeground="#fff",
    command=get,
)
getButton.place(x=700, y=230, width=75)

clearButton = Button(
    root,
    text="CLEAR",
    font=("italic", 10, "bold"),
    bg="white",
    fg="#093985",
    activebackground="#093985",
    activeforeground="#fff",
    command=clearFields,
)
clearButton.place(x=488, y=320, width=75)

# Treeview configurations
treeStyle = ttk.Style()
treeStyle.theme_use("clam")
tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show="headings", height=8)
treeStyle.configure(
    "Treeview.Heading",
    background="#1061a3",
    foreground="white",
    font=("normal", 12, "bold"),
)
treeStyle.configure(
    "Treeview",
    background="gray",
    fieldbackground="lightgray",
    foreground="white",
    rowheight=25,
    font=("times", 12, "normal"),
)


tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="ID")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Name")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Phone")

tree.place(x=220, y=405)

# Warning Labels
wrLbl1 = Label(
    root,
    text="Student ID already exists!!",
    fg="red",
    bg="#0a2654",
    font=("normal", 10),
)
wrLbl2 = Label(
    root,
    text="Please Enter a valid ID!!",
    fg="red",
    bg="#0a2654",
    font=("normal", 10),
)
wrLbl3 = Label(
    root,
    text="Invalid Phone Number!!",
    fg="red",
    bg="#0a2654",
    font=("normal", 10),
)
wrLbl4 = Label(
    root,
    text="Invalid Email format!!",
    fg="red",
    bg="#0a2654",
    font=("normal", 10),
)
noData = Label(
    root,
    text="Data Not Enrolled..",
    font=("times", 14, "bold"),
    fg="red",
    bg="lightgray",
)

show()
root.mainloop()
