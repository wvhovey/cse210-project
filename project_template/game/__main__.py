""" -- Main File --

Class: n/a

Methods: main()

"""

from data import constants
from data.game import arcade
from data.start_menu import Start_Menu

def main():
    """ The main function: compiles all code and runs the program. 

    Args: none.
    """
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    start_view = Start_Menu()
    window.show_view(start_view)
    arcade.run()

main()