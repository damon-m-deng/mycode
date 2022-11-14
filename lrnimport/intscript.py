#!/usr/bin/env python3

# "from" keyword: instead of importing the whole lib, only import the part where "call" is needed
## FAIL: below line is intended to use 3rd party lib--subprocess, but this .py file/module has the same name. By definition, local module takes priority. Therefore, program will fail because local module does not have a function called "call"
## when the program failed, python will create a compiled file ending in .pyc inside a dir called __pycache__, which is used for throw away files
from subprocess import call

# Subprocess in python is used to run new programs and scripts by spawing new processes. 
# Enables user to launch new programs right from the current python program
# call() method is used to INITIATE a program. call() returns the executed code of the program, or CalledProcessError if no program output
# ex. subprocess.call("ls","-al")

call(["ip","link","show","up"])
print("This program will check your interfaces.")

# user prompt
interface = input("Enter an interface, like, ens3: ")

# reveal IPv4 and IPv6 details
call(["ip", "addr", "show", "dev", interface])
call(["ip", "route", "show", "dev", interface])
