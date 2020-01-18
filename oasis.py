#importing all the modules
import os
import logging
import logging.handlers
import subprocess
import time, sys

LOG_FILENAME = 'app.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
userName = input("Welcome to OASIS! \n\nUsername: ") #Ask's the User for Username input
password = input("Password: ") # Ask's the user for their password





while userName == userName and password == password: # The Input will always lead to this while loop, so we can see if their username and password is wrong or correct.



    if userName == 'username' and password == 'password':
        logging.debug('User signed in')
        break # Leave the loop and the whole program as the username and password is correct


    elif userName != 'username' and password != 'password': # The userName and password is NOT equal to 'elmo' and 'blue', the user cannot enter FaceSnap
        print("Your Username and Password is wrong!")
        logging.warning('Failed to sign in') # Lets the user know that the Username and password entered is wrong.
        userName = input("\n\nUsername: ") # Requests the user to have another attempt at entering their correct username
        password = input("Password: ") # Requests the user to have another attempt at entering their correct password
        continue # Continue, as the user hasn't managed to get their username and password correct yet


    elif userName == 'username' and password != 'password':    #The userName is equal to 'elmo', but password is NOT equal to 'blue', the user cannot enter FaceSnap
        print("Your Password is wrong!")
        logging.warning('Failed to sign in') # Lets the user know that their password is wrong
        userName = input("\n\nUsername: ") # Requests the user to have another attempt at entering their correct username
        password = input("Password: ") # Requests the user to have another attempt at entering their correct password

        continue # Continue, as the user hasn't managed to get their username and password correct yet


    elif userName != 'username' and password == 'password': # The userName is NOT equal to 'elmo', however password is equal to 'blue', the user cannot enter FaceSnap
        print("Your Username is wrong!")
        logging.warning('Failed to sign in') # Lets the user know that their username is wrong
        userName = input("\n\nUsername: ") # Requests the user to have another attempt at entering their correct username
        password = input("Password: ") # Requests the user to have another attempt at entering their correct password

        continue # Continue, as the user hasn't managed to get their username and password correct yet






time.sleep(1)

i = 1
while 1 == i:
    logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
    program = input("choose your program. \n\nProgram: ")

    if program == "read file":
        file = input("enter the filename here. \n\nFile: ")
        f = open(file)
        print(f.read())
        logging.debug('file read')
        program = " "

    elif program == "cmd":
        subprocess.call(['C:\Windows\System32\cmd.exe'])
        logging.debug('cmd opened')
    elif program == "Chrome":
        subprocess.call(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])
        logging.debug('chrome opened')
        program = " "
    elif program == "chrome":
        subprocess.call(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])
        logging.debug('chrome opened')
        program = " "
    elif program == "Minecraft":
        subprocess.call(['C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe'])
        logging.debug('minecraft opened')
        program = " "
    elif program == "minecraft":
        subprocess.call(['C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe'])
        logging.debug('minecraft opened')
        program = " "
    elif program == "Task manager":
        subprocess.call(['C:\Windows\System32\Taskmgr.exe'])
        logging.debug('task manager opened')
        program = " "
    elif program == "task manager":
        subprocess.call(['C:\Windows\System32\Taskmgr.exe'])
        logging.debug('task manager opened')
        program = " "
    elif program == "log":
        hrm = 'app.log'
        y = open(hrm)
        print(y.read())
        logging.debug('log function opened')
        program = " "
    elif program == "open app":
        Application = input('enter the filepath \n\nFilepath: ')
        subprocess.call([Application])
        logging.debug('Application opened')
        program = " "
    elif program == "delete file":
        j = input("enter the file name \n\nFilename: ")
        if j == 'first.py':
            logging.debug("delete failed")
            program = " "
        else:
            os.remove(j)
            logging.debug('file deleted')
            program = " "
    elif program == "create file":
        guhgu = input('enter the name of your file \n\nFilename: ')
        z = open(guhgu, "x")
        logging.debug('file created')
        program = " "
    elif program == "temp database":
        logging.debug('database opened')
        print('ALERT:This database is temporary')
        p = input('enter the name of your subject \n\nSubject: ')
        dfg = open('databasefiles' + '\\' + p + '.txt' , 'a')
        dfg = open('databasefiles' + '\\' + p + '.txt' , 'r')
        logging.debug('database file ' + p + ' opened')
        print(dfg.read())
        logging.debug('database file opened/read')
        lkj = input('would you like to add to this file? \n\nY/N: ')
        if lkj == 'y':
            nbv = input('enter your addition. \n\n')
            dfg = open('databasefiles' + '\\' + p + '.txt' , 'a')
            dfg.write(' ' + nbv)
            dfg = open('databasefiles' + '\\' + p + '.txt' , 'r')
            print(dfg.read())
            logging.debug('database file edited')
        mnb = input('press ENTER to exit the database\n\n')
        program = " "
    elif program == "chat":
        subprocess.popen('server.py')
        """Script for Tkinter GUI chat client."""
        from socket import AF_INET, socket, SOCK_STREAM
        from threading import Thread
        import tkinter


        def receive():
            """Handles receiving of messages."""
            while True:
                try:
                    msg = client_socket.recv(BUFSIZ).decode("utf8")
                    msg_list.insert(tkinter.END, msg)
                except OSError:  # Possibly client has left the chat.
                    break


        def send(event=None):  # event is passed by binders.
            """Handles sending of messages."""
            msg = my_msg.get()
            my_msg.set("")  # Clears input field.
            client_socket.send(bytes(msg, "utf8"))
            if msg == "{quit}":
                client_socket.close()
                top.quit()


        def on_closing(event=None):
            """This function is to be called when the window is closed."""
            my_msg.set("{quit}")
            send()

        top = tkinter.Tk()
        top.title("Chatter")

        messages_frame = tkinter.Frame(top)
        my_msg = tkinter.StringVar()  # For the messages to be sent.
        my_msg.set("Type your messages here.")
        scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
        # Following will contain the messages.
        msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        msg_list.pack()
        messages_frame.pack()

        entry_field = tkinter.Entry(top, textvariable=my_msg)
        entry_field.bind("<Return>", send)
        entry_field.pack()
        send_button = tkinter.Button(top, text="Send", command=send)
        send_button.pack()

        top.protocol("WM_DELETE_WINDOW", on_closing)

        #----Now comes the sockets part----
        HOST = '192.168.137.1'
        PORT = 33000
        if not PORT:
            PORT = 33000
        else:
            PORT = int(PORT)

        BUFSIZ = 1024
        ADDR = (HOST, PORT)

        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect(ADDR)

        receive_thread = Thread(target=receive)
        receive_thread.start()
        tkinter.mainloop()  # Starts GUI execution.
        oiioio = input("press enter to quit \n\n")
        program = " "
    elif program == "exit":
        logging.debug('OASIS exited')
        i = 2

#if c == chrome:
#    subprocess.call(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])
