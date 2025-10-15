from database import *
from entries import *

def damage(attacking, defending, form):
    defending.hp = int(defending.hp - form)
    if defending.hp <0:
        defending.hp = 0
    # Affliction checks
    if defending.affliction == "Burn":
        defending.hp = defending.hp - (defending.hp * 0.125)
        print(f"{defending.name} was hurt by burn.")
     
def hp_check(attacking, defending):
    if int(defending.hp) < 1:
        print(f"{defending.name} has feinted!")
        attacking.exp_gain(defending)
        
    elif defending.hp < 20:
        print(f"{defending.name} is low on HP!")