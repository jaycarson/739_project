from backgrounds.CharacterBackground import CharacterBackground


class Outlander(CharacterBackground):
    def __init__(self):
        CharacterBackground.__init__(self)
        self.name = 'Outlander'
        self.profs = ['athletics', 'survival']
        self.tool_prof_count = 1
        self.tool_profs = ['instrument']
        self.gears = ['staff', 'hunting trap', 'travelers clothes']
        self.gold = 10
