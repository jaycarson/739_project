from races.CharacterRace import CharacterRace, NoRace


class HalfOrc(CharacterRace):
    def __init__(self):
        CharacterRace.__init__(self)
        self.name = 'Half Orc'
        self.stats = {'str': 2, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'cha': 0}
        self.dark_vision = 60
        self.languages.append('orc')
        self.class_profs = ['intimidation']
        self.class_prof_count = 1
        self.special = ["Relentless Endurance: When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can't use this feature again until you finish a long rest", "Savage Attacks: When you score a critical hit with a melee weapon attack, you can roll one fohte weapon's damage dice one additional time and add it to the extra damage ofthe critical hit."]


class Tiefling(CharacterRace):
    def __init__(self):
        CharacterRace.__init__(self)
        self.name = 'Tiefling'
        self.stats = {'str': 0, 'dex': 0, 'con': 0, 'int': 1, 'wis': 0, 'cha': 2}
        self.dark_vision = 60
        self.languages.append('infernal')
        self.resistences = ['fire']
        self.special = ['Infernal Legacy: You know the Thaumaturgy cantrip.']
        self.special.append('Infernal Legacy: At 3rd Level, you can cast the hellish rebuke spell as a 2nd level spell once with this trait per long rest. Charisma is your spellcasting ability.')
        self.special.append('Infernal Legacy: At 5th Level, you can cast the darkness spell as a 2nd level spell once with this trait per long rest. Charisma is your spellcasting ability.')


class Human(CharacterRace):
    def __init__(self):
        CharacterRace.__init__(self)
        self.name = 'Human'
        self.stats = {'str': 1, 'dex': 1, 'con': 1, 'int': 1, 'wis': 1, 'cha': 1}
        #self.languages.append('halfling')  Choose one


class HalfElf(CharacterRace):
    def __init__(self):
        CharacterRace.__init__(self)
        self.name = 'Half Elf'
        self.stats = {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 2} # Plus choose 2 for +1
        self.dark_vision = 60
        self.languages.append('elvish')  # Plus choose 1
        self.class_profs = ['all']
        self.class_prof_count = 2
        self.special = ["Fey Ancestry: You have advantage on savign throws against being charmed, and magic can't put you to sleep."]

class DragonBorn(CharacterRace):
    def __init__(self):
        CharacterRace.__init__(self)
        self.name = 'Dragon Born'
        self.stats = {'str': 2, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 1}
        self.languages.append('draconic')
        self.special = ['Draconic Ancestry', 'Breath Weapon', 'Damage Resistence']

