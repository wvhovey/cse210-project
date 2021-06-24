# program entry point
from data import constants
from data.game import arcade
from data.game import game

def main():
    """ Start the game """
    window = game()
    window.start_new_game()
    arcade.run()


main()