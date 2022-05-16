import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")

aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)

def clickMe():
    action.configure(text='Hello ' + name.get() + ' ' + numberChosen.get())

ttk.Label(win, text="Enter a name: ").grid(column=0, row=0)

name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)

ttk.Label(win, text="Choose a number: ").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

win.mainloop()

