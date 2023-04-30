from backgrounds.CharacterBackground import CharacterBackground


class Noble(CharacterBackground):
    def __init__(self):
        CharacterBackground.__init__(self)
        self.name = 'Noble'
        self.profs = ['history', 'persuasion']
        self.tool_prof_count = 1
        self.tool_profs = ['gaming set']
        self.gears = ['fine clothes', 'signet ring', 'scroll of pedigree']
        self.language_count = 1
        self.gold = 15
