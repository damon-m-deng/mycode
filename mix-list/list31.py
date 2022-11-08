#!/usr/bin/env python3

import random


def main():
    wordbank= ["indentation", "spaces"]
    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

    # Add a line of code that appends the integer 4 to the list wordbank
    wordbank.append(4)
    print(wordbank)
    print(len(tlgstudents))

    # include an input asking for a number between 0 and 18, save this as the variable num
    # input() always returns a string, convert num into an integer
    num=int(input(f"Please enter a number between 0 and {len(tlgstudents)} --> "))-1

    # use the integer num to slice one of the elements from the list tlgstudents. Save the name your return as the variable student_name
    # use elements from the tlgstudents list and the student_name string, print this output
    student_name = tlgstudents[num]
    print(student_name)
    
    # choose a random student from the list
    print(random.choice(tlgstudents))

    # use wordbank to fill in the print()
    # <student_name> always uses <4> <spaces> to indent.
    print(f"{student_name} always use {wordbank[2]} {wordbank[1]} to indent.")
main()
