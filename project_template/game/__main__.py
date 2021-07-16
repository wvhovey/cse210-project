""" -- main file --

class: n/a

methods: main()

"""

from data import constants
from data.game import arcade
from data.start_menu import start_menu

def main():
    """ the main function: compiles all code and runs the program. 

    args: none.
    """
    window = arcade.Window(constants.screen_width, constants.screen_height, constants.screen_title, fullscreen=True)
    width, height = window.get_size()

    window.set_viewport(0, width, 0, height)

    start_view = start_menu()
    window.show_view(start_view)
    arcade.run()

main()