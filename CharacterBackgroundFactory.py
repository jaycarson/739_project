from backgrounds.CharacterBackground import CharacterBackground, NoBG
from backgrounds.Acolyte import Acolyte
from backgrounds.Charlatan import Charlatan
from backgrounds.Criminal import Criminal
from backgrounds.Entertainer import Entertainer
from backgrounds.FolkHero import FolkHero
from backgrounds.GuildArtisan import GuildArtisan
from backgrounds.Hermit import Hermit
from backgrounds.Noble import Noble
from backgrounds.Outlander import Outlander
from backgrounds.Sage import Sage
from backgrounds.Sailor import Sailor
from backgrounds.Soldier import Soldier
from backgrounds.Urchin import Urchin


class CharacterBackgroundFactory(object):
    def __init__(self):
        self.acolyte = Acolyte()
        self.charlatan = Charlatan()
        self.criminal = Criminal()
        self.entertainer = Entertainer()
        self.folkHero = FolkHero()
        self.guildArtisan = GuildArtisan()
        self.hermit = Hermit()
        self.noble = Noble()
        self.outlander = Outlander()
        self.sage = Sage()
        self.sailor = Sailor()
        self.soldier = Soldier()
        self.urchin = Urchin()

        self.bgs = {
            'Acolyte': self.acolyte,
            'Charlatan': self.charlatan,
            'Criminal': self.criminal,
            'Entertainer': self.entertainer,
            'FolkHero': self.folkHero,
            'GuildArtisan': self.guildArtisan,
            'Hermit': self.hermit,
            'Noble': self.noble,
            'Outlander': self.outlander,
            'Sage': self.sage,
            'Sailor': self.sailor,
            'Soldier': self.soldier,
            'Urchin': self.urchin,
        }
        self.no_bg = NoBG()
        return

    def __call__(self, name):
        if name in self.bgs:
            return self.bgs[name]
        else:
            return self.no_bg

    def get_backgrounds(self):
        return self.bgs.keys()
