from backgrounds.CharacterBackground import CharacterBackground


class Hermit(CharacterBackground):
    def __init__(self):
        CharacterBackground.__init__(self)
        self.name = 'Hermit'
        self.profs = ['medicine', 'religion']
        self.tool_prof_count = 1
        self.tool_profs = ['herbalism kit']
        self.gears = ['winter blanket', 'common clothes', 'herbalism kit']
        self.gold = 5
