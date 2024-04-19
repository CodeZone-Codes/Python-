#Import Modules
import tkinter as tk
from ttkthemes import ThemedStyle
#------------------------------------------------------------------------------------------------------------------------------------------------------
class Stopwatch(tk.Tk): 
    def __init__(self):
        super().__init__()
        self.title("Stopwatch | CodeZone") #Window Title
        self.geometry("300x350") #Window Size
        self.time = 0  #Time Variable
        self.running = False  #Status of the Timer
        self.config(bg="#00a1f7") #window background
        self.resizable(False,False) #disable resizing
#------------------------------------------------------------------------------------------------------------------------------------------------------
        #Set The Window Theme > breeze
        self.style = ThemedStyle()
        self.style.set_theme("breeze")
#------------------------------------------------------------------------------------------------------------------------------------------------------
        #Set the timer window
        self.label = tk.Label(self, text="0:00:00", pady="20",width=30, font=("Helvetica", 35) , bg="#00a1f7")
        self.label.pack()
#------------------------------------------------------------------------------------------------------------------------------------------------------
        #Set the start Button
        self.start_button = tk.Button(self, text="Start", width=10, height=2, font=("Helvetica", 14), command=self.start ,bg="#4cfdf7")
        self.start_button.pack()
#------------------------------------------------------------------------------------------------------------------------------------------------------
        #Set the stop Button
        self.stop_button = tk.Button(self, text="Stop", width=10, height=2, font=("Helvetica", 14), command=self.stop,bg="#4cfdf7")
        self.stop_button.pack()
#------------------------------------------------------------------------------------------------------------------------------------------------------
        #Set the reset Button
        self.reset_button = tk.Button(self, text="Reset", width=10, height=2, font=("Helvetica", 14), command=self.reset,bg="#4cfdf7")
        self.reset_button.pack()
#------------------------------------------------------------------------------------------------------------------------------------------------------
    #Define the start Function
    def start(self):
        self.running = True
        self.count()
#------------------------------------------------------------------------------------------------------------------------------------------------------
    #Define the stop Function
    def stop(self):
        self.running = False
#------------------------------------------------------------------------------------------------------------------------------------------------------
    #Define the reset Function
    def reset(self):
        self.running = False
        self.time = 0
        self.label.config(text="0:00:00")
#------------------------------------------------------------------------------------------------------------------------------------------------------
    #Define the Count Function
    def count(self):
        if self.running:
            self.time += 1
            minutes, seconds = divmod(self.time, 60)
            hours, minutes = divmod(minutes, 60)
            self.label.config(text="{:01d}:{:02d}:{:02d}".format(hours, minutes, seconds))
            self.after(1000, self.count)
#------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    stopwatch = Stopwatch() 
    stopwatch.mainloop() 