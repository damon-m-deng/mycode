#!/usr/bin/env python3

from random import randint

class Player:
    # default ctor with an empty list
    def __init__(self):
        self.dice=[]
    
    def roll(self):
        self.dice=[]
        for i in range(3):
            self.dice.append(randint(1,6))
    def get_dice(self):
        return self.dice

class Cheat_Swapper(Player): # class Child(Parent)
    def cheat(self):
        self.dice[-1] = 6 # cheater will swap the last die with a 6

class Cheat_Loaded_Dice(Player): 
    # a loaded die will auto increase its roll by 1
    def cheat(self):
        i=0
        while i<len(self.dice):
            if self.dice[i]<6:
                self.dice[i]+=1
            i+=1

class Cheat_mulligan(Player):
    # re-roll if the sum is less than 9
    def cheat(self):
        while sum(self.dice)<15:
            self.roll()

class Cheat_add(Player):
    # Rolls one additional die
    def cheat(self):
        self.dice.append(randint(1,6))

class Cheat_weighted(Player):
    # first die cannot be roll below a three
    def cheat(self):
        if self.dice[0]<3:
            self.dice[0] = randint(3,6)

class Cheat_Sab(Player):
    # switch other player's dice with a die that cannot roll above 3
    def cheat(self, other):
        other.dice=[]
        for i in range(3):
            other.dice.append(randint(1,3))
