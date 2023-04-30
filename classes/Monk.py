from classes.CharacterClass import CharacterClass, NoClass


class Monk(CharacterClass):
    def __init__(self):
        CharacterClass.__init__(self)
        self.name = 'Monk'
        self.hit_die = 8
        self.weapon_profs = ['simple', 'short sword']
        self.armor_profs = []
        self.class_profs = ['acrobatics', 'animla handling', 'athletics', 'history' 'insight', 'intimidation', 'perception', 'survival']
        self.tool_prof_count = 1
        self.tool_profs = self.instruments
        self.tool_profs.append('artisan tools')
        self.saves['str'] = 1
        self.saves['dex'] = 1
        self.gears = ['Shortsword OR Simple Weapon', 'Dungeoneer Pack or Explorer Pack', 'Dart', 'Dart', 'Dart', 'Dart', 'Dart', 'Dart', 'Dart', 'Dart', 'Dart', 'Dart']

