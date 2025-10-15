import unittest
from player import *
from entries import *
class TestFunctions(unittest.TestCase):

    def test_heal(self):
        Charmander = Mon(["Fire"], "Scratch", "Metal_Sound", "Ember", None, None, 52,43,60,50,65,39, 5, exp=50)
        hp = Charmander.hp
        Charmander.set_hp(hp-5)
        Charmander.heal_full()
        self.assertEqual(Charmander.hp, hp)


    def test_heal_by(self):
        mon = Bulbasaur
        mon.set_hp(5)
        self.assertEqual(mon.hp, 5)