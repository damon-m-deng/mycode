#!/usr/bin/env python3

with open("./vlanconfig.cfg", "r") as configfile:
    # display file to the screen
    configblog = configfile.read()
    print(configblog)
    print(type(configblog)) # .read() returns a string

    # break configblog across line boundaries (strip out \n)
    configlist = configblog.splitlines()
    print(configlist)
    print(type(configlist)) # .splitlines() returns a list
