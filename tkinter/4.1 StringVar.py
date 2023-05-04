import tkinter as tk

win = tk.Tk()

strData = tk.StringVar()
strData.set('Hello World')
varData = strData.get()
print(varData)

print(tk.IntVar().get())
print(tk.DoubleVar())

win.mainloop()

