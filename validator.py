# Kim K.
# CSC110
# 12/13/2023
# input validator (CSC110 Term Project)
# This program just validates inputs from different programs

from colorama import Fore
from colorama import Style


def validchoice(textprompt, promptcolor, choices):
    # just a simple valid choice checker
    # if a match in the table is found, it returns its index + 1 (so it doesn't start at 0)
    inpstring = validempty(textprompt, promptcolor)
    
    for var in range(0, len(choices)):
        if inpstring.upper() == choices[var].upper():
            return var + 1
        
    print(f"\n{Fore.RED}Your input doesn't correspond to your available options.{Style.RESET_ALL}\n")
    return validchoice(textprompt, promptcolor, choices)


def validempty(textprompt, promptcolor):
    # simple empty string checker
    inpstring = input(f"{promptcolor}{textprompt}")
    print(Style.RESET_ALL, end="")
    if inpstring == "": print(f"\n{Fore.RED}Please make sure your input isn't empty.{Style.RESET_ALL}\n"); return validempty(textprompt, promptcolor)
    
    return inpstring