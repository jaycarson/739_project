from backgrounds.CharacterBackground import CharacterBackground


class Urchin(CharacterBackground):
    def __init__(self):
        CharacterBackground.__init__(self)
        self.name = 'Urchin'
        self.profs = ['sleight of hand', 'stealth']
        self.tool_prof_count = 2
        self.tool_profs = ['disguise kit', 'thieves tools']
        self.gears = ['small knife', 'common clothes', 'map']
        self.gold = 10
