from backgrounds.CharacterBackground import CharacterBackground


class Charlatan(CharacterBackground):
    def __init__(self):
        CharacterBackground.__init__(self)
        self.name = 'Charlatan'
        self.profs = ['deception', 'sleight of hand']
        self.tool_prof_count = 2
        self.tool_profs = ['disguise kit', 'forgery kit']
        self.gears = ['fine clothes', 'disguise kit']
        self.gold = 15
