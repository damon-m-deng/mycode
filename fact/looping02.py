#!/usr/bin/env python3

# open file in read mode
dnsfile = open('dnsservers.txt','r')

# create a list of lines
# .readlines() returns a list containing each line in the file as a list item
dnslist = dnsfile.readlines()

# loop over the lines
for dns_name in dnslist:
    print(dns_name, end="")

# close the file
dnsfile.close()
