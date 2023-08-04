from tkinter import *
from tkinter import messagebox
import mysql.connector

root = Tk()
root.geometry("475x430")
root.title("Registration")
root.resizable(False, False)
# root.configure(bg='white')

# head_frame = Frame(root,height=50,width=100)
# head_frame.pack()
# form_frame = Frame(root).pack()

fname_value = StringVar()
lname_value = StringVar()
em_value = StringVar()
radio = StringVar()
tec_opt1 = IntVar()
tec_opt2 = IntVar()
tec_opt3 = IntVar()
country_value = StringVar()

head_lab = Label(
    root,
    text="Register Here..",
    # font=("Microsoft YaHei UI Light", 20, "bold"),
    font=("monospace", 20, "bold"),
    fg="#57a1f8",
).place(x=150, y=40)
fn_lab = Label(root, text="First Name:", font=("times", 12)).place(x=70, y=100)
fn_ent = Entry(root, textvariable=fname_value, width=35, border=0).place(x=170, y=104)
ln_lab = Label(root, text="Last Name:", font=("times", 12)).place(x=70, y=132)
ln_ent = Entry(root, textvariable=lname_value, width=35, border=0).place(x=170, y=136)
em_lab = Label(root, text="Email:", font=("times", 12)).place(x=70, y=165)
em_ent = Entry(root, textvariable=em_value, width=35, border=0).place(x=170, y=169)

gnd_lab = Label(root, text="Gender:", font=("times", 12)).place(x=70, y=195)
gnd_rad_inp1 = Radiobutton(
    root, text="Male", variable=radio, value="Male",tristatevalue="x", font=("times", 11)
).place(x=170, y=195)
gnd_rad_inp2 = Radiobutton(
    root, text="Female", variable=radio, value="Female",tristatevalue="x", font=("times", 11)
).place(x=240, y=195)
gnd_rad_inp3 = Radiobutton(
    root, text="Other", variable=radio, value="Other",tristatevalue="x", font=("times", 11)
).place(x=320, y=195)

cnt_lab = Label(root, text="Country:", font=("times", 12)).place(x=70, y=234)

country_value.set("Select Your Country")
drop = OptionMenu(
    root, country_value, "India", "KSA", "UAE", "UK", "Germany", "USA"
).place(x=170, y=230)

tch_lab = Label(root, text="Technology:", font=("times", 12)).place(x=70, y=268)
tech_opt1 = Checkbutton(
    root,
    text="Python",
    variable=tec_opt1,
    onvalue=1,
    offvalue=0,
    height=2,
    width=10,
    font=("times", 11),
).place(x=160, y=260)
tech_opt2 = Checkbutton(
    root,
    text="Php",
    variable=tec_opt2,
    onvalue=1,
    offvalue=0,
    height=2,
    width=10,
    font=("times", 11),
).place(x=245, y=260)
tech_opt3 = Checkbutton(
    root,
    text="Java",
    variable=tec_opt3,
    onvalue=1,
    offvalue=0,
    height=2,
    width=10,
    font=("times", 11),
).place(x=325, y=260)

sub_but = Button(
    root,
    text="Submit",
    bg="#0dd95b",
    fg="#fff",
    height=1,
    border=0,
    width=15,
    activebackground="#00ad42",
    activeforeground="white",
    font=("Microsoft YaHei UI Light", 12, "bold"),
    command=lambda:regSuccess(),
).place(x=180, y=320)

# Database connection and registration data insertion


def connectDB():
    global myDb, myCursor

    myDb = mysql.connector.connect(
        host="localhost", user="root", password="", database="tkinter"
    )
    myCursor = myDb.cursor()

def regSuccess():
    connectDB()
    global fname, lname, email, gender, country
    tech = []
     
    fname = fname_value.get()
    lname = lname_value.get()
    email = em_value.get()
    gender = radio.get()
    if radio.get()!="":
        gender = radio.get()
    else:
        gender = None
    if country_value.get() !="Select Your Country":
        country = country_value.get()
    else:
        country = None
    if tec_opt1.get() !=0:
        tech.append("Python")
    if tec_opt2.get() !=0:
        tech.append("Php")
    if tec_opt3.get() !=0:
        tech.append("Java")
    if fname =="" or lname =="" or email == "":
        messagebox.showwarning("Registration", "Please fill all the fields")
    else:
        sql = "SELECT * FROM form_registration WHERE email = %s"
        val = (email,)
        myCursor.execute(sql,val)
        if myCursor.fetchone() is not None:
            messagebox.showerror("Registration","User already exists")
        else:
            sql = "INSERT INTO form_registration VALUES (%s,%s,%s,%s,%s,%s)"
            val = (fname,lname,email,gender,country,tech)

            myCursor.execute(sql,val)
            myDb.commit()
            messagebox.showinfo("Registration", "Your Registration is successful")
    # print(tech)

root.mainloop()
