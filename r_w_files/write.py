#!/usr/bin/env python3

# writing data to a file with 'with' auto-close
with open('./text.txt', 'a') as outfile: # 'w' clear the previous content, 'a' append
    outfile.write('\n\nI am a new line written from Python')
    outfile.write('\nLook, I am another line written from Python.')
    # no need to call close() because of the indentation
    print('--checking the update--')

with open('./text.txt','r') as outfile:
    print(outfile.readlines())
