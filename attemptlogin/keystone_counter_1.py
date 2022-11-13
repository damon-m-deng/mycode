#!/usr/bin/env python3

# parse keystone.common.wsgi and return number of failed login attempts

loginfail = 0

# open the file for reading
keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi','r')

# turn the file into a list of lines, and store the list in the memory
## list is convenient to use, but if the file is large, it will cause a lot of overhead for the memory
lines = keystone_file.readlines()

# loop over the list of lines
for line in lines:
    if "- - - - -] Authorization failed" in line:
        loginfail += 1
print("The number of failed log in attempts is", loginfail)

# close the open file
keystone_file.close()
