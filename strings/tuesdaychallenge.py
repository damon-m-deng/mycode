#!/usr/bin/env python3
# bad interpreter
##!/usr/env/python3

mylist= [1,2,3,4,5, "Python"]

# bad quotes
# name= input(What is your name?\n>)
name= input("What is your name?\n>")

# This is what you should see when print runs-
# Hi <name>! Welcome to Day 2 of Python Training!

# missing (), cannot cancat str with int
# print("Hi " + name.capitalize + "! Welcome to Day " + mylist[1] + " of " + mylist[6] " Training!")
print("Hi " + name.capitalize() + "! Welcome to Day " +str(mylist[1]) + " of " + str(mylist[5]) + " Training!")

