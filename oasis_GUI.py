from tkinter import *
import os

win = Tk()
win.title("OASIS")
win.resizable(width=False, height=False)
win.geometry("900x600")
win.configure(background="Black")

fondoimg = PhotoImage(file="GUI_Background.png")
fondoshow = Label(win, text="", image=fondoimg)
fondoshow.pack()

win.mainloop()
