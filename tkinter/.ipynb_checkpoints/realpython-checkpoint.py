from tkinter import *
import tkinter.ttk as ttk

window = Tk()
frame = Frame(relief=SUNKEN,borderwidth=5)
frame.pack()

#displaying text on the windows
greeting = Label(master=frame,text='Introduction to tkinter Programming',
                 bg="white",fg="black",width=30,height=1)
#displaying clickable buttons
button = Button(window,text="Click Me",width=5,
                height=2,bg="orange",fg="black")

#getting user input with entry widgets
entry = Entry(window,width=30,bg='white',fg='black')
entry.insert(0,"Enter your email")
#
text = Text(window,width=30,height=2)
text.insert("1.0","Hello world")


label_a = Label(master=frame,text="Getting started in tkinter")
label_a.pack()

name = entry.get()

def on_click_1():
    name1 = text.get("1.0",END)
    text.delete("1.0",END)
    answer1 = Label(window,text=name1)
    answer1.pack()

    
#To get the information entered in the entry widget

def on_click():
    global name
    name = entry.get()
    entry.delete(0,END)
    answer = Label(window,text=name)
    answer.pack()

button_display = Button(window,text="Press",command=on_click)
button_display1 = Button(window,text="Press Bress",command=on_click_1)

greeting.pack()
button.pack()
entry.pack()
button_display.pack()
text.pack()
button_display1.pack()


window.mainloop()


