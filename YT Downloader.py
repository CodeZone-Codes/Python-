from tkinter import *
from pytube import YouTube
from tkinter import ttk
import threading

# Create the main window
window = Tk()
window.geometry('500x150')
window.title('YT Video Downloader | CodeZone')
window.resizable(False,False)


# Create a function to download the video
def download():
    url = entry.get()
    quality = video_resolution.get()
    try:
        youtube = YouTube(url)
        video = youtube.streams.filter(res=quality).first()
        video.download()
        label.config(text='Download completed',bg="red")
    except:
        label.config(text='Error')

# Create a search function to get the video resolutions
def searchResolution():
    url = entry.get()
    try:
        youtube = YouTube(url)
        video_resolution.config(values=tuple([stream.resolution for stream in youtube.streams.all()]))
    except:
        video_resolution.config(values=('',))

# Create a thread for the search function
def searchThread():
    t1 = threading.Thread(target=searchResolution)
    t1.start()

# Create UI elements
label = Label(window, text='')
entry = ttk.Entry(window, width=50)
download_button = ttk.Button(window, text='Download', command=download)
search_resolution = ttk.Button(window, text='Search Resolution', command=searchThread)
video_resolution = ttk.Combobox(window, width=10)

# Place UI elements
label.pack()
entry.pack()
download_button.pack()
search_resolution.pack()
video_resolution.pack()

# Run the main loop
window.mainloop()

#Don't Forget The Subscribe