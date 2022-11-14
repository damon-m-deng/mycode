#!/usr/bin/env python3

from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice

def main():
    player1 = Player()
    player2 = Player()

    cheater1 = Cheat_Swapper()
    cheater2 = Cheat_Loaded_Dice()

    cheater1.roll() # inherited from Player class
    cheater2.roll()

    print(f"Player 1 rolled {cheater1.get_dice()}")
    print(f"Player 2 rolled {cheater2.get_dice()}")

    cheater1.cheat()
    cheater2.cheat()

    print(f"Player 1 rolled {cheater1.get_dice()}")
    print(f"Player 2 rolled {cheater2.get_dice()}")

    if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
        print("Draw!")

    elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
        print("Cheater 1 wins!")

    else:
        print("Cheater 2 wins!")

if __name__ == "__main__":
    main()
