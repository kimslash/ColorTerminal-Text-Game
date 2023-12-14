# Kim K.
# CSC110
# 12/13/2023
# screen renderer (CSC110 Term Project)
# This program renders either pre-made graphics, or custom graphics that require a table of strings.

from colorama import Fore, Back, Style

# i couldn't think of a different place to include these, so i just sorta declared them global right here
line = "----------------------------------------------------------------------------------------------------"
grnd = "████████████████████████████████████████████████████████████████████████████████████████████████████"
brpt = "═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩"
brp2 = "═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦"



def roomrender(roomobj, score=0 ):
    # looking at this, you may be a little astonished by how redundant it is, but it's definitely
    # a simple way to incorporate a scene into the game, I initially was gonna have a sky and grass floor,
    # but then i realized they're called rooms for a reason
    print(f"""{Back.WHITE}{Fore.BLACK}{f"Welcome to Room {roomobj.value}: {roomobj.name}!":^100}{Style.RESET_ALL}
{roomobj.skycolor}{roomobj.objcolor}{brpt:^100}\n{brp2:^100}\n{brpt:^100}\n{brp2:^100}\n{brpt:^100}\n{brp2:^100}
{f"═╦═╩═╦═╩═╦═╩{roomobj.spriteline[0][0]}   {roomobj.spriteline[1][0]}   {roomobj.spriteline[2][0]}   {roomobj.spriteline[3][0]}   {roomobj.spriteline[4][0]}   {roomobj.spriteline[5][0]}╩═╦═╩═╦═╩═╦═╩":^100}
{f"═╩═╦═╩═╦═╩═╦{roomobj.spriteline[0][1]}   {roomobj.spriteline[1][1]}   {roomobj.spriteline[2][1]}   {roomobj.spriteline[3][1]}   {roomobj.spriteline[4][1]}   {roomobj.spriteline[5][1]}╦═╩═╦═╩═╦═╩═╦":^100}
{f"═╦═╩═╦═╩═╦═╩{roomobj.spriteline[0][2]}   {roomobj.spriteline[1][2]}   {roomobj.spriteline[2][2]}   {roomobj.spriteline[3][2]}   {roomobj.spriteline[4][2]}   {roomobj.spriteline[5][2]}╩═╦═╩═╦═╩═╦═╩":^100}
{f"═╩═╦═╩═╦═╩═╦{roomobj.spriteline[0][3]}   {roomobj.spriteline[1][3]}   {roomobj.spriteline[2][3]}   {roomobj.spriteline[3][3]}   {roomobj.spriteline[4][3]}   {roomobj.spriteline[5][3]}╦═╩═╦═╩═╦═╩═╦":^100}
{f"═╦═╩═╦═╩═╦═╩{roomobj.spriteline[0][4]}   {roomobj.spriteline[1][4]}   {roomobj.spriteline[2][4]}   {roomobj.spriteline[3][4]}   {roomobj.spriteline[4][4]}   {roomobj.spriteline[5][4]}╩═╦═╩═╦═╩═╦═╩":^100}
{f"═╩═╦═╩═╦═╩═╦{roomobj.spriteline[0][5]}   {roomobj.spriteline[1][5]}   {roomobj.spriteline[2][5]}   {roomobj.spriteline[3][5]}   {roomobj.spriteline[4][5]}   {roomobj.spriteline[5][5]}╦═╩═╦═╩═╦═╩═╦":^100}
{f"═╦═╩═╦═╩═╦═╩{roomobj.spriteline[0][6]}   {roomobj.spriteline[1][6]}   {roomobj.spriteline[2][6]}   {roomobj.spriteline[3][6]}   {roomobj.spriteline[4][6]}   {roomobj.spriteline[5][6]}╩═╦═╩═╦═╩═╦═╩":^100}
{Style.RESET_ALL}{roomobj.skycolor}{roomobj.groundcolor}{grnd:^100}\n{grnd:^100}\n{grnd:^100}
{Style.RESET_ALL}{roomobj.textcolor}{line:^100}
{f"{Fore.LIGHTBLACK_EX}       Your awesome player score that's totally being kept track of: {Fore.WHITE}{score}{Fore.LIGHTBLACK_EX}!!!{roomobj.textcolor}     ":^100}
{f"     Navigation: “Move (Direction)”                        Menu Commands:                           ":^100}
{f"               NORTH                                       - “Game”             - “My Score”        ":^100}
{f"          WEST   +    EAST                                 - “Check Size”       - “Inventory”       ":^100}
{f"               SOUTH                                       - “Check Scent”      - “Open Map”        ":^100}
{line:^100}{Style.RESET_ALL}""")


      
def rendercustom(forec, backc, sprite1, text):
        
    # render custom sprite
    # the sprite is printed layer by layer
    for var in range(0, len(sprite1)):
        print(f"{backc}{forec}{sprite1[var]:^100}{Style.RESET_ALL}",end=" \n")
    
    # prints a separator
    print(f"{backc}{forec}{line:^100}{Style.RESET_ALL}",end=" \n")
    
    # prints string table
    # printed just like the sprite, hence why the table was required over a multiline string
    for var in range(0, len(text)):
        print(f"{backc}{forec}{text[var]:^100}{Style.RESET_ALL}",end=" \n")