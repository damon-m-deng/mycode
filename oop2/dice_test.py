#!/usr/bin/env python3

from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice
from cheatdice import Cheat_mulligan
from cheatdice import Cheat_add
from cheatdice import Cheat_weighted
from cheatdice import Cheat_Sab

def main():
    player1 = Player()
    player2 = Player()

    cheater1 = Cheat_Swapper()
    cheater2 = Cheat_Loaded_Dice()
    cheater3 = Cheat_mulligan()
    cheater4 = Cheat_add()
    cheater5 = Cheat_weighted()
    cheater6 = Cheat_Sab()

    player1.roll()

    cheater1.roll() # inherited from Player class
    cheater2.roll()
    cheater3.roll()
    cheater4.roll()
    cheater5.roll()
    cheater6.roll()

    print(f"Player 1 rolled {player1.get_dice()}")
    
    print(f"Cheater 1 rolled {cheater1.get_dice()}")
    print(f"Cheater 2 rolled {cheater2.get_dice()}")
    print(f"Cheater 3 rolled {cheater3.get_dice()}")
    print(f"Cheater 4 rolled {cheater4.get_dice()}")
    print(f"Cheater 5 rolled {cheater5.get_dice()}")
    print(f"Cheater 6 rolled {cheater6.get_dice()}")
    
    cheater1.cheat()
    cheater2.cheat()
    cheater3.cheat()
    cheater4.cheat()
    cheater5.cheat()
    cheater6.cheat(player1)

    print(f"Player 1 rolled {player1.get_dice()}")
    print(f"Cheater 1 rolled {cheater1.get_dice()}")
    print(f"Cheater 2 rolled {cheater2.get_dice()}")
    print(f"Cheater 3 rolled {cheater3.get_dice()}")
    print(f"Cheater 4 rolled {cheater4.get_dice()}")
    print(f"Cheater 5 rolled {cheater5.get_dice()}")
    print(f"Cheater 6 rolled {cheater6.get_dice()}")
    
    if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
        print("Draw!")

    elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
        print("Cheater 1 wins!")

    else:
        print("Cheater 2 wins!")

if __name__ == "__main__":
    print("cheater 1: swap the last die to a 6")
    print("cheater 2: increase all dice by 1")
    print("cheater 3: re-roll if the sum is less than 15")
    print("cheater 4: rolls an additional die")
    print("cheater 5: first die cannot be rolled below a 3")
    print("cheater 6: switch player 1's dice, all dice cannot be more than 3")
    main()
