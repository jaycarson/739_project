from classes.CharacterClass import CharacterClass, NoClass


class Warlock(CharacterClass):
    def __init__(self):
        CharacterClass.__init__(self)
        self.name = 'Warlock'
        self.hit_die = 8
        self.weapon_profs = ['simple']
        self.armor_profs = ['light']
        self.class_profs = ['arcana', 'deception', 'history', 'intimidation', 'investigation', 'nature', 'religion']
        self.saves['wis'] = 1
        self.saves['cha'] = 1
        self.gears = ['Light Crossbow OR Simple Weapon', 'Component Pouch OR Arcane Focus', 'Scholar Pack OR Dugneoneer Pack', 'Leather Armor', 'Simple Weapon', 'Dagger', 'Dagger']
