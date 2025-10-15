import json
import io
from player import *
from entries import *
from pathlib import Path
import time, os


# class Object:
#     def toJSON(self):
#         return json.dumps(
#             self,
#             default=lambda o: o.__dict__, 
#             sort_keys=True,
#             indent=4)
class Loaditem:
    def __init__(self, effect, name, count = None):
        self.effect = effect
        self.name = name
        self.count = count
        
    
def save(player, town):
    """Saves game to json file, by converting all data to json object"""
    print("Saving...")
    curr_badges = [badge.__dict__ for badge in player.badges if badge != '1: Back']
    save_data = {
        "player":{
            # "name": player.name,
            "current_town": player.current_town,
            "flags": player.flags,
            "badges": curr_badges
        },
        "bag":[item.__dict__ for item in player.bag if item != '1: Back'],
        "party":[mon.__dict__ for mon in player.mons if mon != '1: Back'],
        "rivalMon": player.rivalMon.__dict__ if player.rivalMon else None
    }
    # t = Object.toJSON(town)
    with io.open("Save_001.json", "w") as file:  # saving database as file
        #     json.dump(team, file, ensure_ascii=False)
            str_ = json.dumps(save_data,
                        indent=4, sort_keys=True,
                        ensure_ascii=True)
            file.write(str_) 
            # str2_ = json.dumps(t,indent=4, sort_keys=True, ensure_ascii=True)
            # file.write(str2_)
    time.sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear') 


def load():
    """load the game and convert json file back to respective objects"""
    
    my_file = Path("Save_001.json")
    if my_file.is_file():
        # file exists
        select = int(input("1. Continue game\n2. New game\n"))
        if select == 2:
            os.system('cls' if os.name == 'nt' else 'clear') 
            return select
        with open("Save_001.json", "r") as sf:
            rsf = json.load(sf)
            monsters = []
            for mon in rsf["party"]:
                if "1: Back" in mon:
                    continue
                m = LoadedMons(affliction=mon['affliction'], attack= mon['attack'], defense=mon['defense'],
                            exp= mon['exp'], exp_yield=mon['exp_yield'], full_hp=mon['full_hp'], hp=mon['hp'],
                            id = mon['id'], level=mon['level'], m1=mon['m1'], m2 = mon['m2'], m3= mon['m3'], 
                            m4= mon['m4'], moves=mon['moves'], def_name=mon['name'], spatk=mon['spatk'],
                            spdef=mon['spdef'], speed=mon['speed'],type=mon['type'])
                monsters.append(m)
                
            items =[]
            for item in rsf["bag"]:
                if "1: Back" in item:
                    continue
                it = Loaditem(effect=item['effect'], name=item['name'], count=item['count'])
                items.append(it)
            
            badges = []
            for badge in rsf["player"].get("badges", []):
                if "1: Back" in badges:
                    continue
                badges.append(badge)
            cuTown = rsf["player"].get("current_town")
            flagsLoad = rsf["player"].get("flags", {})
            rivaldat = rsf.get("rivalMon")
            rivalm = LoadedMons(affliction=rivaldat['affliction'], attack= rivaldat['attack'], defense=rivaldat['defense'],
                            exp= rivaldat['exp'], exp_yield=rivaldat['exp_yield'], full_hp=rivaldat['full_hp'], hp=rivaldat['hp'],
                            id = rivaldat['id'], level=rivaldat['level'], m1=rivaldat['m1'], m2 = rivaldat['m2'], m3= rivaldat['m3'], 
                            m4= rivaldat['m4'], moves=rivaldat['moves'], def_name=rivaldat['name'], spatk=rivaldat['spatk'],
                            spdef=rivaldat['spdef'], speed=rivaldat['speed'],type=rivaldat['type'])
            
            plyer = Player(items,mons = monsters, badges = badges, current_town=cuTown, flags=flagsLoad, rivalMon=rivalm)
            os.system('cls' if os.name == 'nt' else 'clear') 

            return plyer
    else:
        choice = input("1: New Game\n")
        try:
            choice = int(choice)
            if choice != 1:
                load()
            return 2
        except:
            print("Invalid selction")
            load()
