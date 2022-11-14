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
    # a loaded die will auto increate its roll by 1
    def cheat(self):
        i=0
        while i<len(self.dice):
            if self.dice[i]<6:
                self.dice[i]+=1
            i+=1
