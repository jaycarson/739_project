import unittest
from CharacterClassFactory import CharacterClassFactory
from CharacterBackgroundFactory import CharacterBackgroundFactory
from CharacterRaceFactory import CharacterRaceFactory
from ConnectionDB import ConnectionDB
from CharacterGUI import CharacterGUI


class Tests(unittest.TestCase):
    def test_has_all_classes(self):
        test_items = ['Bard', 'Barbarian', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
        factory = CharacterClassFactory()
        items = factory.get_classes()
        for test_item in test_items:
            self.assertIn(test_item, items)
        for item in items:
            self.assertIn(item, test_items)

    def test_has_all_backgrounds(self):
        test_items = ['Acolyte', 'Charlatan', 'Criminal', 'Entertainer', 'FolkHero', 'GuildArtisan', 'Hermit', 'Noble', 'Outlander', 'Sage', 'Sailor', 'Soldier', 'Urchin']
        factory = CharacterBackgroundFactory()
        items = factory.get_backgrounds()
        for test_item in test_items:
            self.assertIn(test_item, items)
        for item in items:
            self.assertIn(item, test_items)

    def test_has_all_races(self):
        test_items = ['Dragon Born', 'Drow', 'Forest Gnome', 'Lightfoot Halfling', 'Hill Dwarf', 'Human', 'Half Orc', 'High Elf', 'Mountain Dwarf', 'Rock Gnome', 'Stout Halfling', 'Tiefling', 'Wood Elf']
        factory = CharacterRaceFactory()
        items = factory.get_races()
        for test_item in test_items:
            self.assertIn(test_item, items)
        for item in items:
            self.assertIn(item, test_items)

    def test_factory_returns_the_correct_class(self):
        factory = CharacterClassFactory()
        item_names = factory.get_classes()
        for item in item_names:
            self.assertEqual(item, factory(item).name)

    def test_factory_returns_the_correct_background(self):
        factory = CharacterBackgroundFactory()
        item_names = factory.get_backgrounds()
        for item in item_names:
            self.assertEqual(item, factory(item).name)

    def test_factory_returns_the_correct_race(self):
        factory = CharacterRaceFactory()
        item_names = factory.get_races()
        for item in item_names:
            self.assertEqual(item, factory(item).name)

    def test_that_nonsense_is_not_in_db(self):
        connection = ConnectionDB()
        self.assertFalse(connection.exists(character_name='Fake Name', gm='Fake GM', lvl=1))

    def test_that_key_is_correct(self):
        connection = ConnectionDB()
        self.assertEqual(connection.create_key(name='Name', gm='GM', lvl=1), 'GM-Name-1')

    def test_attribute_distribution(self):
        gui = CharacterGUI()
        attribute_array = [15, 14, 13, 12, 10, 8]
        for item in attribute_array:
            self.assertIn(item, gui.attrs)





if __name__ == '__main__':
    unittest.main()
