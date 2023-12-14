# Kim K.
# CSC110
# 12/13/2023
# Room World main.py (CSC110 Term Project)
# This program is the master program that runs the entire game, start the program to play.

#>>>>> PLEASE MAKE SURE TO INSTALL colorama WITH `pip install colorama` <<<<<

# time only used once, in a for loop in winner()
import time

# this library allows me to easily send instructions to color strings when they're outputted
from colorama import Fore, Back, Style
import os

# these imports are either self-explainable or are my own programs, if they are, they are explained in detail there
from importlib import import_module

from screenrenderer import roomrender, rendercustom

from fileprocess import processfile, separatedarray, processmap
from fileprocess import processprovidable as provfile

import validator as inpval

from random import choice as randchoice
from random import randint

# for some reason, unicode characters need a different type of encoing to be read from a .txt file
# it's a bit weird since now I don't know if the file is being written to
tscreenarray = processfile("GameAssets/titlescreen.txt")
maparray = processfile("GameAssets/mapsprite.txt")
invarray = processfile("GameAssets/invsprite.txt")
scrarray = processfile("GameAssets/scoresprite.txt")
welscreenarray = processfile("GameAssets/welcomescreen.txt")
# global dictionary var for the player's inventory
playerinventory = {}
playerscore = 0

def welcomesequence():
    # does basically the same thing as the title screen, just gives more exposition, this is explained at titlesequence() comments
    os.system('cls')
    titlecard = [
        "You find yourself in a weird room...",
        "The only thing you see is a massive \"WELCOME\" sign. But your mind tells",
        "you there's more to do here, you imagine an arrow pointing from",
        "yourself to a big green checkmark... What does that mean???? Don't",
        "ask me! Maybe the game wants you to have fun and succeed!",
        "Type \"Continue\" to begin! You'll be sent to a random room with stuff to do!\n",
        "(and to win, you need to play every pygame at least once! good luck!!!!!)",
        "----------------------------------------------------------------------------------------------------"
    ]
    rendercustom(Fore.LIGHTGREEN_EX, Back.BLACK, welscreenarray, titlecard)
    
    inpval.validchoice("| Continue | -> ", Fore.CYAN, ["CONTINUE"])



def getgamedata():
    # gets a sorta readable format for both of these files
    rooms = provfile("ProvidedAssets/rooms.txt")
    pygames = provfile("ProvidedAssets/games.txt")
    # since the room "index" here is not unique for every item, it's best to have it in a 2d table
    objects = separatedarray("ProvidedAssets/objects.txt")
    
    # IT ACTUALLY WORKS!!!!!!!! it returns a dictionary with UNIQUE room objects!!!!!!
    # this is basically THE master dictionary that'll hold this entire project together
    global roomdata
    # this var basically compresses all of the previous 3 and also takes into account the layout to map out where each room is
    roomdata = processmap("ProvidedAssets/map_layout.txt", rooms, objects, pygames)



def checkmovedirection(roomindex, movedir):
    # just a tiny function to check if there's a valid neighbor
    if roomdata[roomindex].borderingrooms[movedir-1] != "":
        roomenter(roomdata[roomindex].borderingrooms[movedir-1], f"Successfully travelled here from Room {roomdata[roomindex].value}!")
    
    roomenter(roomindex, "Seems like there isn't a room in that direction...")



def openinventory(roomindex):
    # quick for loop to print the keys and values of the playerinventory dictionary
    # also a funny if statement in case the player has no items of any kind
    os.system('cls')
    inventorytable = ["(In no particular order) Here are your objects:\n"]
    for key, val in playerinventory.items():
        inventorytable.append(f"{key}: {val}")
        
    invcolor = Fore.YELLOW
    sendofftext = "You're back after checking your inventory."
    if len(inventorytable) == 1:
        inventorytable[0] = ("Wow... You have absolutely nothing.")
        sendofftext = "You're back after wasting your time..."
        invcolor = Fore.LIGHTBLACK_EX
    else: inventorytable.append("\n(no, the objects have no use or purpose but)\n(at least you get to keep count of them ^_^)")
        
    rendercustom(invcolor, Back.BLACK, invarray, inventorytable)
    inpval.validchoice("| Return | -> ", Fore.CYAN, ["RETURN"])
    roomenter(roomindex, sendofftext)
    

