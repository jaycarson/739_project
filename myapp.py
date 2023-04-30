from CharacterGUI import CharacterGUI


def add_character(gui):
    running = True
    while running:
        gui.get_dm_name()
        gui.get_char_name()
        running = gui.character_exists()
    gui.get_char_race()
    gui.get_char_class()
    gui.get_char_background()
    gui.get_char_gear()
    gui.get_char_stats()
    finalize = gui.finalize_char()
    if finalize == 'Yes':
        gui.add_new_character()
        print("FINALIZED")


def run():
    gui = CharacterGUI()
    running = True

    while running:
        option = gui.main_menu()
        if option == 'Create Character':
            gui.clear_screen()
            add_character(gui)
            gui.clear_screen()
        elif option == 'See Existing Characters':
            gui.clear_screen()
            gui.get_table()            
        else:
            running = False


if __name__ == '__main__':
    run()
