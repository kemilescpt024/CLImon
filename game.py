import sys
import time
import os
import os.path as path, sys
from player import Player
from towns import pallet
from saving import load
from saving import save


def main():
    title = "tpkmn"
    wmesg= "Welcome", "to", title

    # for w in wmesg:
    #     print(w)
    #     time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')  # clears terminal
    
    # check for save file
    os.system('cls' if os.name == 'nt' else 'clear') 
    loadcheck = load()
    if loadcheck !=2:
        if loadcheck.current_town == "Pallet":
            pallet.begin(loadcheck)
    else:
        newPlayer = Player()
        pallet.begin(newPlayer)
main()
