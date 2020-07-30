from tkinter import*
import os
def delete2():
    screen3.destroy()
def delete3():
    screen4.destroy()
def delete4():
    screen5.destroy()
def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text="Login success").pack()
    Button(screen3, text="OK", command=delete2).pack()
def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text="password not recognised").pack()
    Button(screen4, text="OK", command=delete3).pack()
def username_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text="User not found").pack()
    Button(screen5, text="OK", command=delete4).pack()
def register_user():
    username_info=username.get()
    password_info=password.get()
    file=open(username_info+".txt","w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    #username_entry.delete(0,END)
    #password_entry.delete(0,END)
    Label( screen1,text="Your registration is successful",fg="green",font=("calibri",11)).pack()


def register():
    global screen1
    global username
    global password
    global username_entry
    global password_entry
    screen1=Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    username=StringVar()
    password=StringVar()
    Label(screen1, text="please enter the details below").pack()
    Label(screen1, text="").pack()

    Label(screen1,text="username").pack()
    username_entry=Entry(screen1,textvariable=username).pack()

    Label(screen1,text="password").pack()

    password_entry=Entry(screen1,textvariable=password).pack()
    Label(screen1, text="").pack()
    Button(screen1,text="Register",width="10",height="1",command=register_user).pack()
def login_verify():
    username1=username_verify.get()
    password1=password_verify.get()
    #username_entry1.delete(0, END)
    #password_entry1.delete(0, END)

    list_of_files=os.listdir()
    if username1+".txt" in list_of_files:
        file1=open(username1+".txt","r")
        verify=file1.read().splitlines()
        verify1 = verify[1]  # NEW
        if password1 == verify1:
            login_success()
        else:
            password_not_recognised()
    else:
        username_not_found()




def login():
    global screen2
    screen2=Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="please enter the details below to login").pack()
    Label(screen2, text="").pack()
    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    username_verify=StringVar()
    password_verify=StringVar()

    Label(screen2, text=" username ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify).pack()
    #username_entry1.pack()

    Label(screen2, text=" password ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify).pack()
    #password_entry1.pack()

    Label(screen2, text="").pack()
    Button(screen2,text="Login",width=10,height=1,command=login_verify).pack()
def main_screen():
    global screen
    screen=Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text="Notes 1.0",bg="grey",width="300",height="2",font=("calibri",15)).pack()
    Label(text="").pack()
    Button(text="Login",width="30",height="1",command=login).pack()
    Label(text="").pack()
    Button(text="Register",width="30",height="1",command=register).pack()

    screen.mainloop()

main_screen()
