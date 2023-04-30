from backgrounds.CharacterBackground import CharacterBackground


class FolkHero(CharacterBackground):
    def __init__(self):
        CharacterBackground.__init__(self)
        self.name = 'FolkHero'
        self.weapon_profs = []
        self.armor_profs = []
        self.profs = ['animal handling', 'survival']
        self.tool_prof_count = 2
        self.tool_profs = ['artisan tools', 'vehicle (land)']
        self.gears = []
        self.gold = 10
