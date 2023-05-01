from pywebio.pin import put_input, put_radio
from pywebio.input import input, FLOAT, radio, input_group
from pywebio.output import put_text, put_row, put_column, put_table, remove, put_scope, use_scope, clear
from Character import Character
from ConnectionDB import ConnectionDB


class CharacterGUI(object):
    def __init__(self):
        self.new_char = Character()
        self.attrs = [15, 14, 13, 12, 10, 8]
        self.dm_name = ''
        self.connection = ConnectionDB()

    def main_menu(self):
        options = ['Create Character', 'See Existing Characters', 'Quit']
        return radio('Menu', options=options)

    def clear_screen(self):
        clear()

    def get_dm_name(self):
        self.dm_name = input('Dungeon Master Name')

    def get_char_name(self):
        self.new_char.name = input('Character')
        self.new_char.print_sheet()

    def get_char_race(self):
        self.new_char.change_race(radio('Race', options=self.new_char.races))
        self.new_char.print_sheet()

    def get_char_class(self):
        self.new_char.change_class(radio('Class', options=self.new_char.classes))
        self.new_char.print_sheet()

    def get_char_background(self):
        self.new_char.change_background(radio('Background', options=self.new_char.backgrounds))
        self.new_char.print_sheet()

    def get_char_gear(self):
        if self.new_char.level == 1:
            new_gear = []
            for gear in self.new_char.character_class.gears:
                if ' OR ' in gear:
                    choice = radio('Select', options=gear.split(' OR '))
                else:
                    choice = gear
                if ' AND ' in choice:
                    for item in choice.split(' AND '):
                        self.new_char.add_gear(item)
                else:
                    self.new_char.add_gear(choice)
                self.new_char.print_sheet()

    def get_char_stats(self):
        for stat in self.new_char.stats:
            self.new_char.stats[stat] = radio(stat, options=self.attrs)
            if self.new_char.stats[stat] in self.attrs:
                self.attrs.remove(self.new_char.stats[stat])
            self.new_char.print_sheet()
        self.attrs = [15, 14, 13, 12, 10, 8]

    def get_table(self):
        new_table = []
        #new_table.append((['Name'], ['DM'], ['Class'], ['Race'], ['Background'], ['Max HP'], ['Darkvision'], ['Level'], ['STR'], ['DEX'], ['CON'], ['INT'], ['WIS'], ['CHA'], ['Gear']))
        new_table.append(('Name', 'DM', 'Class', 'Race', 'Background', 'Max HP', 'Darkvision', 'Level', 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA', 'Gear'))
        content = self.connection.get_table()
        for row in content:
            new_table.append(row)
        print(content)
        put_table(new_table)

    def finalize_char(self):
        self.new_char.update_max_hp()
        self.new_char.print_sheet()
        return radio('Commit', options=['Yes', 'No'])

    def character_exists(self):
        return self.connection.exists(self.new_char.name, self.dm_name)

    def add_new_character(self):
        self.connection.add(self.new_char, self.dm_name)
