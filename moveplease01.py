#!/usr/bin/env python3

'''docstring: move a file'''

import shutil
import os

def main():
    '''main function'''

    ## 'cd' to raynor.obj's folder
    os.chdir('/home/student/mycode')

    ## move raynor.obj to ceph_storage folder
    # shutil.move(source, destination)
    # moves a SINGLE file or FOLDER to the given destination
    # will return a string of the absolute path of the NEW location
    shutil.move('raynor.obj','ceph_storage')

    ## rename kerrigan.obj
    new_name = input("What is the new name for kerrigan.obj? \n")
    shutil.move('ceph_storage/kerrigan.obj','ceph_storage/'+new_name)

if __name__=="__main__":
    main()