def checkforwinner():
    # checks if the win conditions are met by counting remaining items with a tally
    losetally = 0
    for roomindex in roomdata.keys():
        if roomdata[roomindex].iteminv != []: losetally += 1
        
    if losetally == 0: return True
    else: return False

randomcolors = [Fore.RED, Fore.LIGHTRED_EX, Fore.YELLOW, Fore.LIGHTYELLOW_EX, Fore.GREEN, Fore.LIGHTGREEN_EX, Fore.CYAN, Fore.LIGHTCYAN_EX,
                Fore.BLUE, Fore.LIGHTBLUE_EX, Fore.MAGENTA, Fore.LIGHTMAGENTA_EX]



def winner():
    # a quick little program to celebrate the winner, it then exits with an exit code of 0 (success)
    for _ in range(0, 20):
        os.system('cls')
        print(f"""{randomcolors[randint(0, 11)]}\n\n\n{f"Yay you won!!! ^_^":^100}\n\n{f"Congrats! This program will exit shortly.":^100}{Style.RESET_ALL}""")
        time.sleep(.5)
    exit(0)



def checkforgame(roomindex):
    # nest ifs and fors that
    # 1. check if there's a game
    # 2. use import_module from the importlib library to actually play said game
    # 3. when game is done, it takes the room's items and gives them to the player
    # 4. also runs the checkforwinner() to check if... the player wins...
    if roomdata[roomindex].pygame != "None":
        if __name__ == "__main__":
            fixedgame = roomdata[roomindex].pygame.replace(" ","").lower()
            pygametemp = import_module(f"ProvidedAssets.PyGames.{fixedgame}")
            pygametemp.main()
            roomdata[roomindex].pygame = "None"
            
            for var in range(0, len(roomdata[roomindex].iteminv)):
                
                if roomdata[roomindex].iteminv[var] in playerinventory.keys():
                    playerinventory[roomdata[roomindex].iteminv[var]] += 1
                    
                else: playerinventory[roomdata[roomindex].iteminv[var]] = 1
            global playerscore
            playerscore = playerscore + randint(50, 100)            
            roomdata[roomindex].iteminv = []
                
            if checkforwinner():
                winner()
            else:
                roomenter(roomindex, f"{Fore.LIGHTMAGENTA_EX}Since you tried playing the game, check your inventory!{Fore.LIGHTGREEN_EX}")

    roomenter(roomindex, "There's either no game in this room, or you already beat it!")



def openmap(roomindex):
    os.system('cls')
    # while it's unlikely there will be a room with no neighbors, because that'll literally be impossible, and if player
    # was in said room they'd be trapped, i still took the time to make a scenario if that were the case
    
    # if there's more than 1 room the for loop will append their name and location to the table, then render it along with a cool sprite I made
    
    availablerooms = ["List of available rooms:\n"]
    directions = ["North", "West", "East", "South"]
    for var in range(0, len(roomdata[roomindex].borderingrooms)):
        if roomdata[roomindex].borderingrooms[var] != "":
            availablerooms.append(f"Room {roomdata[roomdata[roomindex].borderingrooms[var]].value}: {roomdata[roomdata[roomindex].borderingrooms[var]].name} is to the {directions[var]}.\n")
            
    if len(availablerooms) == 1: 
        availablerooms[0] = "YOU'RE TRAPPED... NOOO!!!!"
        rendercustom(Fore.LIGHTRED_EX, Back.RED, maparray, availablerooms)
        inpval.validchoice("| Return | -> ", Fore.CYAN, ["RETURN"])
        roomenter(roomindex, f"{Fore.RED}Returned after realizing you're trapped.{Fore.LIGHTGREEN_EX}")
        
    rendercustom(roomdata[roomindex].objcolor, Back.BLACK, maparray, availablerooms)

    inpval.validchoice("| Return | -> ", Fore.CYAN, ["RETURN"])
    roomenter(roomindex, "Returned after using the map")

