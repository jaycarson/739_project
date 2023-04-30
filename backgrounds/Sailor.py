from backgrounds.CharacterBackground import CharacterBackground


class Sailor(CharacterBackground):
    def __init__(self):
        CharacterBackground.__init__(self)
        self.name = 'Sailor'
        self.profs = ['athletics', 'perception']
        self.tool_prof_count = 2
        self.tool_profs = ['navigators tools', 'vehicles (water)']
        self.gears = ['club', '50 ft silk rope', 'lucky charm', 'common clothes']
        self.gold = 10
