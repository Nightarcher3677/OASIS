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



systeminfoimg = PhotoImage(file="chat_button.png")
systeminfo = Button(win, text="SYSTEMINFO", image=systeminfoimg, width=150, height=67,borderwidth=0, highlightthickness= 0, command= lambda: os.system("systeminfo"))
systeminfo.place(x=35, y=150)





win.mainloop()
