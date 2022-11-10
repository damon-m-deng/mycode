#!/usr/bin/env python3

import shutil # offers high level file operation such as copy, create and remote operations
import os # provides functions to interact with the operating system

def main():

    os.chdir("/home/student/mycode") # force the python program to start in ../mycode dir instead of current dir (5g)

    # shutil.copy(source, destination)
    # copies a SINGLE FILE from source to destination
    # this function returns a string of the path of the copied file
    shutil.copy("5g_research/sdn_network.txt","5g_research/sdn_network.txt.copy")

    # before creating the backup folder, delete any existing backups to prevent errors
    os.system("rm -rf /home/student/mycode/5g_research_backup")
    # shutil.copytree(source, destination)
    # copies an entier folder and everything this folder contains
    # returns a string of the path of the copied folder
    shutil.copytree("5g_research/","5g_research_backup") # backing up the entire 5g folder

if(__name__=="__main__"):
    main()
