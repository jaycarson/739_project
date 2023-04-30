from pywebio.output import put_text, put_row, put_column, put_table, remove, put_scope, use_scope, clear


class CharacterSheet(object):
    def __init__(self): 
        self.rows = 10
        self.cols = 6
        
        self.table = []
        self.table_details = []

        for row in range(0, self.rows):
            self.table.append([])
            for col in range(0, self.cols):
                self.table[row].append('')
        for row in range(0, 6):
            self.table_details.append([])
            for col in range(0, 2):
                self.table_details[row].append('')

        self.table[0][0] = 'Name'
        self.table[1][0] = 'Race'
        self.table[2][0] = 'Class'
        self.table[3][0] = 'Level'
        self.table[4][0] = 'Proficiency'
        self.table[5][0] = 'Max HP'
        self.table[6][0] = 'Spell DC'
        self.table[7][0] = 'Dark Vision'

        self.table[0][3] = 'ATTR'
        self.table[0][4] = 'MOD'
        self.table[0][5] = 'SAVE'
        self.table[1][2] = 'STR'
        self.table[2][2] = 'DEX'
        self.table[3][2] = 'CON'
        self.table[4][2] = 'INT'
        self.table[5][2] = 'WIS'
        self.table[6][2] = 'CHA'
        
        self.table_details[0][0] = 'Specials'
        self.table_details[1][0] = 'Languages'
        self.table_details[2][0] = 'Armor Proficiencies'
        self.table_details[3][0] = 'Weapon Proficiencies'
        self.table_details[4][0] = 'Tool Proficiencies'
        self.table_details[5][0] = 'Gear'

    def __call__(self, character):
        specials = []
        languages = []
        weapon_profs = []
        armor_profs = []
        tool_profs = []
        darkvision = 0
        specials = []
        gears = []
        if character.character_race.name != 'None':
            languages = character.character_race.languages
            weapon_profs = character.character_race.weapon_profs
            armor_profs = character.character_race.armor_profs
            tool_profs = character.character_race.tool_profs
            darkvision = character.character_race.darkvision
            for item in character.character_race.special:
                specials.append(item)
        if character.character_class.name != 'None':
            character.max_hp = character.character_class.hit_die + character.get_mod('con')
            for language in character.character_class.languages:
                if language not in languages:
                    languages.append(language)
            for weapon in character.character_class.weapon_profs:
                if weapon not in weapon_profs:
                    weapon_profs.append(weapon)
            for armor in character.character_class.armor_profs:
                if armor not in armor_profs:
                    armor_profs.append(armor)
            for tool in character.character_class.tool_profs:
                if tool not in tool_profs:
                    tool_profs.append(tool)
            for special in character.character_class.special:
                if special not in specials:
                    specials.append(special)
            for gear in character.gears:
                gears.append(gear)
        
        self.table[0][1] = character.name
        self.table[1][1] = character.character_race.name
        self.table[2][1] = character.character_class.name
        self.table[3][1] = character.level
        self.table[4][1] = character.proficiency
        self.table[5][1] = character.max_hp
        if character.character_class.spellcasting_ability == 'None':
            self.table[6][1] = 'N/A'
        else:
            self.table[6][1] = character.get_spellcasting_dc()
        self.table[7][1] = darkvision
        
        self.table[1][3] = character.get_stat('str')
        self.table[2][3] = character.get_stat('dex')
        self.table[3][3] = character.get_stat('con')
        self.table[4][3] = character.get_stat('int')
        self.table[5][3] = character.get_stat('wis')
        self.table[6][3] = character.get_stat('cha')

        self.table[1][4] = character.get_mod('str')
        self.table[2][4] = character.get_mod('dex')
        self.table[3][4] = character.get_mod('con')
        self.table[4][4] = character.get_mod('int')
        self.table[5][4] = character.get_mod('wis')
        self.table[6][4] = character.get_mod('cha')

        self.table[1][5] = character.get_save('str')
        self.table[2][5] = character.get_save('dex')
        self.table[3][5] = character.get_save('con')
        self.table[4][5] = character.get_save('int')
        self.table[5][5] = character.get_save('wis')
        self.table[6][5] = character.get_save('cha')
        
        self.table_details[0][1] = '\n'.join(specials)
        self.table_details[1][1] = ', '.join(languages)
        self.table_details[2][1] = ', '.join(armor_profs)
        self.table_details[3][1] = ', '.join(weapon_profs)
        self.table_details[4][1] = ', '.join(tool_profs)
        self.table_details[5][1] = ', '.join(gears)

        clear()
        put_table(self.table)
        put_table(self.table_details)
