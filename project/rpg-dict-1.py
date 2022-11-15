#!/usr/bin/env python3

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there is an item in the room, if so, print it
    if "item" in rooms[currentRoom]:
        print('You see a '+ rooms[currentRoom]['item'])
    print("---------------------------")

# player's inventory
inventory=[]

# a dictionary links a room to other rooms
rooms ={
        'Hall':{'south':'Kitchen'},
        'Kitchen':{'north':'Hall'}
        }

# start the player in the hall
currentRoom='Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # The player must type something in
    # otherwise input will keep asking
    move=""
    while move == '':
        move=input('>')

    # normalizing input:
    move=move.lower().split(" ", 1) # ["go","south"] ["get","key"]

    # if user types 'go' first
    if move[0] == 'go':
        # check that they are allowed whereever they want to go
        if move[1] in rooms[currentRoom]:
            # success: change the currentroom to the new room
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('You can\'t go that way!')

    # if user types 'get' first
    if move[0]=='get':
        # make 2 checks
        # 1. if the current room contains an item
        # 2. if the item in the room matches the user input "get ITEM"
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory.append(move[1])
            print(move[1]+' got!')
            # delete the item KV pair from the room's dict
            del rooms[currentRoom]['item']
        # if there is no item in the room, or the item does not match user's input
        else:
            print("Cannot get "+move[1]+" in the "+currentRoom+"!")
