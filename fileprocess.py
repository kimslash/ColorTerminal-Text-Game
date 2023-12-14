# Kim K.
# CSC110
# 12/13/2023
# file processing program (CSC110 Term Project)
# This program takes in different "types" of .txt files and converts them to readable formats.

from GameAssets.roomclass import RoomProfile

def processfile(filepath):
    # processes EVERY file, removes the newline \n from all of them
    # has to open them with encoding utf-8 because otherwise the
    # unicode art wouldn't print properly
    tempfile = open(filepath, encoding='utf-8')
    temparray = tempfile.readlines()
    tempfile.close()
    
    for var in range(0, len(temparray)):
        if "\n" in temparray[var]:
            temparray[var] = temparray[var][:-1]
    
    
    return temparray

def separatedarray(filepath):
    # just a function to split each line in a file according to the | indicator
    # and also strips it of any outlying spaces and removes empty lines
    temparray = processfile(filepath)
    
    for var in range(0, len(temparray)):
        temparray[var] = temparray[var].split("|")
        for var2 in range(0, len(temparray[var])):
            temparray[var][var2] = temparray[var][var2].strip(" ")
        
        if temparray[var][0] == '': temparray.pop(var)
        
    return temparray

def processprovidable(filepath):
    temparray = separatedarray(filepath)
    # this function processes the file above, which is either the objects or rooms
    # it turns it into a 2d table with the letter indicator at the front, makes it
    # easier to convert to a dictionary afterwards (not converting to a dictionary yet
    # because the objects.txt file shouldn't be, only rooms.txt)
    
    for nestlist in temparray:
        if len(nestlist[1]) == 1: nestlist[0], nestlist[1] = nestlist[1], nestlist[0]
    
    # this sorting algorithm is very useful bc i can then make a cohesive dictionary with ANY list!
    temparray = sorted(temparray, key=lambda ind: ind[0])
    
    tempdict = {}
    for nestlist in temparray:
        tempdict[nestlist[0]] = nestlist[1]
    
    return tempdict

def roomborders(roomindex, mapinst):
    # this function is used to return the OPPOSITE of 
    # the map_layout layout because these paths aren't
    # one-way, it edits the valid room connections to be
    # accessible both ways
    borderdict = {"N": 0, "W": 1, "E": 2, "S": 3}
    returnborder = ["", "", "", ""]
    for roominst in mapinst:
        if roominst[0] == roomindex:
            returnborder[borderdict[roominst[2]]] = roominst[1]
            
    return returnborder
    
    

def processmap(filepath, rooms, objects, pygames):
    # this is super redundant but i really want to keep it so the program's easier to read
    # if used separatedarray() for reading the map it'd look weird
    mapinstructions = separatedarray(filepath)

    # for loop for importing each room as a unique object, all of the object's properties are explained in the roomclass.py file
    for roomindex, roomname in rooms.items():
        temproom = RoomProfile()
        temproom.value = roomindex
        temproom.name = roomname
        temproom.borderingrooms = roomborders(temproom.value, mapinstructions)
        
        if temproom.value in pygames:
            temproom.pygame = pygames[temproom.value]
        #print(temproom.value, temproom.name, temproom.scent, temproom.size, temproom.game, temproom.borderingrooms)
        rooms[temproom.value] = temproom
        
        
        #print(rooms.items())
        
    # and this list... there's 100% a better solution for the following loop but i cant think of it yet
    redundantlist = [3, 2, 1, 0]
    # i was debating if i should make another function for this, but i figured it won't be needed
    # this loop assigns the current room index as a bordering room to the OPPOSITE direction to which IT
    # borders the room it's currently editing (sorry if the explanation was bad)
    for profileindex in rooms.values():
        for brindex in range(0, len(profileindex.borderingrooms)):
            if profileindex.borderingrooms[brindex] != "":
                rooms[profileindex.borderingrooms[brindex]].borderingrooms[redundantlist[brindex]] = profileindex.value
    
    
    # adds the items to the rooms, this MIGHT be redundant but i played it safe so I don't get too many errors at the last minute
    for var in range(0, len(objects)):
        if objects[var][1] in rooms:
            rooms[objects[var][1]].iteminv.append(objects[var][0])
    
    return rooms