import os
import logging
import logging.handlers
import subprocess
import time, sys
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import ssl

file = input("enter the filename here. \n\nFile: ")
f = open(file)
print(f.read())
i = input('press ENTER to continue')
