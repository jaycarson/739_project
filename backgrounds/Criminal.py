from backgrounds.CharacterBackground import CharacterBackground


class Criminal(CharacterBackground):
    def __init__(self):
        CharacterBackground.__init__(self)
        self.name = 'Criminal'
        self.profs = ['deception', 'stealth']
        self.tool_prof_count = 2
        self.tool_profs = ['gaming set', 'thieves tools']
        self.gears = ['crowbar', 'common clothes']
        self.gold = 15
