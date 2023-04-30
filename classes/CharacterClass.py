class CharacterClass(object):
    def __init__(self):
        self.owner = None
        self.darkvision = 0
        self.name = 'None'
        self.stats = {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0}
        self.hit_die = 8
        self.proficiencies = {
             1: 2,  2: 2,  3: 2,  4: 2,  5: 3,  6: 3,  7: 3,  8: 3,  9: 4, 10: 4,
            11: 4, 12: 4, 13: 5, 14: 5, 15: 5, 16: 5, 17: 6, 18: 6, 19: 6, 20: 6,
        }
        self.saves = {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0}
        self.weapon_profs = []
        self.armor_profs = []
        self.languages = []
        self.class_prof_count = 2
        self.class_profs = []
        self.tool_prof_count = 0
        self.tool_profs = []
        self.special = []
        self.instruments = ['flute', 'banjo', 'drum', 'eukalelie', 'harmonica']
        self.gears = []
        self.spellcasting_ability = 'None'


class NoClass(CharacterClass):
    def __init__(self):
        CharacterClass.__init__(self)

