import logging
import logging.handlers
import subprocess
import time, sys



LOG_FILENAME = 'app.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
userName = input("Welcome to OASIS! \n\nUsername: ") #Ask's the User for Username input
password = input("Password: ") # Ask's the user for their password


count = 0 # Create a variable, to ensure the user has limited attempts at entering their correct username and password
count += 1 # The user has already had one attempt above, therefore count has been incremented by 1 already.


while userName == userName and password == password: # The Input will always lead to this while loop, so we can see if their username and password is wrong or correct.



    if userName == 'elmo' and password == 'blue':
        logging.debug('User signed in') # The userName and password is equal to 'elmo' and 'blue', which is correct, they can enter FaceSnap!
        break # Leave the loop and the whole program as the username and passowrd is correct


    elif userName != 'elmo' and password != 'blue': # The userName and password is NOT equal to 'elmo' and 'blue', the user cannot enter FaceSnap
        print("Your Username and Password is wrong!")
        logging.warning('Failed to sign in') # Lets the user know that the Username and password entered is wrong.
        userName = input("\n\nUsername: ") # Requests the user to have another attempt at entering their correct username
        password = input("Password: ") # Requests the user to have another attempt at entering their correct password
        count += 1 # Increments the count by 1
        continue # Continue, as the user hasn't managed to get their username and password correct yet


    elif userName == 'elmo' and password != 'blue': # The userName is equal to 'elmo', but password is NOT equal to 'blue', the user cannot enter FaceSnap
        print("Your Password is wrong!")
        logging.warning('Failed to sign in') # Lets the user know that their password is wrong
        userName = input("\n\nUsername: ") # Requests the user to have another attempt at entering their correct username
        password = input("Password: ") # Requests the user to have another attempt at entering their correct password
        count += 1 # increments the count by 1
        continue # Continue, as the user hasn't managed to get their username and password correct yet


    elif userName != 'elmo' and password == 'blue': # The userName is NOT equal to 'elmo', however password is equal to 'blue', the user cannot enter FaceSnap
        print("Your Username is wrong!")
        logging.warning('Failed to sign in') # Lets the user know that their username is wrong
        userName = input("\n\nUsername: ") # Requests the user to have another attempt at entering their correct username
        password = input("Password: ") # Requests the user to have another attempt at entering their correct password
        count += 1 # Increments the count by 1
        continue # Continue, as the user hasn't managed to get their username and password correct yet






time.sleep(1)

i = 1
while 1 == i:
    logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
    program = input("choose your program. \n\nProgram: ")
    c = "notchrome"
    m = "notminecraft"
    t = "idunno"
    o = "fcgh"
    l = "leavemealone"
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
        c = "chrome"
        if c == "chrome":
            subprocess.call(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])
            logging.debug('chrome opened')
            program = " "
    elif program == "chrome":
        c = "chrome"
        if c == "chrome":
            subprocess.call(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])
            logging.debug('chrome opened')
            program = " "
    elif program == "Minecraft":
        m = "Minecraft"
        if m == "Minecraft":
            subprocess.call(['C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe'])
            logging.debug('minecraft opened')
            program = " "
    elif program == "minecraft":
        m = "Minecraft"
        if m == "Minecraft":
            subprocess.call(['C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe'])
            logging.debug('minecraft opened')
            program = " "
    elif program == "Task manager":
        t = "Minecraft"
        if t == "Minecraft":
            subprocess.call(['C:\Windows\System32\Taskmgr.exe'])
            logging.debug('task manager opened')
            program = " "
    elif program == "task manager":
        t = "Minecraft"
        if t == "Minecraft":
            subprocess.call(['C:\Windows\System32\Taskmgr.exe'])
            logging.debug('task manager opened')
            program = " "
    elif program == "log":
        l = "Minecraft"
        if l == "Minecraft":
            hrm = 'app.log'
            y = open(hrm)
            print(y.read())
            logging.debug(y.read())
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
        dfg = open(p + '.txt', 'a')
        dfg = open(p + '.txt', 'r')
        logging.debug('database file ' + p + ' opened')
        print(dfg.read())
        logging.debug('database file opened/read')
        lkj = input('would you like to add to this file? \n\nY/N: ')
        if lkj == 'y':
            nbv = input('enter your addition. \n\n')
            dfg = open(p + '.txt', 'a')
            dfg.write(' ' + nbv)
            dfg = open(p + '.txt', 'r')
            print(dfg.read())
            logging.debug('database file edited')
        mnb = input('press ENTER to exit the database\n\n')
        program = " "
    elif program == "chat":
        import time, socket, sys
        print('Client Server...')
        time.sleep(1)
        #Get the hostname, IP Address from socket and set Port
        soc = socket.socket()
        shost = socket.gethostname()
        ip = socket.gethostbyname(shost)
        #get information to connect with the server
        print(shost, '({})'.format(ip))
        server_host = input('Enter server\'s IP address:')
        name = input('Enter Client\'s name: ')
        port = 1234
        print('Trying to connect to the server: {}, ({})'.format(server_host, port))
        time.sleep(1)
        soc.connect((server_host, port))
        print("Connected...\n")
        soc.send(name.encode())
        server_name = soc.recv(1024)
        server_name = server_name.decode()
        print('{} has joined...'.format(server_name))
        print('Enter [bye] to exit.')
        while 1 == 1:
           message = soc.recv(1024)
           message = message.decode()
           print(server_name, ">", message)
           message = input(str("Me > "))
           if message == "[bye]":
              message = "Leaving the Chat room"
              soc.send(message.encode())
              print("\n")
              break
           soc.send(message.encode())

        program = " "
    elif program == "exit":
        logging.debug('OASIS exited')
        i = 2

#if c == chrome:
#    subprocess.call(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])
