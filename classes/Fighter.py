from classes.CharacterClass import CharacterClass, NoClass


class Fighter(CharacterClass):
    def __init__(self):
        CharacterClass.__init__(self)
        self.name = 'Fighter'
        self.hit_die = 10
        self.weapon_profs = ['simple', 'martial']
        self.armor_profs = ['light', 'medium', 'heavy', 'shield']
        self.class_profs = ['acrobatics', 'animla handling', 'athletics', 'history' 'insight', 'intimidation', 'perception', 'survival']
        self.saves['str'] = 1
        self.saves['con'] = 1
        self.gears = ['Chain Mail OR Leather AND Longbow', 'Martial Weapon AND Shield OR Martial Weapon AND Martial Weapon', 'Light Crossbow OR Handaxe AND Handaxe', 'Dungeoneer Pack OR Explorer Pack']

