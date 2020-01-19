from tkinter import *
import os
import subprocess

win = Tk()
win.title("OASIS Chat Picker")
win.resizable(width=False, height=False)
win.geometry("900x600")
win.configure(background="Black")
win.iconbitmap("applogo.ico")

systeminfoimg = PhotoImage(file="chat_client.png")
systeminfo = Button(win, text="SYSTEMINFO", image=systeminfoimg, width=150, height=67,borderwidth=0, highlightthickness= 0, command= lambda: os.popen("chat.py"))
systeminfo.place(x=35, y=150)

createfileimg = PhotoImage(file="chat_server.png")
createfile = Button(win, text="createfile", image=createfileimg, width=150, height=67,borderwidth=0, highlightthickness= 0, command= lambda: os.popen("createfile.py"))
createfile.place(x=545, y=150)
