#!/usr/bin/env python3

import requests
import wget

API="https://pokeapi.co/api/v2/pokemon/"

def main():
    pokenum=input("Pick a number between 1 and 151!\n")
    pokeapi=requests.get(API+pokenum).json()
    # 1. slicing: get the png URL
    imgurl= pokeapi['sprites']['front_default']
    # save the PNG in ~/static
    wget.download(imgurl, "/home/student/mycode/api-iss/")

    # 2. slicing WITH a for
    with open('move_names.index','w') as movefile:
        moves=pokeapi['moves']
        for move in moves:
            print(move['move']['name'], file=movefile)

    # 3. count how many generations
    # Not using WITH loop
    count=len(pokeapi['game_indices'])
    print(count)

    # using WITH loop
    counter=0
    game_indices=pokeapi['game_indices']
    for index in game_indices:
        counter+=1
    print(counter)
if __name__=="__main__":
    main()
