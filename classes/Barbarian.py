from classes.CharacterClass import CharacterClass, NoClass


class Barbarian(CharacterClass):
    def __init__(self):
        CharacterClass.__init__(self)
        self.name = 'Barbarian'
        self.hit_die = 12
        self.weapon_profs = ['simple', 'martial']
        self.armor_profs = ['light', 'medium', 'shields']
        self.class_profs = ['animal handling', 'athletics', 'intimidation', 'nature', 'perception', 'survival']
        self.saves['str'] = 1
        self.saves['dex'] = 1
        self.gears = ['Greataxe OR Martial Melee Weapon', 'Handaxe AND Handaxe OR Simple Weapon', 'Explorer Pack', 'Javelin', 'Javelin', 'Javelin', 'Javelin']
