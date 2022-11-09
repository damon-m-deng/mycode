#!/usr/bin/env python3

def main():
    rounds = 1
    while (True):
        if(rounds>3):
            print("Sorry, the answer is Brian.")
            break
        else:
            print("Finish the movie title, 'Monty python\'s The Life of _____'")
            answer = input("Your guess--> ")
            if(answer=="Brian"):
                print("Correct!")
                break
            else:
                print("Sorry, try again")
            rounds = rounds+1

if(__name__ == "__main__"):
    main()
