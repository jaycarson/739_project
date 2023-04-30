from classes.CharacterClass import CharacterClass, NoClass


class Wizard(CharacterClass):
    def __init__(self):
        CharacterClass.__init__(self)
        self.name = 'Wizard'
        self.hit_die = 6
        self.weapon_profs = ['dagger', 'dart', 'sling', 'quarterstaff', 'light crossbow']
        self.armor_profs = []
        self.class_profs = ['arcana', 'history', 'insight', 'investigation', 'medicine', 'religion']
        self.saves['wis'] = 1
        self.saves['int'] = 1
        self.gears = ['Quarterstaff OR Dagger', 'Component Pouch or Arcane Focus', 'Scholar Pack OR Explorer Pack', 'Spellbook']
        self.spellcasting_ability = 'int'
