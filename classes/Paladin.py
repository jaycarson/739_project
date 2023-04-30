from classes.CharacterClass import CharacterClass, NoClass


class Paladin(CharacterClass):
    def __init__(self):
        CharacterClass.__init__(self)
        self.name = 'Paladin'
        self.hit_die = 10
        self.weapon_profs = ['simple', 'martial']
        self.armor_profs = ['light', 'medium', 'heavy', 'shield']
        self.class_profs = ['athletics', 'insight', 'intimidation', 'medicine', 'persuasion', 'religion']
        self.saves['wis'] = 1
        self.saves['cha'] = 1
        self.gears = ['Martial Weapon AND Shield OR Martial Weapon AND Martial Weapon', 'Simple Melee Weapon OR Javelin AND Javelin AND Javelin AND Javelin AND Javelin', 'Priest Pack OR Explorer Pack', 'Chain Mail AND Holy Symbol']
        self.spellcasting_ability = 'cha'
