from tkinter import Tk,Entry,Button,StringVar
import tkinter as tk


# Define calculator class
class Calculator:
  # Initialize calculator
  def __init__(self,master):
      # Set calculator title, size, and background 
      master.title("Calculator")
      master.geometry("357x420+0+0")
      master.config(bg = "black")
      master.resizable(False,False)

      # Create variable and empty string for equation
      self.equation=StringVar()
      self.entry_value=" "


      Button(width=11,height=4,text="(",relief= "flat",fg="#fff",bg="#2a2d36",command=lambda:self.show("(")).place(x=0,y=50)
      Button(width=11,height=4,text=")",relief= "flat",fg="#fff",bg="#2a2d36",command=lambda:self.show(")")).place(x=90,y=50)
      Button(width=11,height=4,text="%",relief= "flat",fg="#fff",bg="#2a2d36",command=lambda:self.show("%")).place(x=180,y=50)
      Button(width=11,height=4,text="1",relief= "flat",fg="#fff",bg="#2a2d36",command=lambda:self.show(1)).place(x=0,y=125)
      Button(width=11,height=4,text="2",relief= "flat",fg="#fff",bg="#2a2d36",command=lambda:self.show(2)).place(x=90,y=125)
      Button(width=11,height=4,text="3",relief= "flat",fg="#fff",bg="#2a2d36",command=lambda:self.show(3)).place(x=180,y=125)
      Button(width=11,height=4,text="4",relief= "flat",fg="#fff",bg="#2a2d36",command=lambda:self.show(4)).place(x=0,y=200)
      Button(width=11,height=4,text="5",relief= "flat",fg="#fff",bg="#2a2d36",command=lambda:self.show(5)).place(x=90,y=200)
      Button(width=11,height=4,text="6",relief= "flat",fg="#fff",bg="#2a2d36",command=lambda:self.show(6)).place(x=180,y=200)
      Button(width=11,height=4,text="7",relief= "flat",fg="#fff",bg="#2a2d36",command=lambda:self.show(7)).place(x=0,y=275)
      Button(width=11,height=4,text="8",relief= "flat",fg="#fff",bg="#2a2d36",command=lambda:self.show(8)).place(x=180,y=275)
      Button(width=11,height=4,text="9",relief= "flat",fg="#fff",bg="#2a2d36",command=lambda:self.show(9)).place(x=90,y=275)
      Button(width=11,height=4,text="0",relief= "flat",fg="#fff",bg="#2a2d36",command=lambda:self.show(0)).place(x=90,y=350)
      Button(width=11,height=4,text=".",relief= "flat",fg="#fff",bg="#2a2d36",command=lambda:self.show(".")).place(x=180,y=350)
      Button(width=11,height=4,text="+",relief= "flat",fg="#fff",bg="#2a2d36",command=lambda:self.show("+")).place(x=270,y=275)
      Button(width=11,height=4,text="-",relief= "flat",fg="#fff",bg="#2a2d36",command=lambda:self.show("-")).place(x=270,y=200)
      Button(width=11,height=4,text="x",relief= "flat",fg="#fff",bg="#2a2d36",command=lambda:self.show("*")).place(x=270,y=50)
      Button(width=11,height=4,text="/",relief= "flat",fg="#fff",bg="#2a2d36",command=lambda:self.show("/")).place(x=270,y=125)
      Button(width=11,height=4,text="=",relief= "flat",fg="#fff",bg="#fe9037",command=self.solve).place(x=270,y=350)
      Button(width=11,height=4,text="C",relief= "flat",fg="#fff",bg="#3697f5",command=self.clear).place(x=0,y=350)

      # Create entry box for equation
      Entry(width=17 , bg='dimgray' , font=("Arial Bold",28),textvariable=self.equation).place(x=0,y=0)

  # Display pressed button's value
  def show(self,value):
      self.entry_value+=str(value)
      self.equation.set(self.entry_value)
      
  # Clear calculator's equation
  def clear(self):
      self.entry_value=" "
      self.equation.set(self.entry_value)
    
  def solve(self):
        result=eval(self.entry_value)
        self.equation.set(result)
      




root=Tk()
calculator=Calculator(root)
root.mainloop()