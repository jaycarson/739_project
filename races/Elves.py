from races.CharacterRace import CharacterRace, NoRace


class Elf(CharacterRace):
    def __init__(self):
        CharacterRace.__init__(self)
        self.darkvision = 60
        self.special = ['Keen Senses: You have proficiency in the Perception skill', "Fey Ancestry: You have advantage on savign throws against being charmed, and magic can't put you to sleep."]
        self.languages.append('elvish')
        self.class_profs = ['perception']
        self.weapon_profs = ['long sword', 'short sword', 'short bow', 'long bow']
        self.stats['dex'] = 2


class HighElf(Elf):
    def __init__(self):
        Elf.__init__(self)
        self.name = 'High Elf'
        self.stats['int'] = 1
        self.special.append('Cantrips: You know one cantrip of our choice from the wizard spell list. Intelligence is your spellcasting ability for it.')
        self.special.append('Extra Language: You can speak, read, and write one extra language of your choice')


class WoodElf(Elf):
    def __init__(self):
        Elf.__init__(self)
        self.name = 'Wood Elf'
        self.stats['wis'] = 1
        self.speed = 35
        self.special.append('Fleet of Foot: Your base walking speed is increased to 35 feet.')
        self.special.append('Mask of hte Wild: You can attempt to hide even when you are only lightly obscurred by foliage, heavy rain, falling snow, mist, and other natural phenomena.')


class Drow(Elf):
    def __init__(self):
        Elf.__init__(self)
        self.name = 'Drow'
        self.stats['cha'] = 1
        self.darkvision = 120
        self.special.append('Sunlight Sensitivity: You have disadvantage on attack rolls and on Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight.')
        self.special.append('Drow Magic: You may cast Dancing Lights Cantrip.')
        self.special.append('Drow Magic: At 3rd Level, you may cast Fairie Fire once per long rest. Charisma is your spellcasting ability.')
        self.special.append('Drow Magic: At 5th Level, you may cast Darkness once per long rest. Charisma is your spellcasting ability.')
        self.weapon_profs = ['rapier', 'shortsword', 'hand crossbow']
