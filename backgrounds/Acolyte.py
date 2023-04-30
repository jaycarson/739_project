from backgrounds.CharacterBackground import CharacterBackground


class Acolyte(CharacterBackground):
    def __init__(self):
        CharacterBackground.__init__(self)
        self.name = 'Acolyte'
        self.profs = ['insight', 'religion']
        self.gears = ['Holy Symbol', '5 Sticks of incense', 'vestments', 'common clothes']
        self.gold = 15
        self.language_count = 2
