#!/usr/bin/env python3

from cheatdice import *

def main():
    swapper=Cheat_Swapper()
    loaded=Cheat_Loaded_Dice()

    swapper.roll()
    loaded.roll()

    swapper.cheat()
    loaded.cheat()

    print(f"swapper rolled {swapper.get_dice()}")
    print(f"loaded rolled {loaded.get_dice()}")

    if sum(swapper.get_dice()) == sum(loaded.get_dice()):
        print("Draw!")

    elif sum(swapper.get_dice()) > sum(loaded.get_dice()):
        print("swapper wins!")

    else:
        print("loaded wins!")