def getscore(roomindex):
    # the quickest possible function could've made I made this at 11:23PM because i just re-read the outline and it asked for a savable score
    # so..... here it is!!!
    os.system('cls')
    inventorytable = [f"Your awesome player score is... {Fore.WHITE}{playerscore}{roomdata[roomindex].textcolor}!!!",
                      "You get a random amount of score after playing the pygames."]

    rendercustom(roomdata[roomindex].textcolor, Back.BLACK, scrarray, inventorytable)
    inpval.validchoice("| Return | -> ", Fore.CYAN, ["RETURN"])
    roomenter(roomindex, "Returned to room after viewing your score.")
    

def roomenter(roomindex, response=f"If your response is valid it'll be acknowledged here in the future."):
    # this is the most commonly called function in this program by far, it renders the given room object and
    # gives the player a LOT of options, it's basically the game and the main menu at the same time
    
    os.system('cls')
    print(f"You've entered Room {roomdata[roomindex].value}: {roomdata[roomindex].name}")
    roomrender(roomdata[roomindex], playerscore)

    
    print(f"""{Fore.LIGHTGREEN_EX}{f"<< You find yourself in Room {roomdata[roomindex].value}: {roomdata[roomindex].name}! >>":^100}
{f"<< {response} >>":^100}\n""")
    
    # the choice and validation functions are explained in their respective comments
    titlechoices = ["MOVE NORTH", "MOVE WEST", "MOVE EAST", "MOVE SOUTH", "INVENTORY", "CHECK SCENT", "CHECK SIZE", "GAME", "OPEN MAP", "MY SCORE"]
    choice = inpval.validchoice("| Options Shown Above | -> ", Fore.CYAN, titlechoices)
    
    # all of these function calls also have explanations in their comments
    if choice in [1, 2, 3, 4]:
        checkmovedirection(roomindex, choice)
    elif choice == 5:
        openinventory(roomindex)
    elif choice == 6:
        roomenter(roomindex, f"{roomdata[roomindex].textcolor}This room smells {roomdata[roomindex].scent}.{Fore.LIGHTGREEN_EX}")
    elif choice == 7:
        roomenter(roomindex, f"{Fore.LIGHTMAGENTA_EX}This room is EXACTLY {roomdata[roomindex].size} meters... But you forgot in which direction.{Fore.LIGHTGREEN_EX}")
    elif choice == 8:
        checkforgame(roomindex)
    elif choice == 9:
        openmap(roomindex)
    elif choice == 10:
        getscore(roomindex)



def randroomtp():
    # all this does is pick a random room to start in, that's it
    roomindex = randchoice(list(roomdata.keys()))
    roomenter(roomindex)



def newgame():
    os.system('cls')
    # each of these functions have comments to explain what they are if you're curious
    getgamedata()
    
    welcomesequence()
    
    randroomtp()


def titlesequence():
    # clears the screen, super super useful!!!
    os.system('cls')
    # i can't use a multiline string in this scenario since my function uses a for loop to iterate through
    # a table of strings, like this one
    titlecard = [
        "Welcome to the game!",
        "",
        "Press Enter to begin! (or really any input)",
        "----------------------------------------------------------------------------------------------------"
    ]
    
    # first two vars are colors, then it's the processed "image" file and the last is the table you see above
    rendercustom(Fore.CYAN, Back.BLUE, tscreenarray, titlecard)
    
    input(f"{Fore.CYAN}| Press Enter | -> ")
    newgame()


def main():
    titlesequence()

main()

#>>> SUMMARY CAN BE FOUND IN "SUMMARY.TXT" IN THE CWD <<<