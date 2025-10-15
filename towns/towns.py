# adds parent folder, so you can import from it

from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])

# from battle import *
from player import *


class Town:
    def __init__(self, buildings =[], grass=[], water=[], name = ""):
        self.name = name
        buildings = []
        grass = []  # to establish wild pokemon
        water =[]
        self.buildings, self.grass,self.water = buildings, grass,water

class Building:
    def __init__(self, options = [], name = ""):
        options.append("1. Exit")
        self.options = options
        self.name = name

    
class PokeCenter(Building):
    def __init__(self, options = [], name = ""):
        super().__init__(options, name)
        self.options.append("2. Heal")
        
    def heal(self, player):
        for i in player.mons:
            try:
                i.hp = i.full_hp
            except:
                continue
        print("Party healed.")



