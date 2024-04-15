"""
Import the necessary modules for creating a tkinter GUI application with themed widgets.
- tkinter as tk: Import the tkinter module as tk for GUI creation.
- from tkinter import messagebox: Import the messagebox module from tkinter for displaying message boxes.
- from ttkbootstrap import ttk, Style: Import ttk and Style from ttkbootstrap for themed widgets.
"""
import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import ttk, Style
###########-----------------------------------------------------------------------------------------------------------------------
"""
Define constants for work time, short break time, and long break time in seconds.
WORK_TIME: 25 minutes
SHORT_BREAK_TIME: 5 minutes
LONG_BREAK_TIME: 15 minutes
"""
WORK_TIME = 25 * 60
SHORT_BREAK_TIME = 5 * 60
LONG_BREAK_TIME = 15 * 60
###########-----------------------------------------------------------------------------------------------------------------------
"""
Create a Pomodoro Timer class to manage time intervals for work and breaks.
The class will have methods to start the timer, pause it, resume it, and reset it.
"""
class PomodoroTimer:
    def __init__(self):
        """
        Create a GUI window for a Pomodoro Timer using Tkinter.
        """
        self.root = tk.Tk()
        self.root.geometry("400x200")
        self.root.title("Pomodoro Timer | Code Zone")
        self.root.resizable(False, False)
        self.style = Style(theme="simplex")
        self.style.theme_use()

        """
        Create a label widget to display a timer on the GUI window.
        """
        self.timer_label = tk.Label(self.root, text="", font=("TkDefaultFont", 40))
        self.timer_label.pack(pady=20)

        """
        Create a button in the GUI with the text "Start" that, when clicked, triggers the start_timer method.
        """
        self.start_button = ttk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=5)


        """
        Create a stop button in the GUI window with the specified text and command function.
        """
        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stop_timer,
                                      state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        """
        Initialize the Pomodoro timer with default work time, short break time, and initial states.
        """
        self.work_time, self.break_time = WORK_TIME, SHORT_BREAK_TIME
        self.is_work_time, self.pomodoros_completed, self.is_running = True, 0, False

        """
        Start the main event loop of the tkinter application.
        """
        self.root.mainloop()
##############---------------------------------------------------------------------------------------------------------------------------
    
    
    """
    Start a timer by disabling the start button, enabling the stop button, setting the timer to running, and updating the timer display.
    """
    def start_timer(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.is_running = True
        self.update_timer()
    

    """
    Stop the timer and update the state of buttons accordingly.
    """
    def stop_timer(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.is_running = False


    """
    Update the timer based on whether it is currently running and if it is work time or break time. 
    Adjust the work time, break time, and pomodoros completed accordingly.
    Display appropriate messages based on the progress.
    """

    def update_timer(self):
        if self.is_running:
            if self.is_work_time:
                self.work_time -= 1
                if self.work_time == 0:
                    self.is_work_time = False
                    self.pomodoros_completed += 1
                    self.break_time = LONG_BREAK_TIME if self.pomodoros_completed % 4 == 0 else SHORT_BREAK_TIME
                    messagebox.showinfo("Great job!" if self.pomodoros_completed % 4 == 0
                                        else "Good job!", "Take a long break and rest your mind."
                                        if self.pomodoros_completed % 4 == 0
                                        else "Take a short break and strech your legs!")
            else:
                self.break_time -= 1
                if self.break_time == 0:
                    self.is_work_time, self.work_time = True, WORK_TIME
                    messagebox.showinfo("Work TIie", "Get back to work!")        
            minutes, seconds = divmod(self.work_time if self.is_work_time else self.break_time, 60)
            self.timer_label.config(text="{:02d}:{:02d}".format(minutes, seconds))
            self.root.after(1000, self.update_timer)



"""
Create a Pomodoro Timer object to help manage time using the Pomodoro Technique.
"""
PomodoroTimer()