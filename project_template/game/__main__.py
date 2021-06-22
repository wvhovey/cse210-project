# program entry point
from data import constants
from data.asteroid_smasher import MyGame
from data.asteroid_smasher import arcade

def main():
    """ Start the game """
    window = MyGame()
    window.start_new_game()
    arcade.run()


main()