# program entry point
from data import constants
from data.game import arcade
from data.start_menu import Start_Menu

def main():
    """ Start the game """
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    start_view = Start_Menu()
    window.show_view(start_view)
    arcade.run()

main() 