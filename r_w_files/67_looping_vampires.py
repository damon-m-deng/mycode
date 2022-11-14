#!/usr/bin/env python3

with open("./dracula.txt","r") as novel:
    # 1. read the content of the novel as a FILE OBJECT
    # novel_file_obj = novel.read()
    # print(type(novel_file_obj)) # string

    # 2. Loop every line in the novel, print each line out
    novel_list = novel.readlines() # list
    
    # 5. count how many lines that contains the word "vampire"
    count=0

    # 6. write all the line that contains "vampire" in it, and write them to a second file named "vampytimes.txt"
    with open("vampytimes.txt","w") as writefile:
        for line in novel_list:
            # 3. only print out the line if it has the word "vampire" in it
            # 4. make the search case insensitive
            if("vampire" in line.lower()):
                count+=1
                print(line)
                print(line, file=writefile)
    print(count)
