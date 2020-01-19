import os
import logging
import logging.handlers
import subprocess
import time, sys
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import ssl

LOG_FILENAME = 'app.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

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
