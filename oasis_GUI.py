from tkinter import *
import os

win = Tk()
win.title("OASIS")
win.resizable(width=False, height=False)
win.geometry("900x600")
win.configure(background="Black")

fondoimg = PhotoImage(file="w.png")
fondoshow = Label(win, text="", image=fondoimg)
fondoshow.pack()



systeminfoimg = PhotoImage(file="chat_button.png")
systeminfo = Button(win, text="SYSTEMINFO", image=systeminfoimg, width=150, height=67,borderwidth=0, highlightthickness= 0, command= lambda: os.popen("chat.py"))
systeminfo.place(x=35, y=150)

adminimg = PhotoImage(file="database.png")
admin = Button(win, text="TASKMGR", width=150, height=67, highlightthickness= 0, borderwidth=0, image=adminimg, command= lambda: os.popen("database.py"))
admin.place(x=205, y=150)

cmdimg = PhotoImage(file="cmd.png")
cmd = Button(win, text="TASKMGR", width=150, height=67, highlightthickness= 0, borderwidth=0, image=cmdimg, command= lambda: os.popen("cmd.py"))
cmd.place(x=375, y=150)

createfileimg = PhotoImage(file="create file.png")
createfile = Button(win, text="createfile", image=createfileimg, width=150, height=67,borderwidth=0, highlightthickness= 0, command= lambda: os.popen("createfile.py"))
createfile.place(x=545, y=150)

deletefileimg = PhotoImage(file="deletefile.png")
deletefile = Button(win, text="deletefile", image=deletefileimg, width=150, height=67,borderwidth=0, highlightthickness= 0, command= lambda: os.popen("deletefile.py"))
deletefile.place(x=545 + 170, y=150)


win.mainloop()
