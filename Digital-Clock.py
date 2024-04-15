from tkinter import *
from tkinter.ttk import *
from time import strftime


root=Tk()
root.title("Clock")
root.resizable(False, False)


#Function to display time
def time():
    #Format time as HH:MM:SS AM/PM
    format = strftime( '%H:%M:%S %p')
    #update time on GUI
    name.config(text=format)
    #Update time every 1000ms
    name.after(1000,time)


name=Label(root,font=("ds-digital" ,100) , background="black" , foreground="cyan")
name.pack(anchor="center")


time()
root.mainloop()