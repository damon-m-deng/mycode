#!/usr/bin/env python3

import crayons
import json

# function to push commands
def commandpush(devicecmd): # devicemd==dict
    for ip in devicecmd.keys(): # looping through the dict
        print(f'{crayons.red("Handshaking")}. .. ... connecting with {ip}') # fstring

        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {mycmds}')
    return None

# create function devicereboot which accept a list of IPs as a single arg. The function should iterate through the list of IPs, and for each one, print, "Connecting to...", then print "REBOOTING NOW!"
def devicereboot(ip_list):
    for ip in ip_list:
        print(f'Connecting to...', ip)
        print('REBOOTING NOW!')

def main():
    """called at runtime"""

    # dict containing IPs mapped to a list of physical interfaces and their state
    # devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}
    
    # replace the above hard-coded dict with imported JSON
    with open("./devicecmd.json","r") as devicecmdfile:
        # need to import json lib
        # json.load(filename): takes a file obj and returns the json obj
        devicecmd = json.load(devicecmdfile)
        print(type(devicecmd)) # dict

    print(f"Welcome to the {crayons.blue('network')} device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices

    ip_list = devicecmd.keys()
    devicereboot(ip_list)

if __name__ == "__main__":
    main()
