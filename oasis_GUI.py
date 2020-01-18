import Tkinter
top = Tkinter.Tk()
# Code to add widgets will go here...

L1 = Label(top, text="Username")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)
R1 = Label(top, text="Password")
R1.pack( side = LEFT)
E1 = Entry(top, bd =10)
E1.pack(side = RIGHT)

top.mainloop()
