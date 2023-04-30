from backgrounds.CharacterBackground import CharacterBackground


class Entertainer(CharacterBackground):
    def __init__(self):
        CharacterBackground.__init__(self)
        self.name = 'Entertainer'
        self.profs = ['acrobatics', 'performance']
        self.tool_prof_count = 2
        self.tool_profs = ['disguise kit', 'instrument']
        self.gears = ['instrument', 'costume']
        self.gold = 15
