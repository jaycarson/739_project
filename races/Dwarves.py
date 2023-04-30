from races.CharacterRace import CharacterRace, NoRace


class Dwarf(CharacterRace):
    def __init__(self):
        CharacterRace.__init__(self)
        self.special = ['Dwarven Resiliance: You have advantage on saving throws against poison, an dyou have resistance against poison damage']
        self.tool_profs = ["smith's tools", "brewer's supplies", "mason's tools"]
        self.weapon_profs = ['battleaxe', 'handaxe', 'light hammer', 'warhammer']
        self.languages.append('dwarvish')
        self.darkvision = 60
        self.tool_prof_count = 1
        self.stats['con'] = 2


class HillDwarf(Dwarf):
    def __init__(self):
        Dwarf.__init__(self)
        self.name = 'Hill Dwarf'
        self.special.append('Dwarven Toughness: Your hit point maximum increases by 1, and it increases by 1 every time you gain a level')
        self.stats['wis'] = 1


class MountainDwarf(Dwarf):
    def __init__(self):
        Dwarf.__init__(self)
        self.name = 'Mountain Dwarf'
        self.armor_profs = ['light', 'medium']
        self.stats['str'] = 2
