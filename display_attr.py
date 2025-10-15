from database import *

def display_mons(player):
    """display mon data"""
    count = 1
    for i in player.mons:
        if i != "1: Back":
            print(f"{count}: {i.name}       {i.hp}/{i.full_hp}")
            count +=1
        else:
            print(i)
            count +=1
            
def dis_mon_stats(mon,player):
    
    print(mon.name+ "\n")
    print(f"HP: {mon.hp}/{mon.full_hp}")
    mstats = vars(mon)
    # stats to not print
    skips = ['id', 'name', 'hp', 'full_hp', 'exp_yield','moves',
             'm1', 'm2', 'm3', 'm4']


    for i in mstats:
        i = str(i)
        moves = skips[-4:]
        if i in moves:
            mv = mstats[i]
            if mv == None:
                continue
            atk = Attacks[mv]
            mv = mv.replace("_", " ")
            print(mv, atk.type, atk.pp)
            continue
        if i in skips:
            continue
        
        print(i.upper() ,":", mstats[i])
    choice = input("1: Back     2: Switch out\n")
    choice = int(choice)
    if choice == 1:
        display_mons(player)
    if choice == 2:
        return choice
    

def display_bag(player):
    """display bag contents"""
    for i in player.bag:
            if i != "1: Back":
                print(f"{i.count}: {i.name}")
            else:
                print(i)
