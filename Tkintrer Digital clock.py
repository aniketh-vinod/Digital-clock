from tkinter import *
import tkinter
import time

root=Tk()
root.title("Digital Clock")
root.geometry("500x500")

def update_time():
    current_time=time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(1000,update_time)


clock=Label(root,fg="blue")
clock.pack()

update_time()
root.mainloop()