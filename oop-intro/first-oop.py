#!/usr/bin/env python3

from random import randint

class Player:
    # default constructor
    # when the object is created, ctor will auto create an empty list
    def __init__(self):
        # dice is an attribute of Player, which is defined as a list
        self.dice = []
    
    # a function defined within a class: method
    def roll(self):
        self.dice = [] # clear the current dice
        for i in range(3):
            self.dice.append(randint(1,6))
    
    def get_dice(self): # getter method: use this instead of the attribute
        return self.dice

def main():
    """called at run time"""

    # create Player objects
    player1 = Player()
    player2 = Player()

    print(player1.dice) # []

    # player objs can use their method "roll"
    player1.roll()
    player2.roll()

    print(f"Player 1 rolled {player1.get_dice()}")
    print(player1.dice) # same as .get_dice(), but use getter instead
    print(f"Player 2 rolled {player2.get_dice()}")

    if sum(player1.get_dice()) ==sum(player2.get_dice()):
        print("Draw")
    elif sum(player1.get_dice()) > sum(player2.get_dice()):
        print("Player 1 wins")
    else:
        print("Player 2 wins")

if __name__ == "__main__":
    main()
