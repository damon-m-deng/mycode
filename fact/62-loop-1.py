#!/usr/bin/env python3

def main():
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    # 1.write a for loop that returns all the animals from the NE farm
    NE_animals = farms[0]['agriculture']
    for animal in NE_animals:
        print(animal)
if __name__ == "__main__":
    main()
