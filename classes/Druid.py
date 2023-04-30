from classes.CharacterClass import CharacterClass, NoClass


class Druid(CharacterClass):
    def __init__(self):
        CharacterClass.__init__(self)
        self.name = 'Druid'
        self.hit_die = 8
        self.weapon_profs = ['club', 'dagger', 'dart', 'javelin', 'mace', 'quarterstaff', 'scimitar', 'sickle', 'sling', 'spear']
        self.armor_profs = ['light', 'medium', 'shield']
        self.languages.append('druidic')
        self.class_profs = ['arcana', 'animal handling', 'insight', 'medicine', 'nature', 'perceptions', 'religion', 'survival']
        self.tool_prof_count = 1
        self.tool_profs = ['herbalism kit']
        self.saves['int'] = 1
        self.saves['wis'] = 1
        self.gears = ['Wooden Shield OR Simple Weapon', 'Scimitar OR Simple Weapon', 'Leather', 'Explorer Pack', 'Druidic Focus']
