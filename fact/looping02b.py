#!/usr/bin/env python3

# use "with" with open()
# "with" statement has colon--auto indentation
# anything indented under "with" statement, the file remains open.
# when the indentation ends, the file is automatically closed

with open('dnsservers.txt','r') as dnsfile:
    # indent to keep the dnsfile open
    
    # create a list of lines (Optional)
    # dnslist = dnsfile.readlines()

    # loop over lines
    for dns_name in dnsfile:
        print(dns_name, end="")

## No need to close the file -- closed automatically
