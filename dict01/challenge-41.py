#!/usr/bin/env python3

def main():
    # bonus 2: ignore user captalization
    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)\n").lower().title()

    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)\n")

    marvelchars = {
            "Starlord":{
                    "real name":"peter quill",
                    "powers":"dance moves",
                    "archenemy":"Thanos"
                    },
            "Mystique":{
                    "real name":"raven darkholme",
                    "powers":"shape shifter",
                    "archenemy":"Professor X"
                    },
            "Hulk":{
                    "real name":"bruce banner",
                    "powers":"super strength",
                    "archenemy":"adrenaline"
                }
            }
    # Bonus 1: capitalize hero's real name: string.title()
    if(char_stat == "real name"):
         print(f"{char_name}\'s {char_stat} is: {marvelchars.get(char_name).get(char_stat).title()}.")
    else:
         print(f"{char_name}\'s {char_stat} is: {marvelchars.get(char_name).get(char_stat)}.")

# bonus 3: allow the user to try again without exiting the script
if(__name__ =="__main__"):
    while(True):
        main()
