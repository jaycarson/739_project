from backgrounds.CharacterBackground import CharacterBackground


class Sage(CharacterBackground):
    def __init__(self):
        CharacterBackground.__init__(self)
        self.name = 'Sage'
        self.profs = ['arcana', 'history']
        self.gears = ['bottle of black ink', 'quill', 'small knife', 'common clothes']
        self.language_count = 2
        self.gold = 10
