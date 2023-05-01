from races.CharacterRace import CharacterRace, NoRace


class Gnome(CharacterRace):
    def __init__(self):
        CharacterRace.__init__(self)
        self.size = 'Small'
        self.speed = 25
        self.dark_vision = 60
        self.languages.append('gnomish')
        self.special = ['Gnomish Cunning: You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic']
        self.stats['int'] = 2


class RockGnome(Gnome):
    def __init__(self):
        Gnome.__init__(self)
        self.name = 'Rock Gnome'
        self.stats['con'] = 1
        self.special.append("Artificer's Lore: Whenever you make an Intelligence (History) check related to magic items, alchemical objects, or technological devices, you can add twice your proficiency bonus, instead of an proficiencey bonus you normally apply.")
        self.special.append("Tinker: For 10 GP and 1 Hour, construct a Clockwork TOw, Fire Starter, or Music Box. You may have up to 3 and can reclaim materials.")
        self.tool_profs = ["tinker's tools"]
        self.tool_prof_count = 1


class ForestGnome(Gnome):
    def __init__(self):
        Gnome.__init__(self)
        self.name = 'Forest Gnome'
        self.stats['dex'] = 1
        self.special.append('Natural Illusionist: You know the minor illusion cantrip. Intelligence is your spelcasting ability for it')
        self.special.append('Speak with small Beasts: Through sounds and gestrures, you can communicate simple ideas with Small or small beasts. Forest gnomes love animals and often keep squirrels, badgers, rabbits, moles, woodpeckers, and other creatures as beloved pets.')
