#!/usr/bin/env python3

## Project name: what class should you choose in WoW (World of Warcraft)?
## Project description: by asking users to answer a series of questions to make a recommendation of the class they should choose for their WOW character
## credit/reference: https://worldofwarcraft.com/en-us/game/classes
def main():
    warrior = {
            "class name":"warrior",
            "class description":"Warriors equip themselves carefully for combat and engage their enemies head-on, letting attacks glance off their heavy armor."
            }
    rogue = {
            "class name":"rogue",
            "class description":"For rogues, the only code is the contract, and their honor is purchased in gold. Free from the constraints of a conscience, these mercenaries rely on brutal and efficient tactics."
            }
    priest = {
            "class name":"priest",
            "class description":"Priests are devoted to the spiritual, and express their unwavering faith by serving the people."
            }
    classes = [warrior, priest, rogue]

    score = 0

    while True:
        question1 =input("You walk in a villiage.\n You hear people are talking about monsters are spotted in the north of the town. What do you do? \n 1. Monster?! I am on my way \n 2. Let me do some research first\n 3. Let me see if there's a bounty for this quest\n")
        # Error handling:
        # user may not always provide a number, which will cause int() to fail
        try:
            value = int(question1)
            if(value == 1):
                score -= 10
                break
            elif(value == 2):
                score += 10
                break
            elif(value == 3):
                score += 5
                break
            else:
                print("please enter 1, 2 or 3.")
        except ValueError:
            print("Please provide a number.")

    while True:
        # Skipped error handling by comparing to a string
        question2 =input("You see a group of giant rat. What do you do? \n 1. Ewwww!!! \n 2. Rat meat? Just more protein for me!\n 3. I wonder if I will catch any nasty diseases from the rats...\n")
        if(question2 == '1'):
            score += 10
            break
        elif(question2 == '2'):
            score -= 10
            break
        elif(question2 == '3'):
            score += 5
            break
        else:
            print("please enter 1, 2 or 3.")

    while True:
        question3 =input("You killed the group of giant rat. What do you do? \n 1. Loot!!! \n 2. Making sure there are no open wounds on me\n 3. Is that it? I need more!\n")
        if(question3 == '1'):
            score += 5
            break
        elif(question3 == '2'):
            score += 10
            break
        elif(question3 == '3'):
            score -= 10
            break
        else:
            print("please enter 1, 2 or 3.")
    if(score > -30 and score < 0):
        print(f"Your recommended class is {classes[0]['class name']}.\n {classes[0]['class description']}")
    elif(score > 20):
        print(f"Your recommeded class is {classes[1]['class name']}.\n {classes[1]['class description']}")
    else:
        print(f"Your recommended class is {classes[2]['class name']}.\n {classes[2]['class description']}")

if __name__=="__main__":
    main()
