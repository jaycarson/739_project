from backgrounds.CharacterBackground import CharacterBackground


class GuildArtisan(CharacterBackground):
    def __init__(self):
        CharacterBackground.__init__(self)
        self.name = 'GuildArtisan'
        self.profs = ['insight', 'persuasion']
        self.tool_prof_count = 1
        self.tool_profs = ['artisan tools']
        self.gears = ['artisan tools', 'travelers clothes']
        self.language_count = 1
        self.gold = 15
