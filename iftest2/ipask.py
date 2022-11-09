#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - testing if strings test true"""

ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# a provided string will test true
if (ipchk=="192.168.70.1"):
    print("Looks like the IP address of the gateway was set: "+ipchk+" this is not recommended.")
elif ipchk:
   print("Looks like the IP address was set: " + ipchk)
else:
    print("no input provided")
