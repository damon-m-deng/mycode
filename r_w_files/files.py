#!/usr/bin/env python3

# open() creates a file object: default mode: READ
# All file objects created with open() need to be closed, unless the function is used via 'with

# .read(size): size is optional. If omitted, reads the entire file and return it
# myfile = open('./text.txt')
myfile = open('./text.txt', 'r')
print("--print first 10 chars--")
print(myfile.read(10))

print('--reads a line, and another line .readline()--')
print(myfile.readline()) # reads a signle line from the file (including \n new line)
print(myfile.readline()) # reads the next single line (including \n); returns empty string when EOF

print('--reads all lines .readlines()--')
print(myfile.readlines()) # returns a LIST containing all lines in the file

myfile.close()

