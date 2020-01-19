import os
import logging
import logging.handlers
import subprocess
import time, sys
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import ssl
win = Tk()
win.title("OASIS")
win.resizable(width=False, height=False)
win.geometry("900x600")
win.configure(background="Black")

fondoimg = PhotoImage(file="GUI_Background.png")
fondoshow = Label(win, text="", image=fondoimg)
fondoshow.pack()



systeminfoimg = PhotoImage(file="chat_button.png")
systeminfo = Button(win, text="SYSTEMINFO", image=systeminfoimg, width=150, height=67,borderwidth=0, highlightthickness= 0, command= lambda: os.popen("chat.py"))
systeminfo.place(x=35, y=150)

adminimg = PhotoImage(file="database.png")
admin = Button(win, text="TASKMGR", width=150, height=67, highlightthickness= 0, borderwidth=0, image=adminimg, command= lambda: os.popen("database.py"))
admin.place(x=205, y=150)




win.mainloop()
