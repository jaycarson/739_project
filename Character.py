from CharacterBackgroundFactory import CharacterBackgroundFactory
from CharacterClassFactory import CharacterClassFactory
from CharacterRaceFactory import CharacterRaceFactory
from CharacterSheet import CharacterSheet
from Armors import Armors
from Weapons import Weapons


class Character(object):
    def __init__(self):
        self.name = ''
        self.proficiency = 0
        self.darkvision = 0
        self.max_hp = 0
        self.level = 1
        self.proficiency = 2

        self.stats = {'str': 8, 'dex': 8, 'con': 8, 'int': 8, 'wis': 8, 'cha': 8}
        self.stats_final = {'str': 8, 'dex': 8, 'con': 8, 'int': 8, 'wis': 8, 'cha': 8}

        self.stats_final = {}
        
        self.character_sheet = CharacterSheet()

        self.character_class_factory = CharacterClassFactory()
        self.character_race_factory = CharacterRaceFactory()
        self.character_background_factory = CharacterBackgroundFactory()
   
        self.character_class = self.character_class_factory('NoClass')
        self.character_race = self.character_race_factory('NoRace')
        self.character_background = self.character_background_factory('NoBG')

        self.races = self.character_race_factory.get_races()
        self.classes = self.character_class_factory.get_classes()
        self.backgrounds = self.character_background_factory.get_backgrounds()

        self.weapon_rack = Weapons()
        self.armor_rack = Armors()

        self.gears = []
        self.weapons = []
        self.armors = []
        self.shields = []

    def __call__(self):
        for stat in self.stats:
            self.stats_final[stat] = self.stats[stat] + self.character_race[stat]
        self.darkvision = max(self.character_race.darkvision, self.character_class.darkvision)

    def add_gear(self, item):
        if self.weapon_rack.is_weapon(item):
            self.weapons.append(self.weapon_rack.get(item))
        elif self.armor_rack.is_armor(item):
            self.armors.append(self.armor_rack.get(item))
        else:
            self.gears.append(item)

    def adjust_stat(self, stat, amount):
        value = self.stats[stat]
        value_new = value + amount

        if value_new > 16 or value_new < 8:
            return

        cost_diff = self.costs[value_new] - self.costs[value]

        if self.points_current + cost_diff <= self.points_max:
            self.stats[stat] = value_new

    def change_background(self, name):
        self.character_background = self.character_background_factory(name)
        self.character_background.owner = self

    def change_class(self, name):
        self.character_class = self.character_class_factory(name)
        self.character_class.owner = self

    def change_race(self, name):
        self.character_race = self.character_race_factory(name)
        self.character_race.owner = self

    def get_mod(self, stat):
        return (self.get_stat(stat) - 10) // 2

    def get_save(self, stat):
        save = (self.get_stat(stat) - 10) // 2
        save_class = self.character_class.saves[stat] * self.proficiency
        save_race = self.character_race.saves[stat] * self.proficiency
        return save + save_class + save_race

    def get_spellcasting_dc(self):
        mod = self.get_mod(self.character_class.spellcasting_ability)
        return mod + self.proficiency + 8

    def get_stat(self, name):
        if name not in self.stats:
            return 0
        stat = self.stats[name]
        stat += self.character_race.stats[name]
        stat += self.character_class.stats[name]
        return stat

    def update_max_hp(self):    
        self.max_hp = self.character_class.hit_die + (int((self.get_stat('con') - 10) / 2) * self.level)

    def print_sheet(self):
        self.character_sheet(self)
