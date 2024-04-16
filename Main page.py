from tkinter import *
from tkinter import messagebox
import ast 


wn=Tk()
wn.title("SignUp Form| CodeZone")
wn.geometry("925x500+300+200")
wn.configure(bg="#fff")
wn.resizable(False,False)

# Function for user signup
def signup():
    # Get user input for username and password
    username = user.get()
    password = code.get()
    conform_password = conform_code.get()

    # Check if password and conform_password match
    if password == conform_password:
        try:
            # Open file in read mode and convert to dictionary
            file = open('datasheet.txt', "r+")
            d = file.read()
            r = ast.literal_eval(d)

            # Create new dictionary with username and password
            dict2 = {username: password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            # Write updated dictionary to file
            file = open("datasheet.txt", "w")
            w = file.write(str(r))
            file.close()

            # Show success message
            messagebox.showinfo("Signup", "Successfully signed up")
        except:
            # If file is empty, create new dictionary with default values
            file = open("datasheet.txt", "w")
            pp = str({"Username": "password"})
            file.write(pp)
            file.close()
    else:
        # Show error message if passwords don't match
        messagebox.showerror("Invalid", "Both Passwords should match")

################################################################################



def singin():
    wn.destroy()
    root=Tk()
    root.title("Login Form | CodeZone")
    root.geometry("925x500+300+200")
    root.configure(bg="#fff")
    root.resizable(False,False)


    def signin(): # Function to handle sign-in process
        username = user.get() # Get input for username
        password = code.get() # Get input for password


        file = open("datasheet.txt","r")
        d = file.read()
        r = ast.literal_eval(d)
        file.close()


        if username in r.keys() and password == r[username]: 
            screen = Toplevel(root) # Create new window for successful sign-in
            screen.title("App")
            screen.geometry("925x500+300+200")
            screen.config(bg="white")

            Label(screen, text="Hello Everyone!", bg="#fff", font=("calibri(Body)", 50, "bold")).pack(expand=True)

            screen.mainloop()

        if username in r.keys() and password != r[username]:
            messagebox.showerror("Invalid","Wrong Password")
        else:
            messagebox.showerror("Invalid","Wrong  Username") 

    img = PhotoImage(file="D:\desktop\Login System\Login Form\login.png")
    Label(root,image=img,bg="white").place(x=50 , y=50)

    frame = Frame(root,width=360,height=350,bg="#fff")
    frame.place(x=480,y=70)

    heading=Label(frame,text="Sign in" , fg="#57a1f8" , bg="White" , font=("Microsoft UI Light",23,"bold"))
    heading.place(x=100,y=5)

    #######################################################

    def on_enter(e):
        user.delete(0 , "end")
    def on_leave(e):
        name=user.get()
        if name =="":
            user.insert(0,"Username")
    user = Entry(frame,width=25 , fg="black" , border=0 , bg="white" , font=("Microsoft YaHei UI Light",11))
    user.place(x=30 , y=80)
    user.insert(0,"Username")
    user.bind("<FocusIn>" , on_enter)
    user.bind("<FocusOut>" , on_leave)

    Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
    ######################################################

    def on_enter(e):
        code.delete(0 , "end")
    def on_leave(e):
        name=code.get()
        if name =="":
            code.insert(0,"Password")
    code = Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
    code.place(x=30 , y=150)
    code.insert(0,"Password")
    code.bind("<FocusIn>" , on_enter)
    code.bind("<FocusOut>" , on_leave)


    Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
    ######################################################

    Button(frame,width=39,pady=7,text="Sign in",bg="#57a1f8" ,fg="white",border=0  ,command=signin).place(x=35 , y=204)
    label=Label(frame,text="Don't have an account?" , fg="black",bg="white",font=("Microsoft YaHei UI Light",9))
    label.place(x=75,y=270)


    def Login():
        root.destroy()
        window=Tk()
        window.title("Login Form | CodeZone")
        window.geometry("925x500+300+200")
        window.configure(bg="#fff")
        window.resizable(False,False)


        def signin(): # Function to handle sign-in process
            username = user.get() # Get input for username
            password = code.get() # Get input for password

            if username == "admin" and password == '283165': # Check if username and password match
                screen = Toplevel(window) # Create new window for successful sign-in
                screen.title("App")
                screen.geometry("925x500+300+200")
                screen.config(bg="white")

                Label(screen, text="Hello Everyone!", bg="#fff", font=("calibri(Body)", 50, "bold")).pack(expand=True)

                screen.mainloop()

            elif username!="admin" and password!="283165": # If both username and password are incorrect
                messagebox.showerror("Invalid",'Username and Password is incorrect')
            elif username =="admin" and password!="283165": # If only password is incorrect
                messagebox.showerror("Invalid",'Password is incorrect')
            elif username!="admin" and password == "283165": # If only username is incorrect
                messagebox.showerror("Invalid",'Username is incorrect')

        img = PhotoImage(file="D:\desktop\Login System\Login Form\login.png")
        Label(window,image=img,bg="white").place(x=50 , y=50)

        frame = Frame(window,width=360,height=350,bg="#fff")
        frame.place(x=480,y=70)

        heading=Label(frame,text="Sign in" , fg="#57a1f8" , bg="White" , font=("Microsoft UI Light",23,"bold"))
        heading.place(x=100,y=5)

        #######################################################

        def on_enter(e):
            user.delete(0 , "end")
        def on_leave(e):
            name=user.get()
            if name =="":
                user.insert(0,"Username")
        user = Entry(frame,width=25 , fg="black" , border=0 , bg="white" , font=("Microsoft YaHei UI Light",11))
        user.place(x=30 , y=80)
        user.insert(0,"Username")
        user.bind("<FocusIn>" , on_enter)
        user.bind("<FocusOut>" , on_leave)

        Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
        ######################################################

        def on_enter(e):
            code.delete(0 , "end")
        def on_leave(e):
            name=code.get()
            if name =="":
                code.insert(0,"Password")
        code = Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
        code.place(x=30 , y=150)
        code.insert(0,"Password")
        code.bind("<FocusIn>" , on_enter)
        code.bind("<FocusOut>" , on_leave)


        Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
        ######################################################

        Button(frame,width=39,pady=7,text="Sign in",bg="#57a1f8" ,fg="white",border=0  ,command=signin).place(x=35 , y=204)
        label=Label(frame,text="Don't have an account?" , fg="black",bg="white",font=("Microsoft YaHei UI Light",9))
        label.place(x=75,y=270)

        sign_up = Button(frame,width=6,text="Sign up" , border=0 ,bg="white",cursor="hand2" , fg="#57a1f8")
        sign_up.place(x=215 ,y=270)


        window.mainloop()












    sign_up = Button(frame,width=6,text="Sign up" , border=0 ,bg="white",cursor="hand2" , fg="#57a1f8",command=Login)
    sign_up.place(x=215 ,y=270)


    root.mainloop()





##############################################################################


img = PhotoImage(file="D:\desktop\Login System\Sign up Form\signup.png")
Label(wn,image=img,border=0,bg="white").place(x=50 , y=90)


frame = Frame(wn,width=350 , height=390,bg="#fff")
frame.place(x=480 , y=50)


heading = Label(frame,text="Sign up" , fg="#57a1f8" , bg="white" , font=("Microsoft Yahei UI Light" ,23,"bold"))
heading.place(x=100,y=5)
########---------------------------------------------------
def on_enter(e):
    user.delete(0 , "end")
def on_leave(e):
    if user.get() == "":
        user.insert(0,"Username")

user = Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light" ,11))
user.place(x=30 , y=80)
user.insert(0 , 'Username')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

########---------------------------------------------------
def on_enter(e):
    code.delete(0 , "end")
def on_leave(e):
    if code.get() == "":
        code.insert(0,"Password")

code = Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light" ,11))
code.place(x=30 , y=150)
code.insert(0 , 'Password')
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)

########---------------------------------------------------
def on_enter(e):
    conform_code.delete(0 , "end")
def on_leave(e):
    if conform_code.get() == "":
        conform_code.insert(0,"Conform Password")

conform_code= Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light" ,11))
conform_code.place(x=30 , y=220)
conform_code.insert(0 , 'Conform Password')
conform_code.bind("<FocusIn>",on_enter)
conform_code.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=247)


########---------------------------------------------------
Button(frame,width=39,pady=7,text="Signup" ,bg="#57a1f8" , fg="white" ,border=0 , command=signup).place(x=85 , y=280)
label=Label(frame,text="I have an account",fg="black",bg="white",font=("Microsoft Yahei UI Light" ,9))
label.place(x=90 , y=340)

signin = Button(frame,width=6,text="Sing in",border=0,bg="white",cursor="hand2",fg="#57a1f8",command=singin)
signin.place(x=200 , y=340)



wn.mainloop()
