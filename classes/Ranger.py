from classes.CharacterClass import CharacterClass, NoClass


class Ranger(CharacterClass):
    def __init__(self):
        CharacterClass.__init__(self)
        self.name = 'Ranger'
        self.hit_die = 10
        self.weapon_profs = ['simple', 'martial']
        self.armor_profs = ['simple', 'martial', 'shield']
        self.class_profs = ['athletics', 'insight', 'investigaion', 'nature', 'perception', 'stealth', 'survival']
        self.saves['str'] = 1
        self.saves['dex'] = 1
        self.gears = ['Scale Mail or Leather', 'Short Sword AND Short Sword OR Simple Melee Weapon AND Simple Melee Weapon', 'Dungeoneer Pack OR Explorer Pack', 'Longbow']
        self.spellcasting_ability = 'wis'
