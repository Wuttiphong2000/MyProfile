from tkinter import *
from time import strftime

mywindow = Tk()
mywindow.title('My Clock')

def time():
    myTime = strftime('%H:%M:%S %p')
    clock.config(text = myTime)
    clock.after(1000, time)

clock = Label(mywindow, font = ('arial', 40, 'bold'),
                                background = 'dark green',
                                foreground = 'white')
clock.pack(anchor = 'center')
time()

mainloop()