from backgrounds.CharacterBackground import CharacterBackground


class Soldier(CharacterBackground):
    def __init__(self):
        CharacterBackground.__init__(self)
        self.name = 'Soldier'
        self.profs = ['athletics', 'intimidation']
        self.tool_prof_count = 1
        self.tool_profs = ['gaming set', 'vehicles (land)']
        self.gears = ['insignia of rank', 'trophy from a fallen enemy', 'set of dice', 'common clothes']
        self.gold = 10
