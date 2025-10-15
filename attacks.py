from entries import *
from database import *
from damage_step import *
import random
from type_chart import *

def atk_process(atk_mon, def_mon, attack):
    """x0.5 if ineffective, 1 if effective, x2 super effective"""
    
    
    if attack.special == "Special Stat":
        StatChanger.use(attack,atk_mon,def_mon)
        return None
    
    # critical hit chance

    draw_crit = random.choice(range(19))
    if draw_crit == 10:
        crit = 2
        print("Critical hit!")
    else:
        crit = 1
    

    # base attack damage
    if attack.special == "Special":
        form = ((((3* atk_mon.level* crit)/5)+2)* attack.power * (atk_mon.spatk/def_mon.spdef))/50
    
    if attack.special == "Physical":
        form = ((((3* atk_mon.level* crit)/5)+2)* attack.power * (atk_mon.attack/def_mon.defense))/50


    # boost if same type using type move
    if attack.type in atk_mon.type:
        form = form * 1.5

    
    for i in def_mon.type:
        if i in types[attack.type]["Strengths"]:
            form = form * 2
            print("It's super effective!")
        elif i in types[attack.type]["Ineffective"]:
            form = form * 0.5
            print("Not very effective!")
        elif attack.type in types[i]["Immunities"]:
            print("Doesn't have an effect!")
            return
    
    # randomise damage a bit
    form = form * random.choice(range(217,255)) / 255
    if form < 1: form = 1
    form = int(form)
    print("Damage is ", form)
    damage(atk_mon,def_mon,form)
    
    # additional ailment
    try:
        if attack.ailment == "Burn":
            StatChanger.use(attack,atk_mon,def_mon)
    except:
        return None

class Attack:
    at_id = 0
    def __init__(self, type, special, power, accuracy, pp):
        self.id = Attack.at_id
        Attack.at_id +=1
        self.type = type
        self.special = special
        self.power = power
        self.accuracy = accuracy
        self.pp = pp

class StatChanger(Attack):
    """
    define changes in defense, attack or any lingering ailment an attack may cause
    """
    sp_d_count = 0
    d_count = 0
    sp_a_count = 0
    speed_count = 0
    a_count = 0
        
    def __init__(self, d_change=0, a_change=0, sp_d_change =0, sp_a_change =0, speed_change = 0, ailment = None,
                 type = None, special = None, power = None, accuracy = None,pp = None):
        
        super().__init__(type,special,power,accuracy,pp)
        self.d_change = d_change
        self.a_change = a_change
        self.sp_d_change = sp_d_change
        self.sp_a_change = sp_a_change
        self.speed_change = speed_change
        self.ailment = ailment

        # counter assignments
        self.sp_d_count ,self.d_count= StatChanger.sp_d_count, StatChanger.d_count
        self.sp_a_count , self.a_count= StatChanger.sp_a_count, StatChanger.a_count
        self.speed_count = StatChanger.speed_count
        
    
    def use(self, atk_mon, opp):
        # counts for limits to stat lowering
        
        if self.ailment == "Burn":
            roll = random.choice(range(5))
            if roll == 4:
                opp.affliction = "Burn"
                print(f"{opp.name} was Burned!")
        if self.d_change > 0:
            atk_mon.defense += self.d_change
        if self.d_change < 0:
            if self.d_count >2:
                print("Can't lower defense anymore.")
            opp.defense += random.choice(range(self.d_change -2, self.d_change +2))
            print(f"Lowered {opp.name}'s defense.")
            self.d_count +=1
            if opp.defense <1:
                opp.defesnse = 1
        if self.sp_d_change < 0:
            if self.sp_d_count >2:
                print("Can't lower special defense anymore.")
                return None
            opp.spdef += random.choice(range(self.sp_d_change -2, self.sp_d_change +2))
            print(f"Lowered {opp.name}'s special defense.")
            self.sp_d_count +=1
            if opp.spdef <1:
                opp.spdef = 1
            damage(atk_mon, opp,0)



Vine_whip = Attack("Grass", "Physical", 45 , 100, 15)
Ember = StatChanger(type="Fire", special="Special", power=40, accuracy=100, pp=25, ailment= "Burn")
Leer = StatChanger(d_change= -3,type="Normal", special="Special Stat", accuracy=100,pp=25)  # id 2
Metal_sound = StatChanger(type="Steel", special="Special Stat", sp_d_change= -4, accuracy=100, pp=15)
Scratch = Attack(type="Normal", special="Physical", power= 40, accuracy=100, pp= 25)
Tackle = Attack(type="Normal", special="Physical", power= 40, accuracy=100, pp= 25)
Flamethrower = StatChanger(type="Fire", special="Special", power = 90, accuracy=100, pp= 15, ailment="Burn")
Wing_attack = Attack(type = "Flying", special="Physical", power=60, accuracy=100, pp = 35)
Water_gun = Attack(type="Water", special="Special", accuracy=100, power=40, pp=25)