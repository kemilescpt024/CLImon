from entries import *
from attacks import *
from database import *
from player import *
from battleViewer import *
import random
from damage_step import *
import time
import imageData
import os
import sys
from display_attr import *
from saving import *
# import msvcrt
import select
import termios
import tty

def clear_input_buffer():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(sys.stdin)
    try:
        tty.setcbreak(sys.stdin.fileno())
        while select.select([sys.stdin], [], [], 0)[0]:
            sys.stdin.read(1)
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)



def display_HUD(Mon, opp):
    
    
    # HP and opp display
    opp.hp = int(opp.hp)
    print(f"\n          {opp.name}\nHP: {opp.hp}")
    hp_print_op = int(opp.hp)
    if hp_print_op > 200:  # to limit amount of = printed
        hp_print_op = 200
    print("=" * hp_print_op)

    
    
    # HP and own display
    Mon.hp = int(Mon.hp)
    print(f"\n\n{Mon.name}      lvl: {Mon.level} \nHP: {Mon.hp}")
    hp_print_own = int(Mon.hp)
    if hp_print_own > 200:  # limit = printed
        hp_print_own = 200
    print("=" * hp_print_own)
    print("\n\n" , move_set(Mon))

    

    
    

def select_attack(Mon, opp):
    display_HUD(Mon, opp)
    time.sleep(0.5)
    try:
        clear_input_buffer
        choice = int(input("\nChoose attack: "))
        if choice >4 or choice <1:
            print("Invalid choice!")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear') 
            select_attack(Mon, opp)
        choice -=1
    except:
        print("Invalid choice!")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear') 
        select_attack(Mon, opp)
    if Mon.moves[choice] != None:
        aname = Mon.moves[choice].replace("_", " ")
        print(f"{Mon.name} used {aname}!")
        time.sleep(0.8)
        a = Mon.moves[choice]
        a = Attacks[a]  # pointer to dict values
        
        atk_process(Mon,opp,a)
        time.sleep(0.8)
        if opp.hp == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            time.sleep(0.5)
            print(f"{opp.name} feinted!")
        else:
            time.sleep(1.2)
            os.system('cls' if os.name == 'nt' else 'clear') 
            display_HUD(Mon, opp)
            hp_check(Mon,opp)

        time.sleep(0.8)
       

    else:
        print("Invalid move!")
        os.system('cls' if os.name == 'nt' else 'clear') 
        select_attack(Mon, opp)
    
    
        

def opponent(Mon, opp):
    atks = []
    for i in Mon.moves:
        if i != None:
            atks.append(i)
    lenatk = len(atks)
    pick = random.choice(range(lenatk))
    atk = Mon.moves[pick]
    atk = Attacks[atk]
    print(f"Opponent's {Mon.name} used {Mon.moves[pick].replace("_", " ")}")
    time.sleep(0.6)
    atk_process(Mon, opp, atk)
    hp_check(Mon, opp)
    

def play(player, one, two, town):
    #pics

    display_battle_images(one, two)
    options = '1: Attack  2: Items 3: Monsters  4: Save'
    clear_input_buffer
    action = input(f"{options} \nSelect an action.\n")
    os.system('cls' if os.name == 'nt' else 'clear') 

    # process for accessing inventory
    if action == "2":
        display_bag(player)
        action = input("\n")
        if action == "1":
            play(player, one,two,town)
        else:
            action = int(action)
            action -=1
            item = player.bag[action]
            item.effect(one)
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            play(player, one, two,town)
            
    if action == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        display_mons(player)
        action = input("\n")
        if action == "1":
            play(player, one,two,town)
        else:
            action = int(action)
            action -=1
            os.system('cls' if os.name == 'nt' else 'clear')
            monster = player.mons[action]
            new_mon = dis_mon_stats(monster, player)
            if new_mon ==2:
                play(player, monster,two,town)
            else:
                play(player, one,two,town)
    if action == '4':
        # saving functionality
        save(player, town)
        play(player,one,two, town)
    while one.hp > 0 and two.hp > 0:
        select_attack(one,two)
        
        time.sleep(0.5)
        if two.hp > 0:
            opponent(two, one)
        time.sleep(0.7)
        os.system('cls' if os.name == 'nt' else 'clear') 
        
        
def process(): 
    # check for save file
    os.system('cls' if os.name == 'nt' else 'clear') 
    loadcheck = load()
    if loadcheck == 2:
        # one = Charizard
        # three = Charmander
        # two = Bulbasaur
        # Red = Player()
        # Red.mons.append(one)
        # Red.mons.append(three)
        # Rare_Candy = Item(Mon.level_up, "Rare Candy")
        # Red.new_item(Rare_Candy)
        # play(Red, one,two)
        return Red
    
    two = Bulbasaur
    play(loadcheck, loadcheck.mons[1], two)

    # two = Venasaur
    # play(Red, one, two)
# process()