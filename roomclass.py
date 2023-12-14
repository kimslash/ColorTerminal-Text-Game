# Kim K.
# CSC110
# 12/13/2023
# room object file (CSC110 Term Project)
# This program exists to make the unique room objects used to make the game work.

from random import randint
from colorama import Fore, Back

import fileprocess

# maybe they shouldn't be global but it's such a small py file it's probably not that big of a deal
scents = ["a little sweet", "somewhat sour", "somehow, a bit savory", "neutral", "weird..", "stinky..", "yucky..", "mossy", "kinda like cinnamon", "sorta like garlic"]
frcolors = [Fore.CYAN, Fore.BLUE, Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX]
bgcolors = [Back.BLACK, Back.LIGHTBLACK_EX]
grcolors = [Fore.LIGHTBLACK_EX, Fore.BLACK]



class RoomProfile():
    # i honestly really wanna call this something like initializeroom
    # but from what i've found it'd be a crime against python programmers
    # to do so
    def __init__(self):
        # initalizes A LOT of properties of the class object
        # i hope they don't require an explanation
        self.value = "nil"
        self.name = "Room of being unnamed"
        self.scent = scents[randint(0, 9)]
        self.size = randint(50, 100)
        self.game = ""
        
        var = randint(0, 6)
        self.textcolor = frcolors[var]
        self.objcolor = frcolors[var]
        
        var2 = randint(0, 1)
        self.skycolor = bgcolors[var2]
        self.groundcolor = grcolors[var2]
        
        
        # gets 6 sprites from my asset folder, i made all of them by the way, everything in GameAssets is made by me
        self.spriteline = [fileprocess.processfile(f"GameAssets/randsprite{randint(1, 12)}.txt"), fileprocess.processfile(f"GameAssets/randsprite{randint(1, 12)}.txt"), 
                      fileprocess.processfile(f"GameAssets/randsprite{randint(1, 12)}.txt"), fileprocess.processfile(f"GameAssets/randsprite{randint(1, 12)}.txt"),
                      fileprocess.processfile(f"GameAssets/randsprite{randint(1, 12)}.txt"), fileprocess.processfile(f"GameAssets/randsprite{randint(1, 12)}.txt")]
        
        # these last three just hold stuff like bordering rooms, the game, and the item inventory
        
        self.iteminv = []
        self.pygame = "None"
        self.borderingrooms = ["", "", "", ""]