#!/usr/bin/env python3

with open("./vlanconfig.cfg","r") as configfile:
    # display file to the terminal screen
    # print(configfile.read()) # .read() returns a string

    # display a list of lines
    configlist = configfile.readlines()
    print(type(configlist)) # .readlines() returns a list
    print(configlist)

    print("Iterate through the list")
    for row in configlist:
        print(row.strip(), end=" ")
