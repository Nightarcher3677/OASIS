import os
import logging
import logging.handlers
import subprocess
import time, sys

#I'm adding stuff

LOG_FILENAME = 'app.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
userName = input("Welcome to OASIS! \n\nUsername: ") #Ask's the User for Username input
password = input("Password: ") # Ask's the user for their password





while userName == userName and password == password: # The Input will always lead to this while loop, so we can see if their username and password is wrong or correct.



    if userName == 'Username' and password == 'password':
        logging.debug('User signed in')
        break # Leave the loop and the whole program as the username and password is correct


    elif userName != 'username' and password != 'password': # The userName and password is NOT equal to 'elmo' and 'blue', the user cannot enter FaceSnap
        print("Your Username and Password is wrong!")
        logging.warning('Failed to sign in') # Lets the user know that the Username and password entered is wrong.
        userName = input("\n\nUsername: ") # Requests the user to have another attempt at entering their correct username
        password = input("Password: ") # Requests the user to have another attempt at entering their correct password
        count += 1 # Increments the count by 1
        continue # Continue, as the user hasn't managed to get their username and password correct yet


    elif userName == 'username and password != 'password': # The userName is equal to 'elmo', but password is NOT equal to 'blue', the user cannot enter FaceSnap
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
        import time, socket, sys
        print('Setup Server...')
        time.sleep(1)
        #Get the hostname, IP Address from socket and set Port
        soc = socket.socket()
        host_name = socket.gethostname()
        ip = socket.gethostbyname(host_name)
        port = 1234
        soc.bind((host_name, port))
        print(host_name, '({})'.format(ip))
        name = input('Enter name: ')
        soc.listen(1) #Try to locate using socket
        print('Waiting for incoming connections...')
        connection, addr = soc.accept()
        print("Received connection from ", addr[0], "(", addr[1], ")\n")
        print('Connection Established. Connected From: {}, ({})'.format(addr[0], addr[0]))
        #get a connection from client side
        client_name = connection.recv(1024)
        client_name = client_name.decode()
        print(client_name + ' has connected.')
        print('Press [bye] to leave the chat room')
        connection.send(name.encode())
        while 1 == 1:
           message = input('Me > ')
           if message == '[bye]':
              message = 'Good Night...'
              connection.send(message.encode())
              print("\n")
              break
           connection.send(message.encode())
           message = connection.recv(1024)
           message = message.decode()
           print(client_name, '>', message)
        program = " "
    elif program == "exit":
        logging.debug('OASIS exited')
        i = 2

#if c == chrome:
#    subprocess.call(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])
