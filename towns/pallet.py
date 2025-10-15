from pathlib import Path
from towns import *
import sys
import os

# adds parent folder, so you can import from it

from inspect import getsourcefile
import os.path as path, sys
from towns import *

from battle import *
from player import *
from towns.towns import PokeCenter, Town

pallet = Town(name = 'Pallet Town')
palletPC = PokeCenter(name = "Pallet PokeCenter")
pallet.buildings.append(palletPC)


def pc(player):
    for op in palletPC.options:
        print(op)
    
    choice = int(input("Select option: "))
    if choice == 2:  # commence healing
        palletPC.heal(player)   
    if choice == 1:
        return
    


def begin(player):
    sflag = player.flags.get("starterFlag")
    while sflag == False:
        print("Welcome, please choose a starting Pokemon: ")
        sChoice = int(input("1. Bulbasaur  2. Squirtle   3. Charmander\n"))
        if sChoice == 1:
            player.mons.append(Bulbasaur)
            oppMon =  Mon(["Fire"], "Scratch", "Metal_Sound", None, None, "Charmander", 52,43,60,50,65,39, 5, exp=50, exp_yield=1500, id = 7)
        elif sChoice ==2:
            player.mons.append(Squirtle)
            oppMon = Mon(["Grass"], "Tackle",None, None, None, "Bulbasaur", 49,49,65,65,45,45, 5,exp=50, exp_yield=1500, id=1)
        elif sChoice == 3:
            player.mons.append(Charmander)
            oppMon = Mon(["Water"], "Tackle", "Leer", None ,None, "Squirtle", 48,65,50,64,43,44,5, exp=50, exp_yield=1500, id=4)
        # elif sChoice ==4:
        #     Red.mons.append(Pikachu)
        
        else:
            print("Invalid choice. Select 1,2, or 3.")
        
        player.rivalMon = oppMon
        player.flags["starterFlag"] = True
        sflag = player.flags.get("starterFlag")

    mon = player.mons[1]
    oppMon = player.rivalMon
    town = {"TownName":"Pallet"}
    if not player.flags.get("beat_rival1"):
        print(f"Congratulations, you've received a {mon.name}")
        print("Test out your skills as a trainer!")
        
        play(player, mon, oppMon, town)
    player.flags["beat_rival1"] = True
    play(player, mon, Squirtle,town)
    print("Where to next...")






