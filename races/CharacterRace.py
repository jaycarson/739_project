class CharacterRace(object):
    def __init__(self):
        self.owner = None
        self.stats = {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0}
        self.saves = {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0}
        self.darkvision = 0
        self.name = 'None'
        self.size = 'Medium'
        self.speed = 30
        self.languages = ['common']
        self.special = []
        self.tool_profs = []
        self.class_profs = []
        self.weapon_profs = []
        self.armor_profs = []
        self.resistences = []


class NoRace(CharacterRace):
    def __init__(self):
        CharacterRace.__init__(self)
