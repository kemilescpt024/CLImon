import sys
import time
import database
import random


class Mon:
    """Initialise base Pokemon and moveset"""
    
    id = 1

    def __init__(self, type = None, m1 = None,m2 = None,m3 = None,
                m4= None, def_name = None,
                attack = 10, defense = 10, spatk = 10, 
                spdef = 10,speed = 10, hp= 10, level = 5, affliction = None,
                exp_yield=20, exp = 0, full_hp = 10, moves = [], id = None):  # 'm' for move
        if not id:
            self.id = Mon.id
            Mon.id +=1
        else:
            self.id = id

        if def_name == None:
            def_name = database.Dex[self.id]
        self.name = def_name
        attack = random.choice(range(attack - 7,attack)) *8
        defense = random.choice(range(defense-7, defense)) *8
        spatk = random.choice(range(spatk-4, spatk))*8
        spdef = random.choice(range(spdef-6, spdef))*8
        speed = random.choice(range(speed-4, speed))*8
        base_stats = [attack,defense,spatk,spdef,speed]
        stats = []
        for s in base_stats:
            current = int((0.01*(2*s+(4)*level)+5))
            stats.append(current)
        self.attack = stats[0]
        self.defense = stats[1]
        self.spatk = stats[2]
        self.spdef = stats[3]
        self.speed = stats[4]

        hp = random.choice(range(hp-4, hp))
        self.hp = int((0.01 * (2* hp + (4)*level)) + level+10)
        self.full_hp = self.hp
        self.level, self.name, self.type = level , def_name, type
        self.m1 ,self.m2, self.m3, self.m4 = m1 , m2, m3 ,m4  # moveset assignments
        self.moves= m1,m2,m3,m4
        self.affliction = affliction
        self.exp_yield = exp_yield
        self.exp = exp

    def level_up(self):
        self.attack, self.defense = int(self.attack * 1.03), int(self.defense* 1.03)
        self.spatk, self.spdef = int(self.spatk * 1.03), int(self.spdef * 1.04)
        self.speed, self.full_hp = int(self.speed * 1.04), int(self.full_hp * 1.04)
        self.level = self.level + 1
        print(f"{self.name} has levelled up to level {self.level}!")
        print(f"Attack increased to {self.attack}, Defense increased to {self.defense},\n"
              f"Sp. Attack increased to {self.spatk}, Sp Defense increased to {self.spdef},\n"
              f"Speed increased to {self.speed}, HP increased to {self.full_hp}!")
    
    def exp_gain(self, opp):
        exp_form = ((opp.exp_yield * opp.level)/ 7) * (1/8) * 1 *1 
        exp_form = int(exp_form)
        print(f"{exp_form} EXP gained!")
        self.exp += exp_form
        required = self.level * 30 + (5* self.level)
        print(f"Total EXP is {self.exp}. Required to level: {required}")
        if self.exp >= required:
            self.level_up()
    
    def updateMoveList(self):
        self.moves = self.m1,self.m2,self.m3,self.m4
    
    def set_hp(self, hp):
        self.hp = hp
    
    def heal_full(self):
        self.hp = self.full_hp
    
    def heal(self, amount):
        self.hp = self.hp + amount
        if self.hp> self.full_hp:
            self.hp = self.full_hp

class LoadedMons():
    def __init__(self, type=None, m1=None, m2=None, m3=None, m4=None, def_name=None,
                 attack=10, defense=10, spatk=10, spdef=10, speed=10, hp=10, 
                 level=5, affliction=None, exp_yield=20, exp=0, full_hp=10, moves=[], id = None):
        # super().__init__(type, m1, m2, m3, m4, def_name, attack, defense, spatk, spdef, speed, hp, level, affliction, exp_yield, exp, full_hp, moves)
        self.id = id
        self.name = def_name
        self.attack = attack
        self.defense = defense
        self.spatk = spatk
        self.spdef = spdef
        self.speed = speed
        self.hp = hp
        self.full_hp = full_hp
        self.level, self.name, self.type = level , def_name, type
        self.m1 ,self.m2, self.m3, self.m4 = m1 , m2, m3 ,m4  # moveset assignments
        self.moves= m1,m2,m3,m4
        self.affliction = affliction
        self.exp_yield = exp_yield
        self.exp = exp

    def exp_gain(self, opp):
        exp_form = ((opp.exp_yield * opp.level)/ 7) * (1/8) * 1 *1 
        exp_form = int(exp_form)
        print(f"{exp_form} EXP gained!")
        self.exp += exp_form
        required = self.level * 30 + (5* self.level)
        print(f"Total EXP is {self.exp}. Required to level: {required}")
        time.sleep(1)
        input(">")
        for i in range(10):
            if self.exp >= required:
                self.level_up()
    
    def level_up(self):
        self.attack, self.defense = int(self.attack * 1.03), int(self.defense* 1.03)
        self.spatk, self.spdef = int(self.spatk * 1.03), int(self.spdef * 1.04)
        self.speed, self.full_hp = int(self.speed * 1.04), int(self.full_hp * 1.04)
        self.level = self.level + 1
        print(f"{self.name} has levelled up to level {self.level}!")
        print(f"Attack increased to {self.attack}, Defense increased to {self.defense},\n"
              f"Sp. Attack increased to {self.spatk}, Sp Defense increased to {self.spdef},\n"
              f"Speed increased to {self.speed}, HP increased to {self.full_hp}!")
        time.sleep(2)
        input(">")

    def set_hp(self, hp):
        self.hp = hp

    def heal_full(self):
        self.hp = self.full_hp

    def heal(self, amount):
        self.hp = self.hp + amount
        if self.hp> self.full_hp:
            self.hp = self.full_hp

def move_set(Mon):
    """define initial moveset and format for ease of access
    return in neat format to select attacks"""

    moves = f"{Mon.m1} {Mon.m2} {Mon.m3} {Mon.m4}"
    moves = moves.replace("None", "--")
    moves = moves.split(" ", 4)
    layout = ""
    for mcount, i in enumerate(moves):
        mcount +=1
        if i != "--":
            layout += f"{mcount}: {i} "
    layout = layout.replace("_", " ")
    return layout

        

Bulbasaur = Mon(["Grass"], "Vine-whip", "Tackle", None, None, None, 49,49,65,65,45,45, 5,exp=50, exp_yield=64)
Ivysaur = Mon(["Grass"], "Vine-whip", "Metal_Sound", None, None, None, 62,63,80,80,60,60)
Venasaur = Mon(["Grass"], "Vine-whip", "Metal_Sound", None, None, None, 82,83,100,100,80,80, exp_yield=263)
Charmander = Mon(["Fire"], "Scratch", "Metal_Sound", "Ember", None, None, 52,43,60,50,65,39, 5, exp=50)
Charmeleon = Mon(["Fire"], "Tackle", "Leer", "Ember", "Metal_Claw")
Charizard = Mon(["Fire","Flying"], "Wing_Attack", "Ember", "Scratch", "Flamethrower", None, 84,78,109,85,100,78)
Squirtle = Mon(["Water"], "Tackle", "Leer", "Water_Gun" ,None, None, 48,65,50,64,43,44,5, exp=50)

# print(Charmander.__dict__)
# print(Charmeleon.name)
# print(move_set(Charmeleon))
# print(Charmeleon)