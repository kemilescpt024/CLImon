from entries import *
from database import *

class Player:
    def __init__(self, bag = [], badges = [], mons = [], current_town= "Pallet", flags = {"starterFlag": False}, rivalMon = Squirtle):
        endbag = ['1: Back']
        endbadges = ['1: Back']
        endmons = ['1: Back']
        for i in bag:
            endbag.append(i)
        for i in badges:
            endbadges.append(i)
        for i in mons:
            endmons.append(i)
        
        
        self.bag, self.badges, self.mons, self.current_town, self.flags ,self.rivalMon= endbag, endbadges,endmons, current_town,flags, rivalMon
    
    def new_item(self,item):
        count = 2
        item.count = count
        self.bag.append(item)
        count +=1
    
class Item:
    def __init__(self, effect, name, count = None):
        self.effect = effect
        self.name = name
        self.count = count
        

