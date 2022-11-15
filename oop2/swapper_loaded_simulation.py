#!/usr/bin/env python3

from cheatdice import *

def main():
    swapper=Cheat_Swapper()
    loaded=Cheat_Loaded_Dice()
    
    swapper_wins=0
    loaded_wins=0

    # size of the simulation
    number_of_games=100000
    game_number=0

    # begin simulation
    print("Simulation running")
    print("==================")

    while game_number<number_of_games:
        swapper.roll()
        loaded.roll()

        swapper.cheat()
        loaded.cheat()

        if sum(swapper.get_dice()) == sum(loaded.get_dice()):
            # print("Draw!")
            pass
        elif sum(swapper.get_dice()) > sum(loaded.get_dice()):
            # print("swapper wins!")
            swapper_wins+=1
        else:
            # print("loaded wins!")
            loaded_wins+=1
        game_number+=1
    # the game has ended
    print("Simulation complete")
    print("-------------------")
    print("Final scores")
    print("------------")
    print(f"Swapper won: {swapper_wins}")
    print(f"Loaded dice won: {loaded_wins}")

    # determine the winner
    if swapper_wins == loaded_wins:
        print("Game was drawn")
    elif swapper_wins > loaded_wins:
        print("Swapper won most games")
    else:
        print("Loaded dice won most games")
if __name__ == "__main__":
    main()
