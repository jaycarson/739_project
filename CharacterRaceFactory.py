from races.CharacterRace import CharacterRace, NoRace
from races.Dwarves import HillDwarf, MountainDwarf
from races.Elves import HighElf, WoodElf, Drow
from races.Gnomes import RockGnome, ForestGnome
from races.Halflings import LightfootHalfling, StoutHalfling
from races.Misc import HalfOrc, Tiefling, Human, HalfElf, DragonBorn


class CharacterRaceFactory(object):
    def __init__(self):
        self.DragonBorn = DragonBorn()
        self.Drow = Drow()
        self.ForestGnome = ForestGnome()
        self.LightfootHalfling = LightfootHalfling()
        self.HillDwarf = HillDwarf()
        self.Human = Human()
        self.HalfOrc = HalfOrc()
        self.HighElf = HighElf()
        self.MountainDwarf = MountainDwarf()
        self.RockGnome = RockGnome()
        self.StoutHalfling = StoutHalfling()
        self.Tiefling = Tiefling()
        self.WoodElf = WoodElf()

        self.races = {
            'Dragon Born': self.DragonBorn,
            'Drow': self.Drow,
            'Forest Gnome': self.ForestGnome,
            'Lightfoot Halfling': self.LightfootHalfling,
            'Hill Dwarf': self.HillDwarf,
            'Human': self.Human,
            'Half Orc': self.HalfOrc,
            'High Elf': self.HighElf,
            'Mountain Dwarf': self.MountainDwarf,
            'Rock Gnome': self.RockGnome,
            'Stout Halfling': self.StoutHalfling,
            'Tiefling': self.Tiefling,
            'Wood Elf': self.WoodElf,
        }
        self.no_race = NoRace()

    def __call__(self, name):
        if name in self.races:
            return self.races[name]
        else:
            return self.no_race

    def get_races(self):
        return self.races.keys()
