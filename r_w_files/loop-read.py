#!/usr/bin/env python3

with open('text.txt','r') as openfile:
    for line in openfile:
        print(line, end='')
