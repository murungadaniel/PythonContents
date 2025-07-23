import tkinter as tk
from tkinter import *

window = Tk()

frame1 = Frame(master=window, height=100, bg="red")
frame1.pack(fill=BOTH,side=LEFT, expand=True)

frame2 = Frame(master=window, height=50, bg="yellow")
frame2.pack(fill=BOTH,side=LEFT, expand=True)

frame3 = Frame(master=window, height=25, bg="blue")
frame3.pack(fill=BOTH,side=LEFT, expand=True)

entry = Entry(master=frame1,width=30,bg='white',fg='black')
entry.insert(0,"Enter your email")
entry.pack()

window.mainloop()