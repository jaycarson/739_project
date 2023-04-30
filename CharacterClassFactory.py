from classes.CharacterClass import CharacterClass, NoClass
from classes.Barbarian import Barbarian
from classes.Bard import Bard
from classes.Cleric import Cleric
from classes.Druid import Druid
from classes.Fighter import Fighter
from classes.Monk import Monk
from classes.Paladin import Paladin
from classes.Ranger import Ranger
from classes.Rogue import Rogue
from classes.Sorcerer import Sorcerer
from classes.Warlock import Warlock
from classes.Wizard import Wizard


class CharacterClassFactory(object):
    def __init__(self):
        self.Bard = Bard()
        self.Barbarian = Barbarian() 
        self.Cleric = Cleric() 
        self.Druid = Druid() 
        self.Fighter = Fighter()
        self.Monk = Monk()
        self.Paladin = Paladin()
        self.Ranger = Ranger()
        self.Rogue = Rogue()
        self.Sorcerer = Sorcerer()
        self.Warlock = Warlock()
        self.Wizard = Wizard()
        
        self.classes = {
            'Bard': self.Bard,
            'Barbarian': self.Barbarian ,
            'Cleric': self.Cleric ,
            'Druid': self.Druid ,
            'Fighter': self.Fighter,
            'Monk': self.Monk,
            'Paladin': self.Paladin,
            'Ranger': self.Ranger,
            'Rogue': self.Rogue,
            'Sorcerer': self.Sorcerer,
            'Warlock': self.Warlock,
            'Wizard': self.Wizard,
        }
        self.no_class = NoClass()

    def __call__(self, name):
        if name in self.classes:
            return self.classes[name]
        else:
            return self.no_class

    def get_classes(self):
        return self.classes.keys()
