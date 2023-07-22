import tkinter as tk
from pytube import YouTube
from tkinter import messagebox
import os

def show_output_download():
    link = url_input.get()
    choose = choose_var.get()

    try:
        video = YouTube(link)
    except Exception as e:
        messagebox.showerror("Error!", f"Error: {str(e)}")
        return

    if choose == "1":
        stream = video.streams.get_audio_only()
    elif choose == "2":
        stream = video.streams.get_highest_resolution()

    download_path = os.path.join(os.path.expanduser('~'), 'downloads')
    stream.download(download_path)

    messagebox.showinfo("Success!", "Download Completed!")

window = tk.Tk()
window.title('YouTubeDownload')
window.minsize(width=500, height=200)

title_label = tk.Label(master=window, text='Paste URL Here:')
title_label.pack(pady=20)

url_input = tk.Entry(master=window, width=50)
url_input.pack()

choose_var = tk.StringVar()
choose_var.set("1")

choose_frame = tk.Frame(master=window)
choose_frame.pack()

radio_buton1 = tk.Radiobutton(choose_frame, text = "Audio only", variable = choose_var, value="1")
radio_buton1.grid(row=0, column=0)

radio_buton2 = tk.Radiobutton(choose_frame, text = "Video", variable = choose_var, value="2")
radio_buton2.grid(row=0, column=2)

button1 = tk.Button(
    master=window, text='Download',
    command=show_output_download, width=15, height=1
    )
button1.pack(pady=10)

output_label = tk.Label(master=window)
output_label.pack(pady=20)

window.mainloop()
