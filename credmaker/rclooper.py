#!/usr/bin/env python3

import csv

with open("csv_users.txt","r") as csvfile:
    # counter to create unique file names
    i=0
    # csv.reader(csvfile, dialect='excel',**fmtparams)
    # returns a reader object which will iterate over lines in a given csvfile
    # print(csv.reader(csvfile)) # <_csv.reader object at 0x7f249cd1e0a0>
    for line in csv.reader(csvfile):
        i+=1
        filename = f"admin.rc{i}" # this f string says "fill in the value of i"

        # open/create a file via "with"
        with open(filename, 'w') as rcfile:
            print("export OS_AUTH_URL="+line[0], file=rcfile)
            print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
            print("export OS_PROJECT_NAME="+line[1], file=rcfile)
            print("export OS_PROJECT_DOMAIN_NAME=" + line[2], file=rcfile)
            print("export OS_USERNAME=" + line[3], file=rcfile)
            print("export OS_USER_DOMAIN_NAME=" + line[4], file=rcfile)
            print("export OS_PASSWORD=" + line[5], file=rcfile)
print("admin.rc files created!")
