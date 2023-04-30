from classes.CharacterClass import CharacterClass, NoClass


class Sorcerer(CharacterClass):
    def __init__(self):
        CharacterClass.__init__(self)
        self.name = 'Sorcerer'
        self.hit_die = 6
        self.weapon_profs = ['dagger', 'dart', 'sling', 'quarterstaff', 'light crossbow']
        self.armor_profs = []
        self.class_profs = ['arcana', 'deception', 'insight', 'intimidation', 'persuasion', 'religion']
        self.saves['cha'] = 1
        self.saves['con'] = 1
        self.gears = ['Light Crossbow OR Simple Weapon', 'Component Pouch OR Arcane Focus', 'Dungeoneer Pack OR Explorer Pack', 'Dagger', 'Dagger']
        self.spellcasting_ability = 'cha'
