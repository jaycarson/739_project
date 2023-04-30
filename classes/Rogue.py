from classes.CharacterClass import CharacterClass, NoClass


class Rogue(CharacterClass):
    def __init__(self):
        CharacterClass.__init__(self)
        self.name = 'Rogue'
        self.hit_die = 8
        self.weapon_profs = ['simple', 'hand crossbow', 'long sword', 'rapier', 'short sword']
        self.armor_profs = ['light']
        self.languages.append("thieve's cant")
        self.tool_profs = ["thive's tools"]
        self.tool_prof_count = 1
        self.class_profs = ['acrobatics', 'athletics', 'deception', 'insight', 'intimidation', 'investigation', 'perception', 'performance', 'persuasion', 'sleight of hand', 'stealth']
        self.class_prof_count = 4
        self.saves['int'] = 1
        self.saves['dex'] = 1
        self.gears = ['Rapier OR Shortsword', 'Short Bow OR Shortsword', 'Burglar Pack OR Dungeoneer Pack OR Explorer Pack', 'Leather Armor', 'Dagger', 'Dagger', 'Thieves Tools']
