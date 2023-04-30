from classes.CharacterClass import CharacterClass, NoClass


class Cleric(CharacterClass):
    def __init__(self):
        CharacterClass.__init__(self)
        self.name = 'Cleric'
        self.hit_die = 8
        self.weapon_profs = ['simple']
        self.armor_profs = ['light', 'medium', 'shield']
        self.class_profs = ['history', 'insight', 'medicine', 'persuasion', 'religion']
        self.saves['cha'] = 1
        self.saves['wis'] = 1
        self.gears = ['Mace OR Warhammer', 'Scale Mail OR Leather OR Chain Mail', 'Light Crossbow OR Simple Weapon', 'Shield', 'Holy Symbol']
        self.spellcasting_ability = 'wis'

