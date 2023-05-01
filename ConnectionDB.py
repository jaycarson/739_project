import sqlite3
import argparse


class ConnectionDB(object):
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.character_fields = '(KEY, CHAR_NAME, DM_NAME, CHAR_CLASS, CHAR_RACE, CHAR_BG, MAX_HP, DARKVISION, LVL, STR, DEX, CON, INT, WIS, CHA, GEARS)'

    def __call__(self):
        return

    def create_key(self, name, gm, lvl):
        return str(gm)+'-'+str(name)+'-'+str(lvl)

    def exists(self, character_name, gm, lvl=1):
        key = self.create_key(character_name, gm, lvl)
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM CHARACTERS WHERE KEY=?", (key,))

        rows = cursor.fetchall()
        #print('Rows: ' + str(len(rows)) + ': ' + str(rows))
        if len(rows) > 0:
            return True
        else:
            return False

    def add(self, character, gm):
        command = 'INSERT INTO CHARACTERS ' + self.character_fields
        command += ' VALUES ('
        command += '"' + self.create_key(character.name, gm, character.level) + '", '
        command += '"' + character.name + '", '
        command += '"' + gm + '", '
        command += '"' + character.character_class.name + '", '
        command += '"' + character.character_race.name + '", '
        command += '"' + character.character_background.name + '", '
        command += str(character.max_hp) + ', '
        command += str(character.dark_vision) + ', '
        command += str(character.level) + ', '
        command += str(character.stats['str']) + ', '
        command += str(character.stats['dex']) + ', '
        command += str(character.stats['con']) + ', '
        command += str(character.stats['int']) + ', '
        command += str(character.stats['wis']) + ', '
        command += str(character.stats['cha']) + ', '
        command += '"' + ','.join(character.gears) + '"'
        command += ')'
        cursor = self.conn.cursor()
        cursor.execute(command)
        self.conn.commit()
        cursor.close()

    def get_names(self, items):
        item_names = []
        for item in items:
            item_names.append(item.name)
        return ','.join(item_names)

    def get_table(self):
        cursor = self.conn.cursor()
        #cursor.execute("SELECT * FROM CHARACTERS")
        cursor.execute("SELECT CHAR_NAME, DM_NAME, CHAR_CLASS, CHAR_RACE, CHAR_BG, MAX_HP, DARKVISION, LVL, STR, DEX, CON, INT, WIS, CHA, GEARS FROM CHARACTERS")
        rows = cursor.fetchall()
        return rows

    def initialize(self):
        print("Dropping Table: CHARACTERS")
        self.conn.execute("DROP TABLE IF EXISTS CHARACTERS")
 
        print("Creating Table: CHARACTERS")
        table = """ CREATE TABLE CHARACTERS (
            KEY        CHAR(255) NOT NULL,
            CHAR_NAME  CHAR(25)  NOT NULL,
            DM_NAME    CHAR(25)  NOT NULL,
            CHAR_CLASS CHAR(25),
            CHAR_RACE  CHAR(25),
            CHAR_BG    CHAR(25),
            MAX_HP     INT,
            DARKVISION INT,
            LVL        INT,
            STR        INT,
            DEX        INT,
            CON        INT,
            INT        INT,
            WIS        INT,
            CHA        INT,
            GEARS      CHAR(255)
            ); """

        self.conn.execute(table)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description="""The Game""",
        )
    parser.add_argument(
            "-i", "--initialize",
            action="store_true",
            help="Initializes the database tables",
        )
    args = parser.parse_args()
    app = ConnectionDB()
    if args.initialize:
        app.initialize()
    app()
