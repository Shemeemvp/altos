from tkinter import *
from tkinter import messagebox
import mysql.connector


def fun():  # db connection
    global mydb, mycursor
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="", database="Tkinter"
    )
    mycursor = mydb.cursor()


def register():  # getting user input
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Registration")
    screen1.geometry("500x500")
    global username, passwd, firstname, lastname
    username = StringVar()
    passwd = StringVar()
    firstname = StringVar()
    lastname = StringVar()
    Label(screen1, text="Register Here").pack()

    us1 = Label(screen1, text="username").place(x=50, y=70)
    e1 = Entry(screen1, textvariable=username).place(x=140, y=70)

    ps1 = Label(screen1, text="password").place(x=50, y=110)
    e1 = Entry(screen1, textvariable=passwd).place(x=140, y=110)

    fn1 = Label(screen1, text="firstname").place(x=50, y=150)
    e1 = Entry(screen1, textvariable=firstname).place(x=140, y=150)

    ln1 = Label(screen1, text="lastname").place(x=50, y=190)
    e1 = Entry(screen1, textvariable=lastname).place(x=140, y=190)

    sbmibtn = Button(screen1, text="Register", command=reg_1).place(x=70, y=250)


def reg_1():  # Storing values into db (user)
    fun()
    global user_name
    global password
    user_name = username.get()
    password = passwd.get()
    first_name = firstname.get()
    last_name = lastname.get()
    if user_name == "" or password == "" or first_name == "" or last_name == "":
        Label(screen1, text="Please complete the form", fg="red").place(x=90, y=300)
    else:
        sql = "SELECT * FROM registration WHERE username=%s"  # selecting entire table from db,taking username , nd check the existance
        val = (user_name,)
        mycursor.execute(sql, val)
        if mycursor.fetchone() is not None:
            Label(screen1, text="User name already exist!!", fg="red").pack()

        else:
            sql = (
                "INSERT INTO registration VALUES(%s,%s,%s,%s)"  # adding values into db
            )
            val = (user_name, password, first_name, last_name)
            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Registration successfull", "Registration successfull")


def login():  # frontend
    global screen2
    global username1, password1
    screen2 = Toplevel(screen)
    screen2.title("LOGIN")
    screen2.geometry("400x300")

    username1 = StringVar()
    password1 = StringVar()

    Label(screen2, text="Login Here").pack()
    uss1 = Label(screen2, text="Username").place(x=50, y=70)
    ee1 = Entry(screen2, textvariable=username1).place(x=140, y=70)

    pss1 = Label(screen2, text="Password").place(x=50, y=110)
    ee2 = Entry(screen2, textvariable=password1).place(x=140, y=110)

    submitbtn1 = Button(screen2, text="Login", width=20, height=2, command=log).place(
        x=70, y=200
    )


def log():
    fun()
    global user_name1
    user_name1 = username1.get()
    passwd1 = password1.get()
    if user_name1 == "" or passwd1 == "":
        Label(screen2, text="Plz enter both username and password", fg="red").place(
            x=85, y=260
        )
    else:
        sql = "SELECT * FROM registration WHERE username=%s AND passsword=%s"
        val = (
            user_name1,
            passwd1,
        )
        mycursor.execute(sql, val)
        if mycursor.fetchone() is not None:
            logpage(user_name1)
        else:
            messagebox.showinfo("Acess denied", "Acess denied")


def logpage(user_name1):  # front end
    global screen3, uname
    screen3 = Toplevel(screen)
    screen3.title("welcome")
    screen3.geometry("500x500")
    uname = user_name1
    Label(screen3, text="Welcome" + " " + uname).pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Change Password", command=lambda: update(uname)).pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Delete Acct", command=lambda: delete(uname)).pack()


def update(uname):  # front end
    global screen4, newpass, u_name
    u_name = uname
    screen4 = Toplevel(screen3)
    screen4.title("Change password")
    screen4.geometry("500x500")
    newpass = StringVar()
    Label(screen4, text=uname).pack()
    Label(screen4, text="Enter new password").place(x=50, y=70)
    pe1 = Entry(screen4, textvariable=newpass).place(x=170, y=70)
    Button(screen4, text="Update password", command=lambda: upd(u_name)).place(
        x=50, y=140
    )


def upd(u_name):
    fun()
    global nepas
    nepas = newpass.get()
    un_ame = u_name
    if nepas == "":
        Label(screen4, text="Plz enter new password", fg="red").place(x=85, y=260)
    else:
        sql = "UPDATE registration SET passsword=%s WHERE username=%s"
        val = (
            nepas,
            un_ame,
        )
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Updated", "Password updated successfully")


def delete(uname):
    fun()
    sql = "DELETE FROM registration WHERE username=%s"  # fetching
    val = (uname,)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo("Delete", "Account deleted successfully")


def main():
    global screen
    screen = Tk()
    screen.geometry("300x300")
    screen.title("Welcome")
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Button(text="Login", command=login).pack()
    Label(text="").pack()
    Button(text="Register", command=register).pack()
    screen.mainloop()


main()
