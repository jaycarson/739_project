from classes.CharacterClass import CharacterClass, NoClass


class Bard(CharacterClass):
    def __init__(self):
        CharacterClass.__init__(self)
        self.name = 'Bard'
        self.hit_die = 8
        self.weapon_profs = ['simple', 'hand crossbow', 'long sword', 'rapier', 'short sword']
        self.armor_profs = ['light']
        self.class_prof_count = 3
        self.class_profs = ['all']
        self.tool_prof_count = 3
        self.instruments = ['flute', 'banjo', 'drum', 'eukalelie', 'harmonica']
        self.tool_profs = self.instruments
        self.saves['cha'] = 1
        self.saves['dex'] = 1
        self.gears = ['Rapier OR Longsword OR Simple Weapon', 'Diplomat Pack OR Entertainer Pack', 'Lute OR Music Instrument', 'Leather Armor', 'Dagger']
        self.spellcasting_ability = 'cha'

