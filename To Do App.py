import customtkinter as ctk

# Function to add a new todo item
def add_todo():
    # Get the text from the entry field
    todo = entry.get()
    # Create a new label with the todo text
    label = ctk.CTkLabel(scrollable_frame, text=todo)
    # Add the new label to the scrollable frame
    label.pack()
    # Clear the entry field
    entry.delete(0, ctk.END)

#Make The App Window:-
    
#Create CTK window object
root = ctk.CTk() 
# Set window size
root.geometry("750x450") 
#Set title of window
root.title("Todo App | CodeZone")


#Title Label
title_label = ctk.CTkLabel(root, text="Daily Tasks", font=ctk.CTkFont(size=30, weight="bold"))
#Place Title in top center of window
title_label.pack(padx=10, pady=(40, 20)) 

#height is set to make it scrollable
scrollable_frame = ctk.CTkScrollableFrame(root, width=500, height=200)
#place the scrollable frame at bottom left corner of
scrollable_frame.pack()

#create an Entry Field for user input
entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Add todo")
#expand horizontally
entry.pack(fill="x")

#command refers to function that will be executed when button
add_button = ctk.CTkButton(root, text="Add", width=500, command=add_todo)
#place the "Add" Button below the Entry Field
add_button.pack(pady=20)

#run the mainloop method which keeps the app running until closed by user
root.mainloop()