#!/usr/bin/env python3

import requests
from random import randint

# riddle function: use a flag to have 1, 2, 3 values
# define the flag in main with a default value of 1
# when user successful solve the riddle, change the flag to 2
# if user fails to solve, change the flag to 3
def riddle(flag):
    API = "https://pokeapi.co/api/v2/pokemon/" 
    pokemon=requests.get(API+str(randint(1,12))).json()
    print(pokemon['name'])
    # print(pokemon['types'][0]['type'])

    guess=1

    print("Welcome to the Pokemon Riddle!")
    print("Guess what Pokemon am I?")
    while flag==1:
        if guess==1:
            print(f"My type is {pokemon['types'][0]['type']['name']}.")
        elif guess==2:
            print(f"My ability is {pokemon['abilities'][0]['ability']['name']}.")
        elif guess==3:
            print(f"My pokedex ID is {pokemon['id']}")
        else:
            # TODO trigger gameover
            flag=2
            break
        user_input=input("Your guess is >> ").lower()
        if user_input == pokemon['name']:
            print("Congratz! That is correct")
            flag=3
            break
        guess+=1

