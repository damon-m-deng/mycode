#!/usr/bin/env python3

# ask a user to choose a farm, return the plants/animals that are raised on that farm
# return animals only

# farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
#         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
#         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]

def main():
    for farm in farms:
        print("-", farm['name'])
    user_input = input("Please select a farm.  ")

    animals = ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]
    
    for farm in farms:
        if(farm['name'].lower() == user_input.lower()):
            # print(farm['agriculture'])
            for animal in farm['agriculture']:
                if animal in animals:
                    print(animal)

if __name__ == "__main__":
    main()
