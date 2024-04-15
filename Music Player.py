"""
Import necessary libraries for creating a GUI application, handling file dialogs, 
displaying progress bars, using custom tkinter widgets, working with mp3 files,
threading, playing audio with pygame, and managing time and operating system functionalities.
"""
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
import customtkinter as ctk
from mutagen import mp3
import threading
import pygame
import time
import os

# Initialize pygame mixer
pygame.mixer.init()

# Store the current position of the music
current_position = 0
paused = False
selected_folder_path = "" # Store the selected folder path

def update_progress():
    global current_position
    while True:
        if pygame.mixer.music.get_busy() and not paused:
            current_position = pygame.mixer.music.get_pos() / 1000  # Get current position in seconds
            pbar["value"] = current_position  # Update progress bar with current position

            # Check if the current song has reached its maximum duration
            if current_position >= pbar["maximum"]:
                stop_music()  # Stop the music playback
                pbar["value"] = 0  # Reset the progress bar
            
            window.update()
        time.sleep(0.1)

# Create a thread to update the progress bar
pt = threading.Thread(target=update_progress)
pt.daemon = True
pt.start()

# Define function to play selected song
def play_selected_song():
    # Set global variables
    global current_position, paused
    # Check if a song is selected
    if len(lbox.curselection()) > 0:
        # Get the index of the selected song
        current_index = lbox.curselection()[0]
        # Get the name of the selected song
        selected_song = lbox.get(current_index)
        # Combine the folder path and song name to get the full path
        full_path = os.path.join(selected_folder_path, selected_song)
        # Load the selected song
        pygame.mixer.music.load(full_path)
        # Play the song from the current position
        pygame.mixer.music.play(start=current_position)
        # Set paused to False
        paused = False
        # Get audio info
        audio = mp3(full_path)
        # Get song duration
        song_duration = audio.info.length
        # Set progress bar maximum to song duration
        pbar["maximum"] = song_duration

def stop_music():
    # Stop music and reset paused state
    pygame.mixer.music.stop()
    paused = False

    

# Create the main window
window = tk.Tk()
window.title("Music Player App | CodeZone")
window.geometry("700x600")
window.resizable(False,False)

# Create a label for the music player title
l_music_player = tk.Label(window, text="Music Player", font=("TkDefaultFont", 30, "bold"))
l_music_player.pack(pady=10)


#####################################################-----------------------------------------------------------
# Function to select music folder
def select_music_folder():
    # Set global variable for selected folder path
    global selected_folder_path
    # Open directory dialog and get user selection
    selected_folder_path = filedialog.askdirectory()
    # If a folder is selected
    if selected_folder_path:
        # Clear listbox
        lbox.delete(0, tk.END)
        # Loop through files in selected folder
        for filename in os.listdir(selected_folder_path):
            # If file is an MP3
            if filename.endswith(".mp3"):
                # Add file to listbox
                lbox.insert(tk.END, filename)

# Create a button to select the music folder
btn_select_folder = ctk.CTkButton(window, text="Select Music Folder",
                                  command=select_music_folder,
                                  font=("TkDefaultFont", 18))
btn_select_folder.pack(pady=20)
#####################################################-----------------------------------------------------------

# Create a listbox to display the available songs
lbox = tk.Listbox(window, width=50, font=("TkDefaultFont", 16))
lbox.pack(pady=10)

#####################################################-----------------------------------------------------------

# Create a progress bar to indicate the current song's progress
pbar = Progressbar(window, length=300, mode="determinate")
pbar.pack(pady=10)
#####################################################-----------------------------------------------------------

# Create a frame to hold the control buttons
btn_frame = tk.Frame(window)
btn_frame.pack(pady=20)
#####################################################-----------------------------------------------------------

# Define previous_song function
def previous_song():
    # Check if any song is selected
    if len(lbox.curselection()) > 0:
        # Get current selected index
        current_index = lbox.curselection()[0]
        # Check if previous song exists
        if current_index > 0:
            # Clear current selection
            lbox.selection_clear(0, tk.END)
            # Select previous song
            lbox.selection_set(current_index - 1)
            # Play selected song
            play_selected_song()

# Create a button to go to the previous song
btn_previous = ctk.CTkButton(btn_frame, text="<", command=previous_song,
                            width=50, font=("TkDefaultFont", 18))
btn_previous.pack(side=tk.LEFT, padx=5)
#####################################################-----------------------------------------------------------
def play_music():
    global paused
    if paused:  # Check if music is paused
        pygame.mixer.music.unpause()  # Unpause the music
        paused = False
    else:
        play_selected_song()  # Play the selected song

# Create a button to play the music
btn_play = ctk.CTkButton(btn_frame, text="Play", command=play_music, width=50,
                         font=("TkDefaultFont", 18))
btn_play.pack(side=tk.LEFT, padx=5)
#####################################################-----------------------------------------------------------
def pause_music():
    # Indicate music is paused
    global paused
    # Pause music playback
    pygame.mixer.music.pause()
    # Set paused status to True
    paused = True

# Create a button to pause the music
btn_pause = ctk.CTkButton(btn_frame, text="Pause", command=pause_music, width=50,
                          font=("TkDefaultFont", 18))
btn_pause.pack(side=tk.LEFT, padx=5)

#####################################################-----------------------------------------------------------
# Define next_song function
def next_song():
    # Check if a song is selected
    if len(lbox.curselection()) > 0:
        # Get current song index
        current_index = lbox.curselection()[0]
        # Check if there's a next song
        if current_index < lbox.size() - 1:
            # Clear current selection
            lbox.selection_clear(0, tk.END)
            # Select next song
            lbox.selection_set(current_index + 1)
            # Play selected song
            play_selected_song()

# Create a button to go to the next song
btn_next = ctk.CTkButton(btn_frame, text=">", command=next_song, width=50,
                         font=("TkDefaultFont", 18))
btn_next.pack(side=tk.LEFT, padx=5)
#####################################################-----------------------------------------------------------

window.mainloop()

#Don't Forget the Subscribe