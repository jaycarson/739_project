from races.CharacterRace import CharacterRace, NoRace


class Halfling(CharacterRace):
    def __init__(self):
        CharacterRace.__init__(self)
        self.stats['dex'] = 2
        self.languages.append('halfling')
        self.size = 'Small'
        self.speed = 25
        self.special = ['Brave: You have advantage on saving throws against being frightened', 'Halfling Nimbleness: You can move through the space of any creature that is of a size larger than yours.', 'Lucky: When you roll a 1 on the d20 for an attack roll, ability check, or saving throw, you can reroll the die and must use the new roll.']


class LightfootHalfling(Halfling):
    def __init__(self):
        Halfling.__init__(self)
        self.name = 'Lightfoot Halfling'
        self.stats['cha'] = 1
        self.special.append('Naturally Stealthy: You can attempt to hide even when you are obscured only by a creature htat is at least one size larger than you.')


class StoutHalfling(Halfling):
    def __init__(self):
        Halfling.__init__(self)
        self.name = 'Stout Halfling'
        self.stats['con'] = 1
        self.special.append('Stout: You have advantage on savign throws against poison, and you have resistance against poison damage.')
