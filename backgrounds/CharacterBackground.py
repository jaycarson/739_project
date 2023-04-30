class CharacterBackground(object):
    def __init__(self):
        self.owner = None
        self.name = 'None'
        self.weapon_profs = []
        self.armor_profs = []
        self.languages = []
        self.prof_count = 2
        self.profs = []
        self.tool_prof_count = 0
        self.tool_profs = []
        self.special = []
        self.instruments = ['flute', 'banjo', 'drum', 'eukalelie', 'harmonica']
        self.gears = []
        self.gold = 0


class NoBG(CharacterBackground):
    def __init__(self):
        CharacterBackground.__init__(self)

