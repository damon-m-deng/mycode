#!/usr/bin/env python3

# open file in read mode
with open('dnsservers.txt','r') as dnsfile:
    # loop across the lines in the file
    for svr in dnsfile:
        svr = svr.rstrip('\n') # remove newline chat if exist

        # if the string svr ends with 'org'
        if(svr.endswith('org')):
            with open('org-domain.txt','a') as srvfile: 
                # 'a': append mode --add lines to the end of the file
                # 'w': file will be emptied before the byte insertion
                srvfile.write(svr+"\n") # <file>.write(byte): write bytes to the file
        elif(svr.endswith('com')):
            with open('com-domain.txt', 'a') as srvfile:
                srvfile.write(svr+"\n")
