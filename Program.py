import random
import math
import os


##Define Modes##
gamemodes = ["Competative", "Unrated", "Swift Play", "Spike Rush"]



def programrun():
    ## Shuffle List #
    random.shuffle(gamemodes)

    ## If Comp Mode ##
    if(gamemodes[0] == "Competative"):
        length = len(gamemodes[1])  
        if (length < len(gamemodes[0])):
            length = len(gamemodes[0]) 
            sublen = 11 - len(gamemodes[1])
            slb = sublen / 2
            slbfloor = math.floor(slb)
            slbvalue  = math.ceil(slb)

    ## If any other mode ##
    else:
        length = len(gamemodes[0]) 


    ##Print Top Row##
    print(" ┏━", end="")
    for i in range (length) :
        print("━", end='') # change end from '\n' (newline) to a space
    print("━┓")

    ##Print Mode Row##
    print(" ┃ "+gamemodes[0]+" ┃")

    ##Print Alt Comp Row##
    if (gamemodes[0] == "Competative"):
        print(" ┃", end=' ')
        for i in range (slbfloor) :
            print(" ", end='') # change end from '\n' (newline) to a space
        print(gamemodes[1], end='')
        for i in range (slbvalue) :
            print(" ", end='') # change end from '\n' (newline) to a space
        print(" ┃")

    ##Print Final Row##
    print(" ┗━", end="")
    for i in range (length) :
        print("━", end='') # change end from '\n' (newline) to a space
    print("━┛")


    os.system ('pause')
    programrun()

##
def Loop():
    r = input("Enter Y or yes to rerun")
    if r == "yes" or r == "y":
        programrun()
        Loop()

programrun()

1>2# : ^
'''
@echo off
echo normal 
echo batch code
echo Switch to python
python "%~f0"
exit /b
rem ^
'''
print ("This is Python code")
