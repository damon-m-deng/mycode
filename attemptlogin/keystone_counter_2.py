#!/usr/bin/python3
# parse keystone.common.wsgi and return number of failed login attempts
## improve from version 1
## No need to use readlines() to store all lines in memory
## Remove the need to manually close the file when finished

loginfail = 0 # counter for fails
# open the file for reading

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r") as keystone_file:

    # loop over the list of lines
    for line in keystone_file:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            # print out the IP address of the failed attempt
            # print(line)
            print(line.split(" ")[-1])
print("The number of failed log in attempts is", loginfail)

