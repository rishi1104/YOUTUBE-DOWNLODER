import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os
import youtube_dl

def clear():
    url.delete(first=0, last=300)

def browse_button():
    global folder_path
    global filename
    filename = filedialog.askdirectory()
    folder_path.set(filename)

def download():
    try:
        URL = url.get()
        PATH = path.get()
        ydl_opts = {}
        os.chdir(PATH)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([URL])
        noty='Your video Downloaded'
        Notification.configure(text=noty,fg='white', bg="black", width=50, font=('times', 17, 'bold','italic'))
        Notification.place(x=350, y=500)
    except Exception as e:
        print(e)

window = tk.Tk()
folder_path = StringVar()
window.title("MY VIDEO DOWNLODER")


width, height = window.winfo_screenwidth(), window.winfo_screenheight()

window.geometry('%dx%d+0+0' % (width,height))
# window.geometry('1300x720')
window.configure(background='snow')
# window.grid_rowconfigure(0, weight=1)
# window.grid_columnconfigure(0, weight=1)

message = tk.Label(window, text="MY VIDEO DOWNLODER", bg="SpringGreen3", fg="black", width=50,
                   height=3, font=('times', 30, 'italic bold '))
message.place(x=80, y=20)

copy_right = tk.Label(window, text="©Developed by rushabh makwana", bg="red", fg="black", width=60,
                   height=1, font=('times', 30, 'italic bold '))
copy_right.place(x=00, y=607)

Notification = tk.Label(window, text="Video downloaded from youtube", bg="Green", fg="white", width=35,
                   height=3, font=('times', 17, 'bold'))

lbl_url = tk.Label(window, text="YOUTUBE URL", width=18, height=2, fg="white", bg="black", font=('times', 15, ' bold '))
lbl_url.place(x=200, y=200)

url = tk.Entry(window, width=32, bg="yellow", fg="red",font=('times', 25, ' bold '))
url.place(x=490, y=210)

lbl_path = tk.Label(window, text="SAVE TO", width=18, height=2, fg="white", bg="black", font=('times', 15, ' bold '))
lbl_path.place(x=200, y=310)

path = tk.Entry(window, width=32, bg="yellow", fg="red",textvariable=folder_path, font=('times', 25, ' bold '))
path.place(x=490, y=320)

clearButton = tk.Button(window, text="Clear",command=clear,fg="black"  ,bg="white"  ,width=10  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.place(x=1100, y=210)

browse = tk.Button(window, text="Browse",command=browse_button,fg='black',bg="white",width=10  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
browse.place(x=1100, y=320)

down = tk.Button(window, text="Download",command=download  ,fg="white"  ,bg="red"  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
down.place(x=650, y=400)

window.mainloop()
